# 🚀 CareerSync - AI-Powered Job Application Tracker

[![Django](https://img.shields.io/badge/Django-6.1-092E20?style=for-the-badge&logo=django&logoColor=white)](https://www.djangoproject.com/)
[![Python](https://img.shields.io/badge/Python-3.10+-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)
[![Tailwind CSS](https://img.shields.io/badge/Tailwind_CSS-3.0+-06B6D4?style=for-the-badge&logo=tailwindcss&logoColor=white)](https://tailwindcss.com/)
[![Google Gemini AI](https://img.shields.io/badge/Google_Gemini-AI_Analysis-8E75B2?style=for-the-badge&logo=google&logoColor=white)](https://ai.google.dev/)

**CareerSync** is a modern, full-stack Django web application designed to help job seekers seamlessly track, organize, and manage their job applications and interview schedules from a single, beautifully crafted dashboard. Powered by **Google Gemini AI**, CareerSync automatically analyzes complex job descriptions to extract required skills, experience levels, key technologies, and custom interview preparation strategies.

---

## 📌 Table of Contents

- [Features](#-features)
  - [1. User Authentication & Profile Management](#1-user-authentication--profile-management)
  - [2. Job Application Lifecycle (CRUD)](#2-job-application-lifecycle-crud)
  - [3. Search, Filter & Tagging System](#3-search-filter--tagging-system)
  - [4. Interview Management System](#4-interview-management-system)
  - [5. AI Job Description Analyzer (Gemini AI)](#5-ai-job-description-analyzer-gemini-ai)
  - [6. Analytics Dashboard](#6-analytics-dashboard)
- [🛠️ Tech Stack & Dependencies](#%EF%B8%8F-tech-stack--dependencies)
- [📁 Project Directory Structure](#-project-directory-structure)
- [📊 Database Schema & Data Models](#-database-schema--data-models)
- [⚙️ Local Setup & Installation Guide](#%EF%B8%8F-local-setup--installation-guide)

---

## ✨ Features

### 1. User Authentication & Profile Management
- **Registration & Login**: Secure account creation and session authentication.
- **User Isolation**: Each user can only view, manage, and edit their own applications and interviews.
- **Profile & Security**: User profile management with password update, password validation error alerts, and password visibility toggles.

### 2. Job Application Lifecycle (CRUD)
- **Full CRUD Capabilities**: Add, view, edit, and delete job applications.
- **Complete Application Attributes**:
  - **Job Title** & **Company Name**
  - **Category** (Frontend, Backend, Fullstack, DevOps, Mobile, etc.)
  - **Job Description** (Single line expandable)
  - **Location** & **Salary Range**
  - **Job URL** (Direct link to posting)
  - **Application Date** & **Tags** (Comma separated)
  - **Status Pipeline**: `Wishlist` ➔ `Applied` ➔ `Screening` ➔ `Interview` ➔ `Selected` / `Rejected`
  - **Notes**: Personal application notes.

### 3. Search, Filter & Tagging System
- **Real-time Search**: Search applications by Job Title or Company Name.
- **Multi-criteria Filtering**: Filter by Application Status, Job Category, and Location.
- **Structured Layout**: Grid filter bar with an explicit **Apply Filter** action.

### 4. Interview Management System
- **Schedule Interviews**: Track upcoming interview rounds for any job application.
- **Interview Types & Dynamic Badging**:
  - `HR Screening` (Fuchsia Badge)
  - `Technical Round` (Blue Badge)
  - `Final Round` (Emerald Badge)
  - `Culture Fit / Behavioral` (Amber Badge)
- **Direct Video Join Link**: Quick access button styled in Zoom/Meet blue (`bg-blue-600`) to launch video calls directly.
- **Notes & Logs**: Keep track of questions asked, preparation notes, and interviewer details.

### 5. AI Job Description Analyzer (Gemini AI)
- Powered by `google-generativeai` (Gemini model).
- **One-Click Deep Analysis**: Generates AI insights directly from raw job descriptions:
  - **Executive Job Summary**: Quick overview of the role.
  - **Required Skills**: Core skills required for candidate selection.
  - **Experience Level**: Minimum years and expertise needed.
  - **Key Technologies**: Parsed clean list of tools, frameworks, and languages.
  - **Interview Preparation Guide**: Tailored bullet points on topics to study for the interview.
- **Smart UX Anchor Scrolling**: Automatically refocuses the user directly on the **AI Insights** section upon analysis regeneration without jumping to the top of the page.

### 6. Analytics Dashboard
- **Total Application Counter**: Summary count of all jobs tracked.
- **Status Metrics Bar**: Interactive breakdown by status (`Wishlist`, `Applied`, `Interview`, `Selected`, `Rejected`).
- **Recent Applications Table**: Quick view of latest applications.
- **Upcoming Interviews Widget**: Chronological listing of upcoming interview calls with formatted date & time.

---

## 🛠️ Tech Stack & Dependencies

- **Backend Framework**: Django 6.1 (Python 3.10+)
- **AI Integration**: Google Gemini API (`google-generativeai`)
- **Frontend Stack**: HTML5, Vanilla JavaScript, Tailwind CSS (via CDN)
- **Icons & Fonts**: FontAwesome 6, Google Fonts (`Outfit`)
- **Environment Management**: `python-dotenv`
- **Database**: SQLite3

### Top-Level Dependencies (`requirements.txt`)
```text
Django==6.1
google-generativeai==0.8.6
python-dotenv==1.2.3
```

---

## 📁 Project Directory Structure

```text
CareerSync/
├── core/                         # Django Project Core Configuration
│   ├── settings.py               # Settings & API configuration
│   ├── urls.py                   # Global Routing
│   ├── wsgi.py / asgi.py
├── tracker/                      # Primary Tracker App
│   ├── models.py                 # JobApplication, Interview, JobAnalysis, Category
│   ├── views.py                  # Authentication, Application CRUD & AI Views
│   ├── forms.py                  # User, Application & Interview Forms
│   ├── ai_utils.py               # Gemini API Integration & Parsing Engine
│   ├── urls.py                   # App URL Routing
│   └── admin.py                  # Admin Panel Configurations
├── templates/                    # HTML Templates (Tailwind CSS)
│   ├── base.html                 # Navigation & Base Layout
│   ├── registration/             # Login & Registration Templates
│   └── tracker/
│       ├── dashboard.html        # Main Dashboard & Widgets
│       ├── application_list.html # Filterable Applications Table
│       ├── application_detail.html# Detail View & AI Insights
│       ├── application_form.html # Create / Edit Application Form
│       ├── interview_form.html   # Create / Edit Interview Form
│       └── profile.html          # Profile & Password Update Page
├── .env                          # Secret API Keys (Not committed to Git)
├── seed_data.py                  # Database Seeding Script
├── manage.py                     # Django Command Utility
└── requirements.txt              # Core Python Dependencies
```

---

## 📊 Database Schema & Data Models

1. **`Category`**: Pre-defined or custom job category taxonomy (e.g., Frontend, Backend).
2. **`JobApplication`**: Core model containing job details, company, location, salary, status, tags, and user foreign key.
3. **`Interview`**: One-to-many relationship with `JobApplication`, storing interview type, date/time, meeting link, and preparation notes.
4. **`JobAnalysis`**: One-to-one relationship with `JobApplication`, storing AI-generated insights (Summary, Skills, Experience, Tech stack, Prep guide).

---

## ⚙️ Local Setup & Installation Guide

Follow these simple steps to run CareerSync locally on your machine:

### 1. Clone the Repository
```bash
git clone <YOUR_GITHUB_REPOSITORY_URL>
```
```bash
cd CareerSync
```

### 2. Create and Activate a Virtual Environment
- **Windows (PowerShell)**:
  ```powershell
  python -m venv venv
  ```
  ```powershell
  .\venv\Scripts\Activate
  ```
- **macOS / Linux**:
  ```bash
  python3 -m venv venv
  ```
  ```bash
  source venv/bin/activate
  ```

### 3. Install Requirements
```bash
pip install -r requirements.txt
```

### 4. Configure Environment Variables (`.env`)
Create a `.env` file in the root directory of the project:
```env
SECRET_KEY=django-insecure-your-secret-key-here
GEMINI_API_KEY=your_google_gemini_api_key_here
```
*(Get a free Gemini API key from [Google AI Studio](https://aistudio.google.com/))*

### 5. Run Database Migrations
```bash
python manage.py migrate
```

### 6. (Optional) Seed Demo Data
To populate the app with sample job applications, interviews, and categories:
```bash
python seed_data.py
```

### 7. Start the Development Server
```bash
python manage.py runserver
```

Open your browser and navigate to: **`http://127.0.0.1:8000/`**



Developed by **Arka Karmoker**
