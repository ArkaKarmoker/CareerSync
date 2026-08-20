from django import forms
from django.contrib.auth.models import User
from .models import JobApplication, Interview, UserProfile

class UserRegisterForm(forms.ModelForm):
    first_name = forms.CharField(max_length=30, required=False, label="First Name")
    last_name = forms.CharField(max_length=30, required=False, label="Last Name")
    email = forms.EmailField(required=True, label="Email Address")
    password = forms.CharField(widget=forms.PasswordInput)
    password_confirm = forms.CharField(widget=forms.PasswordInput, label="Confirm Password")

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'password']

    def clean_email(self):
        email = self.cleaned_data.get('email', '').strip()
        if email:
            if User.objects.filter(email__iexact=email).exists():
                raise forms.ValidationError("An account with this email already exists.")
        return email

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get("password")
        password_confirm = cleaned_data.get("password_confirm")

        if password and password_confirm and password != password_confirm:
            raise forms.ValidationError("Passwords do not match!")

class UserProfileUpdateForm(forms.ModelForm):
    email = forms.EmailField(required=True, label="Email Address")

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email']

    def clean_email(self):
        email = self.cleaned_data.get('email', '').strip()
        if email:
            if User.objects.filter(email__iexact=email).exclude(pk=self.instance.pk).exists():
                raise forms.ValidationError("This email is already in use by another account.")
        return email

class UserProfileDetailsForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ['headline', 'skills', 'experience_years', 'bio']
        labels = {
            'headline': 'Professional Title / Headline',
            'skills': 'Your Skills (Comma Separated)',
            'experience_years': 'Years of Experience',
            'bio': 'Professional Bio',
        }
        widgets = {
            'headline': forms.TextInput(attrs={'placeholder': 'e.g. Fullstack Software Engineer', 'maxlength': 100}),
            'skills': forms.Textarea(attrs={'rows': 3, 'placeholder': 'e.g. Python, Django, React, PostgreSQL, Docker, AWS', 'maxlength': 500}),
            'experience_years': forms.NumberInput(attrs={'min': 0, 'max': 50, 'placeholder': 'e.g. 4'}),
            'bio': forms.Textarea(attrs={'rows': 5, 'placeholder': 'Brief summary of your expertise...', 'maxlength': 1000}),
        }

    def clean_headline(self):
        headline = self.cleaned_data.get('headline', '')
        if headline and len(headline) > 100:
            raise forms.ValidationError("Professional headline cannot exceed 100 characters.")
        return headline

    def clean_skills(self):
        skills = self.cleaned_data.get('skills', '')
        if skills and len(skills) > 500:
            raise forms.ValidationError("Skills list cannot exceed 500 characters.")
        return skills

    def clean_experience_years(self):
        exp = self.cleaned_data.get('experience_years')
        if exp is not None:
            if exp < 0 or exp > 50:
                raise forms.ValidationError("Years of experience must be between 0 and 50.")
        return exp

    def clean_bio(self):
        bio = self.cleaned_data.get('bio', '')
        if bio and len(bio) > 1000:
            raise forms.ValidationError("Professional bio cannot exceed 1000 characters.")
        return bio

class JobApplicationForm(forms.ModelForm):
    class Meta:
        model = JobApplication
        fields = ['job_title', 'company_name', 'category', 'job_description', 'location', 'salary', 'job_url', 'application_date', 'status', 'tags', 'notes']
        widgets = {
            'application_date': forms.DateInput(attrs={'type': 'date'}),
        }

class InterviewForm(forms.ModelForm):
    class Meta:
        model = Interview
        fields = ['interview_type', 'interview_date', 'meeting_link', 'interview_notes']
        widgets = {
            'interview_date': forms.DateTimeInput(attrs={'type': 'datetime-local'}),
        }
