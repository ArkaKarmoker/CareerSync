from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, update_session_auth_hash
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse, reverse_lazy
from django.contrib import messages
from django.db.models import Count, Q

from .models import JobApplication, Interview, JobAnalysis
from .forms import UserRegisterForm, JobApplicationForm, InterviewForm, UserProfileUpdateForm
from .ai_utils import generate_job_analysis

@login_required
def profile(request):
    if request.method == 'POST':
        if 'update_profile' in request.POST:
            p_form = UserProfileUpdateForm(request.POST, instance=request.user)
            pass_form = PasswordChangeForm(user=request.user)
            if p_form.is_valid():
                p_form.save()
                messages.success(request, "Your profile information has been updated successfully!")
                return redirect('profile')
            else:
                messages.error(request, "Please correct the profile errors below.")
        elif 'change_password' in request.POST:
            p_form = UserProfileUpdateForm(instance=request.user)
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
        pass_form = PasswordChangeForm(user=request.user)

    context = {
        'p_form': p_form,
        'pass_form': pass_form,
    }
    return render(request, 'tracker/profile.html', context)

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
def dashboard(request):
    applications = JobApplication.objects.filter(user=request.user)
    
    total_apps = applications.count()
    status_counts = applications.values('status').annotate(count=Count('status'))
    
    recent_apps = applications.order_by('-created_at')[:5]
    upcoming_interviews = Interview.objects.filter(application__user=request.user).order_by('interview_date')[:5]

    context = {
        'total_apps': total_apps,
        'status_counts': status_counts,
        'recent_apps': recent_apps,
        'upcoming_interviews': upcoming_interviews,
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
        analysis_data = generate_job_analysis(application.job_description)
        
        # Helper to handle lists returned by LLM
        def parse_to_string(value, is_bulleted=False):
            if isinstance(value, list):
                if is_bulleted:
                    return '\n'.join(f"- {item}" for item in value)
                return ', '.join(str(item) for item in value)
            return str(value) if value else ''

        analysis, created = JobAnalysis.objects.update_or_create(
            application=application,
            defaults={
                'job_summary': parse_to_string(analysis_data.get('job_summary')),
                'required_skills': parse_to_string(analysis_data.get('required_skills')),
                'required_experience': parse_to_string(analysis_data.get('required_experience')),
                'important_technologies': parse_to_string(analysis_data.get('important_technologies')),
                'interview_preparation_suggestions': parse_to_string(analysis_data.get('interview_preparation_suggestions'), is_bulleted=True),
            }
        )
        messages.success(request, "AI Analysis completed successfully!")
    except Exception as e:
        messages.error(request, f"AI Analysis failed: {str(e)}")
        
    return redirect(f"{reverse('application_detail', kwargs={'pk': application_id})}?ai=1")
