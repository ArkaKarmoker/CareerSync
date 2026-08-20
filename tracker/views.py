import csv
from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.contrib.auth import authenticate, login, update_session_auth_hash
from django.contrib.auth.models import User
from django.contrib.auth.forms import PasswordChangeForm, AuthenticationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse, reverse_lazy
from django.contrib import messages
from django.db.models import Count, Q

from .models import JobApplication, Interview, JobAnalysis, UserProfile
from .forms import UserRegisterForm, JobApplicationForm, InterviewForm, UserProfileUpdateForm, UserProfileDetailsForm
from .ai_utils import generate_job_analysis

def login_view(request):
    if request.user.is_authenticated:
        return redirect('dashboard')

    if request.method == 'POST':
        username_or_email = request.POST.get('username', '').strip()
        password = request.POST.get('password', '')

        # Resolve user by username or email
        user_obj = User.objects.filter(Q(username__iexact=username_or_email) | Q(email__iexact=username_or_email)).first()
        auth_username = user_obj.username if user_obj else username_or_email

        user = authenticate(request, username=auth_username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, f"Welcome back, {user.first_name or user.username}!")
            next_url = request.POST.get('next') or request.GET.get('next')
            if next_url and next_url.startswith('/'):
                return redirect(next_url)
            return redirect('dashboard')
        else:
            messages.error(request, "Please enter a correct username/email and password. Note that both fields may be case-sensitive.")
            request.session['login_username'] = username_or_email
            next_param = request.GET.get('next', '')
            redirect_url = reverse('login')
            if next_param:
                redirect_url += f"?next={next_param}"
            return redirect(redirect_url)
    else:
        initial_username = request.session.pop('login_username', '')
        form = AuthenticationForm(initial={'username': initial_username})

    context = {
        'form': form,
        'initial_username': initial_username,
    }
    return render(request, 'tracker/login.html', context)

def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.first_name = form.cleaned_data.get('first_name', '')
            user.last_name = form.cleaned_data.get('last_name', '')
            user.set_password(form.cleaned_data['password'])
            user.save()
            login(request, user)
            messages.success(request, "Registration successful!")
            return redirect('dashboard')
    else:
        form = UserRegisterForm()
    return render(request, 'tracker/register.html', {'form': form})

@login_required
def profile(request):
    user_profile, _ = UserProfile.objects.get_or_create(user=request.user)

    if request.method == 'POST':
        if 'update_skills' in request.POST:
            p_form = UserProfileUpdateForm(instance=request.user)
            d_form = UserProfileDetailsForm(request.POST, instance=user_profile)
            pass_form = PasswordChangeForm(user=request.user)
            if d_form.is_valid():
                d_form.save()
                messages.success(request, "Your AI skills and professional profile have been updated successfully!")
                return redirect('profile')
            else:
                messages.error(request, "Please correct the errors in your skills profile.")

        elif 'update_account' in request.POST:
            p_form = UserProfileUpdateForm(request.POST, instance=request.user)
            d_form = UserProfileDetailsForm(instance=user_profile)
            pass_form = PasswordChangeForm(user=request.user)
            if p_form.is_valid():
                p_form.save()
                messages.success(request, "Your account information has been updated successfully!")
                return redirect('profile')
            else:
                messages.error(request, "Please correct the account information errors below.")

        elif 'update_profile' in request.POST:
            p_form = UserProfileUpdateForm(request.POST, instance=request.user)
            d_form = UserProfileDetailsForm(request.POST, instance=user_profile)
            pass_form = PasswordChangeForm(user=request.user)
            if p_form.is_valid() and d_form.is_valid():
                p_form.save()
                d_form.save()
                messages.success(request, "Your profile and skills have been updated successfully!")
                return redirect('profile')
            else:
                messages.error(request, "Please correct the profile errors below.")
        elif 'change_password' in request.POST:
            p_form = UserProfileUpdateForm(instance=request.user)
            d_form = UserProfileDetailsForm(instance=user_profile)
            pass_form = PasswordChangeForm(user=request.user, data=request.POST)
            if pass_form.is_valid():
                user = pass_form.save()
                update_session_auth_hash(request, user)
                messages.success(request, "Your password has been changed successfully!")
                return redirect('profile')
            else:
                messages.error(request, "Please correct the password errors below.")
    else:
        p_form = UserProfileUpdateForm(instance=request.user)
        d_form = UserProfileDetailsForm(instance=user_profile)
        pass_form = PasswordChangeForm(user=request.user)

    context = {
        'p_form': p_form,
        'd_form': d_form,
        'pass_form': pass_form,
        'user_profile': user_profile,
    }
    return render(request, 'tracker/profile.html', context)


