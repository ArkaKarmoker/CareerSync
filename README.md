# 🚀 CareerSync - AI-Powered Job Application Tracker

[![Django](https://img.shields.io/badge/Django-6.1-092E20?style=for-the-badge&logo=django&logoColor=white)](https://www.djangoproject.com/)
[![Python](https://img.shields.io/badge/Python-3.10+-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)
[![Tailwind CSS](https://img.shields.io/badge/Tailwind_CSS-3.0+-06B6D4?style=for-the-badge&logo=tailwindcss&logoColor=white)](https://tailwindcss.com/)
[![Google Gemini AI](https://img.shields.io/badge/Google_Gemini-AI_Analysis-8E75B2?style=for-the-badge&logo=google&logoColor=white)](https://ai.google.dev/)

**CareerSync** is a modern, full-stack Django web application designed to help job seekers seamlessly track, organize, and manage their job applications and interview schedules from a single, beautifully crafted dashboard. Powered by **Google Gemini AI**, CareerSync automatically analyzes complex job descriptions to extract required skills, experience levels, key technologies, and custom interview preparation strategies.

This project was built as an assignment for **Django Batch 10 - Module 20**, fulfilling all core and optional requirements while adding extra robust features like extensive test coverage and mobile responsiveness.

---

## 📌 Table of Contents

- [Features](#-features)
  - [1. User Authentication & Profile Management](#1-user-authentication--profile-management)
  - [2. Job Application Lifecycle (CRUD)](#2-job-application-lifecycle-crud)
  - [3. Search, Filter & Tagging System](#3-search-filter--tagging-system)
  - [4. Interview Management System](#4-interview-management-system)
  - [5. AI Job Description Analyzer (Gemini AI)](#5-ai-job-description-analyzer-gemini-ai)
  - [6. Analytics Dashboard](#6-analytics-dashboard)
- [🛡️ Comprehensive Testing](#%EF%B8%8F-comprehensive-testing)
- [📸 UI Screenshots](#-ui-screenshots)
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
- **Full CRUD Capabilities**: Add, view, edit, and delete job applications easily.
- **Complete Application Attributes**:
  - **Job Title** & **Company Name**
  - **Category** (Frontend, Backend, Fullstack, DevOps, Mobile, etc.)
  - **Job Description** 
  - **Location** & **Salary Range**
  - **Job URL** (Direct link to posting)
  - **Application Date** & **Tags** (Comma separated)
  - **Status Pipeline**: `Wishlist` ➔ `Applied` ➔ `Screening` ➔ `Interview` ➔ `Selected` / `Rejected`
  - **Notes**: Personal application notes.

### 3. Search, Filter & Tagging System
- **Real-time Search**: Search applications by Job Title, Company Name, or Tags.
- **Multi-criteria Filtering**: Filter by Application Status, Job Category, and Location.
- **Sorting & Pagination**: Sort by date, role, company, or status. Pagination applied (5 items per page) for optimal performance.

### 4. Interview Management System
- **Schedule Interviews**: Track upcoming interview rounds for any job application. Full CRUD support for Interviews.
- **Interview Types & Dynamic Badging**: Easily log HR Screenings, Technical Rounds, and Final Interviews.
- **Direct Video Join Link**: Quick access button to launch video calls directly.
- **Notes & Logs**: Keep track of questions asked, preparation notes, and interviewer details.

### 5. AI Job Description Analyzer (Gemini AI)
- Powered by `google-generativeai` (Gemini model).
- **One-Click Deep Analysis**: Generates AI insights directly from raw job descriptions:
  - **Executive Job Summary**: Quick overview of the role.
  - **Required Skills**: Core skills required for candidate selection.
  - **Experience Level**: Minimum years and expertise needed.
  - **Key Technologies**: Parsed clean list of tools, frameworks, and languages.
  - **Interview Preparation Guide**: Tailored bullet points on topics to study for the interview.

### 6. Analytics Dashboard
- **Total Application Counter**: Summary count of all jobs tracked.
- **Status Metrics Bar**: Interactive breakdown by status (`Wishlist`, `Applied`, `Interview`, `Selected`, `Rejected`).
- **Recent Applications Table**: Quick view of latest applications.
- **Upcoming Interviews Widget**: Chronological listing of upcoming interview calls with formatted date & time.

---

## 🛡️ Comprehensive Testing
This project includes a highly robust, automated testing suite powered by Django's `TestCase`. 
There are currently **25 Comprehensive Test Cases** that ensure system stability across:
- **Authentication & User Flows**: Registration, Login, Logout, Profile Updates, Password Changes.
- **Application CRUD & Data Isolation**: Ensures users cannot access, edit, or delete data belonging to other users.
- **Filtering, Pagination & Sorting**: Verifies accurate URL parameter parsing and queryset filtering.
- **Interview CRUD & Isolation**: Ensures interview instances are perfectly mapped and isolated.
- **AI Integration Logic**: Mocks and verifies the Gemini AI analysis pipeline without real API limits.

Run tests using:
```bash
python manage.py test tracker.tests
```

---

## 📸 UI Screenshots

### Authentication & Dashboard

**1. Login Page**
![Login Page](screenshots/1.%20login%20page.jpeg)

**2. Registration Page**
![Registration Page](screenshots/2.%20registration%20page.jpeg)

**3. Dashboard Page**
![Dashboard Page](screenshots/3.%20dashboard%20page.jpeg)

**12. Profile Page**
![Profile Page](screenshots/12.%20profile%20page.jpeg)

### Job Applications

**4. Applications Page**
![Applications Page](screenshots/4.%20applications%20page.jpeg)

**5. Applications Page (With Filter)**
![Applications Page with Filter](screenshots/5.%20applications%20page%20with%20filter.jpeg)

**6. Add Application Page**
![Add Application Page](screenshots/6.%20add%20application%20page.jpeg)

**7. Application Details Page**
![Application Details Page](screenshots/7.%20application%20details%20page.jpeg)

**7. Edit Application Page**
![Edit Application Page](screenshots/7.%20edit%20application%20page.jpeg)

**11. Delete Application Page**
![Delete Application Page](screenshots/11.%20delete%20application%20page.jpeg)

### Interviews & AI

**8. Add Interview Page**
![Add Interview Page](screenshots/8.%20add%20interview%20page.jpeg)

**9. Edit Interview Page**
![Edit Interview Page](screenshots/9.%20edit%20interview%20page.jpeg)

**10. Delete Interview Page**
![Delete Interview Page](screenshots/10.%20delete%20interview%20page.jpeg)

### Mobile Responsiveness

**13. Mobile Dashboard**
![Mobile Dashboard](screenshots/13.%20mobile%20responsive%20dashboard%20page.png)

**14. Mobile Application Details**
![Mobile Application Details](screenshots/14.%20mobile%20responsive%20application%20details%20page.png)

**15. Mobile AI Insights**
![Mobile AI Insights](screenshots/15.%20mobile%20responsive%20ai%20insights.png)


---

## 🛠️ Tech Stack & Dependencies

- **Backend Framework**: Django 6.1 (Python 3.10+)
- **AI Integration**: Google Gemini API (`google-generativeai`)
- **Frontend Stack**: HTML5, Vanilla JavaScript, Tailwind CSS 
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
├── tracker/                      # Primary Tracker App
│   ├── models.py                 # JobApplication, Interview, JobAnalysis, Category
│   ├── views.py                  # Authentication, Application CRUD & AI Views
│   ├── forms.py                  # User, Application & Interview Forms
│   ├── tests.py                  # 25 Comprehensive Automated Tests
│   ├── ai_utils.py               # Gemini API Integration & Parsing Engine
│   ├── urls.py                   # App URL Routing
├── static/                       # Static Assets
│   ├── css/style.css             # Custom modular CSS
│   ├── js/main.js                # Core UI Interactions
│   ├── js/auth.js                # Auth UI logic
│   └── js/tailwind-config.js     # Tailwind themes
├── templates/                    # HTML Templates (Tailwind CSS)
│   ├── base.html                 # Responsive Navigation & Base Layout
│   ├── registration/             # Login & Registration Templates
│   └── tracker/                  # Dashboard, CRUD forms, and detail views
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
cd CareerSync
```

### 2. Create and Activate a Virtual Environment
- **Windows (PowerShell)**:
  ```powershell
  python -m venv venv
  .\venv\Scripts\Activate
  ```
- **macOS / Linux**:
  ```bash
  python3 -m venv venv
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
