from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    # Auth
    path('register/', views.register, name='register'),
    path('login/', auth_views.LoginView.as_view(template_name='tracker/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('profile/', views.profile, name='profile'),

    # Dashboard
    path('', views.dashboard, name='dashboard'),

    # Applications
    path('applications/', views.ApplicationListView.as_view(), name='application_list'),
    path('applications/new/', views.ApplicationCreateView.as_view(), name='application_create'),
    path('applications/<int:pk>/', views.ApplicationDetailView.as_view(), name='application_detail'),
    path('applications/<int:pk>/edit/', views.ApplicationUpdateView.as_view(), name='application_update'),
    path('applications/<int:pk>/delete/', views.ApplicationDeleteView.as_view(), name='application_delete'),

    # Interviews
    path('applications/<int:application_id>/interviews/new/', views.InterviewCreateView.as_view(), name='interview_create'),
    path('interviews/<int:pk>/edit/', views.InterviewUpdateView.as_view(), name='interview_update'),
    path('interviews/<int:pk>/delete/', views.InterviewDeleteView.as_view(), name='interview_delete'),

    # AI Analysis
    path('applications/<int:application_id>/analyze/', views.analyze_job, name='analyze_job'),
]