@login_required
def dashboard(request):
    applications = JobApplication.objects.filter(user=request.user)
    
    total_apps = applications.count()
    status_counts = applications.values('status').annotate(count=Count('status'))
    
    recent_apps = applications.order_by('-created_at')[:5]
    upcoming_interviews = Interview.objects.filter(application__user=request.user).order_by('interview_date')[:5]

    # Top 5 AI matched jobs — only those with an analysis and a match_score, sorted by highest score
    top_ai_matches = (
        applications
        .filter(analysis__isnull=False, analysis__match_score__isnull=False)
        .select_related('analysis')
        .order_by('-analysis__match_score')[:5]
    )

    context = {
        'total_apps': total_apps,
        'status_counts': status_counts,
        'recent_apps': recent_apps,
        'upcoming_interviews': upcoming_interviews,
        'top_ai_matches': top_ai_matches,
    }
    return render(request, 'tracker/dashboard.html', context)

class ApplicationListView(LoginRequiredMixin, ListView):
    model = JobApplication
    template_name = 'tracker/application_list.html'
    context_object_name = 'applications'
    paginate_by = 5

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        from .models import Category
        context['categories'] = Category.objects.all()
        
        # Build query string for pagination links (preserves search, filters & sort, excluding 'page')
        query_params = self.request.GET.copy()
        if 'page' in query_params:
            del query_params['page']
        context['query_params'] = query_params.urlencode()

        # Build query string for sorting headers (preserves search & filters, excluding 'sort' & 'page')
        sort_params = self.request.GET.copy()
        if 'page' in sort_params:
            del sort_params['page']
        if 'sort' in sort_params:
            del sort_params['sort']
        context['sort_base_url'] = sort_params.urlencode()
        context['current_sort'] = self.request.GET.get('sort', '')
        return context

    def get_queryset(self):
        queryset = JobApplication.objects.filter(user=self.request.user)
        q = self.request.GET.get('q')
        status = self.request.GET.get('status')
        location = self.request.GET.get('location')
        category = self.request.GET.get('category')
        sort = self.request.GET.get('sort')
        
        if q:
            queryset = queryset.filter(Q(job_title__icontains=q) | Q(company_name__icontains=q) | Q(tags__icontains=q))
        if status:
            queryset = queryset.filter(status=status)
        if location:
            queryset = queryset.filter(location__icontains=location)
        if category:
            queryset = queryset.filter(category_id=category)
            
        # Dynamic Column Sorting
        sort_mapping = {
            'company': 'company_name',
            '-company': '-company_name',
            'role': 'job_title',
            '-role': '-job_title',
            'category': 'category__name',
            '-category': '-category__name',
            'location': 'location',
            '-location': '-location',
            'status': 'status',
            '-status': '-status',
            'date': 'application_date',
            '-date': '-application_date',
        }
        
        from django.db.models import F
        
        if sort and sort in sort_mapping:
            order_field = sort_mapping[sort]
            if order_field in ['application_date', '-application_date']:
                return queryset.order_by(order_field, '-created_at')
            else:
                # Provide a secondary sort by date to keep things predictable within the same category/status
                return queryset.order_by(order_field, F('application_date').desc(nulls_last=True), '-created_at')
        else:
            # Default: Latest application dates first, null dates at the end, then fallback to newest entries
            return queryset.order_by(F('application_date').desc(nulls_last=True), '-created_at')

class ApplicationDetailView(LoginRequiredMixin, DetailView):
    model = JobApplication
    template_name = 'tracker/application_detail.html'
    context_object_name = 'application'

    def get_queryset(self):
        return JobApplication.objects.filter(user=self.request.user)

class ApplicationCreateView(LoginRequiredMixin, CreateView):
    model = JobApplication
    form_class = JobApplicationForm
    template_name = 'tracker/application_form.html'
    success_url = reverse_lazy('application_list')

    def form_valid(self, form):
        form.instance.user = self.request.user
        messages.success(self.request, "Application created successfully.")
        return super().form_valid(form)

class ApplicationUpdateView(LoginRequiredMixin, UpdateView):
    model = JobApplication
    form_class = JobApplicationForm
    template_name = 'tracker/application_form.html'

    def get_queryset(self):
        return JobApplication.objects.filter(user=self.request.user)

    def get_success_url(self):
        messages.success(self.request, "Application updated successfully.")
        return reverse_lazy('application_detail', kwargs={'pk': self.object.pk})

class ApplicationDeleteView(LoginRequiredMixin, DeleteView):
    model = JobApplication
    template_name = 'tracker/application_confirm_delete.html'
    success_url = reverse_lazy('application_list')

    def get_queryset(self):
        return JobApplication.objects.filter(user=self.request.user)

class InterviewCreateView(LoginRequiredMixin, CreateView):
    model = Interview
    form_class = InterviewForm
    template_name = 'tracker/interview_form.html'

    def form_valid(self, form):
        application = get_object_or_404(JobApplication, pk=self.kwargs['application_id'], user=self.request.user)
        form.instance.application = application
        messages.success(self.request, "Interview added successfully.")
        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy('application_detail', kwargs={'pk': self.kwargs['application_id']})

