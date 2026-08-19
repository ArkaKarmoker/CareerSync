from django.db import models
from django.contrib.auth.models import User

class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Categories'

class JobApplication(models.Model):
    STATUS_CHOICES = [
        ('Wishlist', 'Wishlist'),
        ('Applied', 'Applied'),
        ('Screening', 'Screening'),
        ('Interview', 'Interview'),
        ('Selected', 'Selected'),
        ('Rejected', 'Rejected'),
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='applications')
    job_title = models.CharField(max_length=255)
    company_name = models.CharField(max_length=255)
    job_description = models.TextField(blank=True, null=True)
    location = models.CharField(max_length=255, blank=True, null=True)
    salary = models.CharField(max_length=100, blank=True, null=True)
    job_url = models.URLField(blank=True, null=True)
    application_date = models.DateField(blank=True, null=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='Wishlist')
    notes = models.TextField(blank=True, null=True)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, blank=True, related_name='applications')
    tags = models.CharField(max_length=255, blank=True, null=True, help_text="Comma-separated tags")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.job_title} at {self.company_name}"

class Interview(models.Model):
    application = models.ForeignKey(JobApplication, on_delete=models.CASCADE, related_name='interviews')
    interview_date = models.DateTimeField()
    interview_type = models.CharField(max_length=100)
    meeting_link = models.URLField(blank=True, null=True)
    interview_notes = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.interview_type} for {self.application.company_name}"

class JobAnalysis(models.Model):
    application = models.OneToOneField(JobApplication, on_delete=models.CASCADE, related_name='analysis')
    job_summary = models.TextField(blank=True, null=True)
    required_skills = models.TextField(blank=True, null=True)
    required_experience = models.TextField(blank=True, null=True)
    important_technologies = models.TextField(blank=True, null=True)
    interview_preparation_suggestions = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Analysis for {self.application.job_title}"
