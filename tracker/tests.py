from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth.models import User
from django.utils import timezone
from unittest.mock import patch
from datetime import timedelta

from tracker.models import Category, JobApplication, Interview, JobAnalysis
from tracker.forms import UserRegisterForm, JobApplicationForm, InterviewForm, UserProfileUpdateForm

class UserModelTests(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            username='testuser',
            email='test@example.com',
            password='password123',
            first_name='Test',
            last_name='User'
        )

    def test_user_creation(self):
        self.assertEqual(self.user.username, 'testuser')
        self.assertEqual(self.user.email, 'test@example.com')
        self.assertTrue(self.user.check_password('password123'))

class TrackerModelsTests(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='john', password='password123')
        self.category = Category.objects.create(name='Backend Development')
        self.app = JobApplication.objects.create(
            user=self.user,
            job_title='Software Engineer',
            company_name='TechCorp',
            job_description='Python & Django backend developer needed.',
            location='Remote',
            salary='$100,000',
            status='Applied',
            category=self.category,
            tags='python, django'
        )

    def test_category_str(self):
        self.assertEqual(str(self.category), 'Backend Development')

    def test_job_application_str(self):
        self.assertEqual(str(self.app), 'Software Engineer at TechCorp')

    def test_interview_str(self):
        interview = Interview.objects.create(
            application=self.app,
            interview_date=timezone.now() + timedelta(days=2),
            interview_type='Technical Round',
            meeting_link='https://meet.example.com/123'
        )
        self.assertEqual(str(interview), 'Technical Round for TechCorp')

    def test_job_analysis_str(self):
        analysis = JobAnalysis.objects.create(
            application=self.app,
            job_summary='Backend role focusing on API design.',
            required_skills='Python, Django',
            required_experience='3 years',
            important_technologies='PostgreSQL, Redis'
        )
        self.assertEqual(str(analysis), 'Analysis for Software Engineer')