class InterviewUpdateView(LoginRequiredMixin, UpdateView):
    model = Interview
    form_class = InterviewForm
    template_name = 'tracker/interview_form.html'

    def get_queryset(self):
        return Interview.objects.filter(application__user=self.request.user)

    def get_success_url(self):
        messages.success(self.request, "Interview updated successfully.")
        return reverse_lazy('application_detail', kwargs={'pk': self.object.application.pk})

class InterviewDeleteView(LoginRequiredMixin, DeleteView):
    model = Interview
    template_name = 'tracker/interview_confirm_delete.html'

    def get_queryset(self):
        return Interview.objects.filter(application__user=self.request.user)

    def get_success_url(self):
        messages.success(self.request, "Interview deleted successfully.")
        return reverse_lazy('application_detail', kwargs={'pk': self.object.application.pk})

@login_required
def analyze_job(request, application_id):
    application = get_object_or_404(JobApplication, pk=application_id, user=request.user)
    
    if not application.job_description:
        messages.error(request, "Please add a job description to analyze.")
        return redirect('application_detail', pk=application_id)
        
    try:
        user_profile, _ = UserProfile.objects.get_or_create(user=request.user)
        user_skills = user_profile.skills or ""
        
        analysis_data = generate_job_analysis(application.job_description, user_skills=user_skills)
        
        # Helper to handle lists returned by LLM
        def parse_to_string(value, is_bulleted=False):
            if isinstance(value, list):
                if is_bulleted:
                    return '\n'.join(f"- {item}" for item in value)
                return ', '.join(str(item) for item in value)
            return str(value) if value else ''

        # Parse match score safely
        raw_score = analysis_data.get('match_score', 85)
        try:
            match_score = int(str(raw_score).replace('%', '').strip())
        except (ValueError, TypeError):
            match_score = 85

        analysis, created = JobAnalysis.objects.update_or_create(
            application=application,
            defaults={
                'job_summary': parse_to_string(analysis_data.get('job_summary')),
                'required_skills': parse_to_string(analysis_data.get('required_skills')),
                'required_experience': parse_to_string(analysis_data.get('required_experience')),
                'important_technologies': parse_to_string(analysis_data.get('important_technologies')),
                'interview_preparation_suggestions': parse_to_string(analysis_data.get('interview_preparation_suggestions'), is_bulleted=True),
                'match_score': match_score,
                'match_analysis': parse_to_string(analysis_data.get('match_analysis')),
                'interview_questions': parse_to_string(analysis_data.get('interview_questions'), is_bulleted=True),
            }
        )
        messages.success(request, "AI Analysis completed successfully!")
    except Exception as e:
        messages.error(request, f"AI Analysis failed: {str(e)}")
        
    return redirect(f"{reverse('application_detail', kwargs={'pk': application_id})}?ai=1")

@login_required
def export_applications_csv(request):
    response = HttpResponse(content_type='text/csv; charset=utf-8')
    response['Content-Disposition'] = 'attachment; filename="careersync_applications.csv"'
    
    # Write UTF-8 BOM for Excel compatibility
    response.write('\ufeff')

    writer = csv.writer(response)
    writer.writerow([
        'ID', 'Company Name', 'Job Title', 'Status', 'Category', 
        'Location', 'Application Date', 'Tags', 'Salary Range', 
        'Job URL', 'Job Description', 'Notes', 'AI Match Score'
    ])

    applications = JobApplication.objects.filter(user=request.user).select_related('category', 'analysis').order_by('-application_date')

    # Also respect search/filters if user exported from a filtered list
    q = request.GET.get('q', '').strip()
    status = request.GET.get('status', '').strip()
    category = request.GET.get('category', '').strip()
    location = request.GET.get('location', '').strip()

    if q:
        applications = applications.filter(
            Q(company_name__icontains=q) | 
            Q(job_title__icontains=q) | 
            Q(notes__icontains=q)
        )
    if status:
        applications = applications.filter(status=status)
    if category:
        applications = applications.filter(category_id=category)
    if location:
        applications = applications.filter(location__icontains=location)

    for app in applications:
        match_score = f"{app.analysis.match_score}%" if hasattr(app, 'analysis') and app.analysis and app.analysis.match_score is not None else 'N/A'
        writer.writerow([
            app.id,
            app.company_name,
            app.job_title,
            app.get_status_display(),
            app.category.name if app.category else '',
            app.location or '',
            app.application_date.strftime('%Y-%m-%d') if app.application_date else '',
            app.tags or '',
            app.salary or '',
            app.job_url or '',
            app.job_description or '',
            app.notes or '',
            match_score
        ])

    return response
