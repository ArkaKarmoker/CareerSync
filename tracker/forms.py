from django import forms
from django.contrib.auth.models import User
from .models import JobApplication, Interview

class UserRegisterForm(forms.ModelForm):
    first_name = forms.CharField(max_length=30, required=False, label="First Name")
    last_name = forms.CharField(max_length=30, required=False, label="Last Name")
    password = forms.CharField(widget=forms.PasswordInput)
    password_confirm = forms.CharField(widget=forms.PasswordInput, label="Confirm Password")

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'password']

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get("password")
        password_confirm = cleaned_data.get("password_confirm")

        if password and password_confirm and password != password_confirm:
            raise forms.ValidationError("Passwords do not match!")

class UserProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email']

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
