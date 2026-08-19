import os
import django
from datetime import datetime, timedelta
from django.utils import timezone

# Set up Django environment
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "core.settings")
django.setup()

from django.contrib.auth.models import User
from tracker.models import JobApplication, Interview, JobAnalysis

def seed():
    # Clear existing data to avoid duplicates if run multiple times
    print("Clearing existing sample data...")
    User.objects.filter(username='testuser').delete()
    
    # Create test user
    print("Creating test user...")
    user = User.objects.create_user(username='testuser', email='testuser@example.com', password='password123')
    
    # Job descriptions
    jd_frontend = """We are looking for a skilled Frontend Developer to join our team. 
    You will be responsible for building the ‘client-side’ of our web applications.
    Requirements:
    - 3+ years of experience with React, HTML, CSS, JavaScript.
    - Experience with Tailwind CSS is a plus.
    - Excellent problem-solving skills."""

    jd_backend = """Seeking a Backend Python Developer to build scalable APIs and backend services.
    Requirements:
    - 4+ years of Python and Django/FastAPI experience.
    - Strong understanding of SQL databases (PostgreSQL).
    - Experience with Docker and AWS.
    - Ability to write clean, testable code."""

    jd_fullstack = """Fullstack Software Engineer needed for a fast-paced startup.
    Requirements:
    - 2+ years of experience with Django and React.
    - Knowledge of cloud platforms.
    - Team player and good communication skills."""

    # Create Job Applications
    print("Creating job applications...")
    now = timezone.now()
    
    app1 = JobApplication.objects.create(
        user=user,
        job_title='Frontend Developer',
        company_name='TechNova Solutions',
        job_description=jd_frontend,
        location='Remote',
        salary='$90,000 - $110,000',
        job_url='https://technova.example.com/jobs/1',
        application_date=(now - timedelta(days=15)).date(),
        status='Interview',
        notes='Referred by Alex. The product looks very interesting.'
    )

    app2 = JobApplication.objects.create(
        user=user,
        job_title='Backend Engineer (Python)',
        company_name='DataFlow Inc',
        job_description=jd_backend,
        location='New York, NY',
        salary='$130,000',
        job_url='https://dataflow.example.com/careers',
        application_date=(now - timedelta(days=5)).date(),
        status='Applied',
        notes='Applied directly on their website.'
    )

    app3 = JobApplication.objects.create(
        user=user,
        job_title='Fullstack Software Engineer',
        company_name='StartupX',
        job_description=jd_fullstack,
        location='San Francisco, CA (Hybrid)',
        salary='Equity + $110,000',
        job_url='https://startupx.example.com/jobs',
        application_date=(now - timedelta(days=20)).date(),
        status='Rejected',
        notes='Rejected after the second round. They needed more DevOps experience.'
    )

    app4 = JobApplication.objects.create(
        user=user,
        job_title='Senior Django Developer',
        company_name='WebCorp',
        job_description='Looking for a senior django expert to migrate our legacy systems.',
        location='Remote',
        salary='$140,000',
        job_url='',
        application_date=None,
        status='Wishlist',
        notes='Saw this on LinkedIn, will apply this weekend after updating resume.'
    )
    
    app5 = JobApplication.objects.create(
        user=user,
        job_title='Software Engineer',
        company_name='BigTech Corp',
        job_description='Generalist software engineer role for our core product team.',
        location='Seattle, WA',
        salary='$160,000 + Bonus',
        job_url='https://bigtech.example.com/jobs',
        application_date=(now - timedelta(days=40)).date(),
        status='Selected',
        notes='Received the offer letter! Negotiating salary.'
    )

    # Create Interviews
    print("Creating interviews...")
    Interview.objects.create(
        application=app1,
        interview_date=now - timedelta(days=2),
        interview_type='HR Screening',
        meeting_link='https://zoom.us/j/123456789',
        interview_notes='HR asked about basic background and salary expectations.'
    )

    Interview.objects.create(
        application=app1,
        interview_date=now + timedelta(days=3),
        interview_type='Technical Round',
        meeting_link='https://meet.google.com/abc-defg-hij',
        interview_notes='Will be a live coding round on React.'
    )

    Interview.objects.create(
        application=app3,
        interview_date=now - timedelta(days=10),
        interview_type='Technical Round',
        meeting_link='',
        interview_notes='Failed to answer the system design question well.'
    )

    Interview.objects.create(
        application=app5,
        interview_date=now - timedelta(days=15),
        interview_type='Final Round',
        meeting_link='',
        interview_notes='Met with the VP of Engineering. Went great.'
    )

    # Create Job Analysis
    print("Creating job analysis samples...")
    JobAnalysis.objects.create(
        application=app1,
        job_summary='A frontend developer role focused on building client-side web applications using modern web technologies.',
        required_skills='React, HTML, CSS, JavaScript, Tailwind CSS',
        required_experience='3+ years in frontend development',
        important_technologies='React, Tailwind CSS',
        interview_preparation_suggestions='- Review React hooks and state management.\n- Practice building responsive layouts with Tailwind.\n- Be prepared to discuss past projects.'
    )

    print("Database successfully seeded!")
    print("You can log in with:\nUsername: testuser\nPassword: password123")

if __name__ == '__main__':
    seed()