class AuthenticationViewsTests(TestCase):
    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user(
            username='existinguser',
            email='existing@example.com',
            password='password123',
            first_name='Existing',
            last_name='User'
        )

    def test_register_view_get(self):
        response = self.client.get(reverse('register'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'tracker/register.html')
        self.assertIsInstance(response.context['form'], UserRegisterForm)

    def test_register_view_post_success(self):
        data = {
            'username': 'newuser',
            'email': 'new@example.com',
            'first_name': 'New',
            'last_name': 'Person',
            'password': 'Password123!',
            'password_confirm': 'Password123!'
        }
        response = self.client.post(reverse('register'), data)
        self.assertRedirects(response, reverse('dashboard'))
        self.assertTrue(User.objects.filter(username='newuser').exists())

    def test_register_view_post_password_mismatch(self):
        data = {
            'username': 'newuser2',
            'email': 'new2@example.com',
            'first_name': 'New',
            'last_name': 'Person',
            'password': 'Password123!',
            'password_confirm': 'DifferentPassword!'
        }
        response = self.client.post(reverse('register'), data)
        self.assertEqual(response.status_code, 200)
        self.assertFalse(User.objects.filter(username='newuser2').exists())

    def test_login_and_logout(self):
        # Login
        login_response = self.client.post(reverse('login'), {
            'username': 'existinguser',
            'password': 'password123'
        })
        self.assertRedirects(login_response, reverse('dashboard'))

        # Logout
        logout_response = self.client.post(reverse('logout'))
        self.assertEqual(logout_response.status_code, 302)

    def test_profile_update_and_password_change(self):
        self.client.login(username='existinguser', password='password123')

        # Update profile info
        profile_data = {
            'update_profile': '1',
            'username': 'existinguser',
            'first_name': 'UpdatedFirst',
            'last_name': 'UpdatedLast',
            'email': 'updated@example.com'
        }
        response = self.client.post(reverse('profile'), profile_data)
        self.assertRedirects(response, reverse('profile'))
        self.user.refresh_from_db()
        self.assertEqual(self.user.first_name, 'UpdatedFirst')
        self.assertEqual(self.user.email, 'updated@example.com')

        # Change password
        pass_data = {
            'change_password': '1',
            'old_password': 'password123',
            'new_password1': 'NewSecurePassword123!',
            'new_password2': 'NewSecurePassword123!'
        }
        pass_response = self.client.post(reverse('profile'), pass_data)
        self.assertRedirects(pass_response, reverse('profile'))
        self.user.refresh_from_db()
        self.assertTrue(self.user.check_password('NewSecurePassword123!'))

class ApplicationCRUDTests(TestCase):
    def setUp(self):
        self.client = Client()
        self.user1 = User.objects.create_user(username='user1', password='password123')
        self.user2 = User.objects.create_user(username='user2', password='password123')
        self.category = Category.objects.create(name='Fullstack')

        self.app1 = JobApplication.objects.create(
            user=self.user1,
            job_title='Frontend Developer',
            company_name='Meta',
            location='Remote',
            status='Applied',
            category=self.category
        )

    def test_unauthenticated_access_redirection(self):
        protected_urls = [
            reverse('dashboard'),
            reverse('application_list'),
            reverse('application_create'),
            reverse('application_detail', kwargs={'pk': self.app1.pk}),
            reverse('application_update', kwargs={'pk': self.app1.pk}),
            reverse('application_delete', kwargs={'pk': self.app1.pk}),
            reverse('interview_create', kwargs={'application_id': self.app1.pk}),
            reverse('analyze_job', kwargs={'application_id': self.app1.pk}),
            reverse('profile'),
        ]
        for url in protected_urls:
            response = self.client.get(url)
            self.assertEqual(response.status_code, 302, f"URL {url} did not redirect unauthenticated user.")

    def test_create_application(self):
        self.client.login(username='user1', password='password123')
        data = {
            'job_title': 'Backend Developer',
            'company_name': 'Google',
            'job_description': 'Build high scale microservices.',
            'location': 'Mountain View, CA',
            'salary': '$150,000',
            'job_url': 'https://careers.google.com/jobs/123',
            'application_date': '2026-08-15',
            'status': 'Applied',
            'category': self.category.id,
            'tags': 'python, microservices'
        }
        response = self.client.post(reverse('application_create'), data)
        self.assertRedirects(response, reverse('application_list'))
        self.assertTrue(JobApplication.objects.filter(company_name='Google', user=self.user1).exists())

    def test_user_data_isolation(self):
        # Create app for user2
        app2 = JobApplication.objects.create(
            user=self.user2,
            job_title='DevOps Lead',
            company_name='Amazon',
            status='Interview'
        )

        self.client.login(username='user1', password='password123')

        # Application list should only contain app1, not app2
        response = self.client.get(reverse('application_list'))
        self.assertContains(response, 'Meta')
        self.assertNotContains(response, 'Amazon')

        # Accessing user2's application detail should return 404
        detail_response = self.client.get(reverse('application_detail', kwargs={'pk': app2.pk}))
        self.assertEqual(detail_response.status_code, 404)

        # Accessing user2's application edit should return 404
        edit_response = self.client.get(reverse('application_update', kwargs={'pk': app2.pk}))
        self.assertEqual(edit_response.status_code, 404)

    def test_update_application(self):
        self.client.login(username='user1', password='password123')
        update_data = {
            'job_title': 'Senior Frontend Developer',
            'company_name': 'Meta',
            'location': 'Menlo Park, CA',
            'status': 'Interview',
            'category': self.category.id
        }
        response = self.client.post(reverse('application_update', kwargs={'pk': self.app1.pk}), update_data)
        self.assertRedirects(response, reverse('application_detail', kwargs={'pk': self.app1.pk}))
        self.app1.refresh_from_db()
        self.assertEqual(self.app1.job_title, 'Senior Frontend Developer')
        self.assertEqual(self.app1.status, 'Interview')

    def test_delete_application(self):
        self.client.login(username='user1', password='password123')
        response = self.client.post(reverse('application_delete', kwargs={'pk': self.app1.pk}))
        self.assertRedirects(response, reverse('application_list'))
        self.assertFalse(JobApplication.objects.filter(pk=self.app1.pk).exists())

class SearchFilterSortPaginationTests(TestCase):
    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user(username='searchuser', password='password123')
        self.cat1 = Category.objects.create(name='AI')
        self.cat2 = Category.objects.create(name='Mobile')

        # Create 12 applications for pagination & filter tests
        for i in range(1, 13):
            JobApplication.objects.create(
                user=self.user,
                job_title=f'Role {i}',
                company_name=f'Company {i}',
                location='San Francisco' if i % 2 == 0 else 'Remote',
                status='Applied' if i <= 6 else 'Interview',
                category=self.cat1 if i <= 6 else self.cat2,
                tags='ai, ml' if i % 2 == 0 else 'react, mobile'
            )

        self.client.login(username='searchuser', password='password123')

    def test_pagination(self):
        response = self.client.get(reverse('application_list'))
        self.assertEqual(response.status_code, 200)
        self.assertTrue(response.context['is_paginated'])
        self.assertEqual(len(response.context['applications']), 5) # 5 per page

        # Page 2
        page2_response = self.client.get(reverse('application_list') + '?page=2')
        self.assertEqual(len(page2_response.context['applications']), 5)

        # Page 3
        page3_response = self.client.get(reverse('application_list') + '?page=3')
        self.assertEqual(len(page3_response.context['applications']), 2)

    def test_search_filter(self):
        # Search query
        response = self.client.get(reverse('application_list') + '?q=Company 1')
        self.assertEqual(response.status_code, 200)
        # Should match Company 1, Company 10, Company 11, Company 12
        for app in response.context['applications']:
            self.assertIn('Company 1', app.company_name)

        # Filter by status
        status_response = self.client.get(reverse('application_list') + '?status=Interview')
        self.assertEqual(status_response.context['paginator'].count, 6)

        # Filter by category
        cat_response = self.client.get(reverse('application_list') + f'?category={self.cat1.id}')
        self.assertEqual(cat_response.context['paginator'].count, 6)

    def test_sorting(self):
        # Sort by company ascending
        sort_company = self.client.get(reverse('application_list') + '?sort=company')
        companies = [app.company_name for app in sort_company.context['applications']]
        self.assertEqual(companies, sorted(companies))

        # Sort by role descending
        sort_role = self.client.get(reverse('application_list') + '?sort=-role')
        roles = [app.job_title for app in sort_role.context['applications']]
        self.assertEqual(roles, sorted(roles, reverse=True))

class InterviewAndAITests(TestCase):
    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user(username='aiuser', password='password123')
        self.app = JobApplication.objects.create(
            user=self.user,
            job_title='Machine Learning Engineer',
            company_name='OpenAI',
            job_description='Train large language models.',
            status='Applied'
        )
        self.client.login(username='aiuser', password='password123')

    def test_create_interview(self):
        interview_data = {
            'interview_date': '2026-09-01T10:00',
            'interview_type': 'Technical Round',
            'meeting_link': 'https://zoom.us/j/123456789',
            'interview_notes': 'Prepare transformer architecture questions.'
        }
        response = self.client.post(reverse('interview_create', kwargs={'application_id': self.app.pk}), interview_data)
        self.assertRedirects(response, reverse('application_detail', kwargs={'pk': self.app.pk}))
        self.assertTrue(Interview.objects.filter(application=self.app, interview_type='Technical Round').exists())

    def test_update_interview(self):
        interview = Interview.objects.create(
            application=self.app,
            interview_date=timezone.now() + timedelta(days=1),
            interview_type='HR Screening'
        )
        update_data = {
            'interview_date': '2026-09-02T11:00',
            'interview_type': 'Updated HR Screening',
            'meeting_link': 'https://meet.google.com/xyz',
            'interview_notes': 'Updated notes'
        }
        response = self.client.post(reverse('interview_update', kwargs={'pk': interview.pk}), update_data)
        self.assertRedirects(response, reverse('application_detail', kwargs={'pk': self.app.pk}))
        interview.refresh_from_db()
        self.assertEqual(interview.interview_type, 'Updated HR Screening')
        self.assertEqual(interview.meeting_link, 'https://meet.google.com/xyz')

    def test_delete_interview(self):
        interview = Interview.objects.create(
            application=self.app,
            interview_date=timezone.now() + timedelta(days=1),
            interview_type='HR Screening'
        )
        response = self.client.post(reverse('interview_delete', kwargs={'pk': interview.pk}))
        self.assertRedirects(response, reverse('application_detail', kwargs={'pk': self.app.pk}))
        self.assertFalse(Interview.objects.filter(pk=interview.pk).exists())

    def test_interview_data_isolation(self):
        # Create another user and app
        other_user = User.objects.create_user(username='other', password='password123')
        other_app = JobApplication.objects.create(
            user=other_user, job_title='Role', company_name='Company', status='Applied'
        )
        other_interview = Interview.objects.create(
            application=other_app,
            interview_date=timezone.now() + timedelta(days=1),
            interview_type='Other HR Screening'
        )
        
        # Current user (aiuser) tries to edit other_user's interview
        response = self.client.get(reverse('interview_update', kwargs={'pk': other_interview.pk}))
        self.assertEqual(response.status_code, 404)
        
        # Current user tries to delete other_user's interview
        response = self.client.post(reverse('interview_delete', kwargs={'pk': other_interview.pk}))
        self.assertEqual(response.status_code, 404)

    def test_ai_analysis_missing_description(self):
        no_desc_app = JobApplication.objects.create(
            user=self.user,
            job_title='Data Analyst',
            company_name='StartupX',
            job_description=''
        )
        response = self.client.get(reverse('analyze_job', kwargs={'application_id': no_desc_app.pk}))
        self.assertRedirects(response, reverse('application_detail', kwargs={'pk': no_desc_app.pk}))
        self.assertFalse(JobAnalysis.objects.filter(application=no_desc_app).exists())

    @patch('tracker.views.generate_job_analysis')
    def test_ai_analysis_success(self, mock_ai):
        mock_ai.return_value = {
            'job_summary': 'Train and deploy generative AI models.',
            'required_skills': ['PyTorch', 'Transformers', 'CUDA'],
            'required_experience': '5+ years in ML',
            'important_technologies': ['Python', 'PyTorch', 'vLLM'],
            'interview_preparation_suggestions': ['Review attention mechanisms', 'System design for LLMs']
        }
        response = self.client.get(reverse('analyze_job', kwargs={'application_id': self.app.pk}))
        self.assertRedirects(response, reverse('application_detail', kwargs={'pk': self.app.pk}) + '?ai=1')
        self.assertTrue(JobAnalysis.objects.filter(application=self.app).exists())
        analysis = JobAnalysis.objects.get(application=self.app)
        self.assertEqual(analysis.job_summary, 'Train and deploy generative AI models.')
        self.assertIn('PyTorch', analysis.required_skills)

class DashboardViewTests(TestCase):
    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user(username='dashuser', password='password123')
        self.app1 = JobApplication.objects.create(user=self.user, job_title='Role 1', company_name='Co 1', status='Applied')
        self.app2 = JobApplication.objects.create(user=self.user, job_title='Role 2', company_name='Co 2', status='Interview')
        Interview.objects.create(
            application=self.app2,
            interview_date=timezone.now() + timedelta(days=1),
            interview_type='HR Screening'
        )
        self.client.login(username='dashuser', password='password123')

    def test_dashboard_context(self):
        response = self.client.get(reverse('dashboard'))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.context['total_apps'], 2)
        self.assertEqual(len(response.context['upcoming_interviews']), 1)
