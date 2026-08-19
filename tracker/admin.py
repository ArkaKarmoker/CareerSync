from django.contrib import admin
from .models import JobApplication, Interview, JobAnalysis, Category

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)

@admin.register(JobApplication)
class JobApplicationAdmin(admin.ModelAdmin):
    list_display = ('job_title', 'company_name', 'status', 'category', 'application_date', 'user')
    list_filter = ('status', 'application_date')
    search_fields = ('job_title', 'company_name')

@admin.register(Interview)
class InterviewAdmin(admin.ModelAdmin):
    list_display = ('application', 'interview_type', 'interview_date')

@admin.register(JobAnalysis)
class JobAnalysisAdmin(admin.ModelAdmin):
    list_display = ('application', 'created_at')
