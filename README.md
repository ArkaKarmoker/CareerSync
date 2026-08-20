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
  - [5. AI-Powered Intelligence Suite (Gemini AI)](#5-ai-powered-intelligence-suite-gemini-ai)
  - [6. Analytics Dashboard](#6-analytics-dashboard)
- [🛡️ Comprehensive Testing](#%EF%B8%8F-comprehensive-testing)
- [📸 UI Screenshots](#-ui-screenshots)
- [🛠️ Tech Stack & Dependencies](#%EF%B8%8F-tech-stack--dependencies)
- [📁 Project Directory Structure](#-project-directory-structure)
- [📊 Database Schema & Data Models](#-database-schema--data-models)
- [⚙️ Local Setup & Installation Guide](#%EF%B8%8F-local-setup--installation-guide)
- [🔑 Demo User Credentials](#-demo-user-credentials)

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

### 5. AI-Powered Intelligence Suite (Gemini AI)
- Powered by `google-generativeai` (Google Gemini models).
- **One-Click Deep Analysis**: Generates comprehensive AI insights directly from raw job descriptions:
  - **Executive Job Summary**: Quick, concise overview of the role and key duties.
  - **Required Skills**: Extracted list of core skills for candidate selection.
  - **Experience Level**: Minimum years and background needed.
  - **Key Technologies**: Parsed clean list of tools, frameworks, and programming languages.
  - **Interview Preparation Guide**: Tailored bullet points on specific technical and behavioral topics to study.
  - **🎯 AI Job Match Analysis**: Evaluates candidate profile alignment and calculates an AI Match Score (0–100%) with qualitative fit commentary.
  - **❓ AI Interview Question Generation**: Generates role-specific technical and behavioral interview questions accompanied by suggested answer hints and strategies.

### 6. Analytics Dashboard
- **Total Application Counter**: Summary count of all jobs tracked.
- **Status Metrics Bar**: Interactive breakdown by status (`Wishlist`, `Applied`, `Interview`, `Selected`, `Rejected`).
- **Recent Applications Table**: Quick view of latest applications.
- **Upcoming Interviews Widget**: Chronological listing of upcoming interview calls with formatted date & time.

---

## 🛡️ Comprehensive Testing
This project includes a highly robust, automated testing suite powered by Django's `TestCase`. 
There are currently **29 Comprehensive Test Cases** that ensure system stability across:
- **Authentication & User Flows**: Registration, Login, Logout, Profile Updates, Password Changes.
- **Application CRUD & Data Isolation**: Ensures users cannot access, edit, or delete data belonging to other users.
- **Filtering, Pagination & Sorting**: Verifies accurate URL parameter parsing and queryset filtering.
- **Interview CRUD & Isolation**: Ensures interview instances are perfectly mapped and isolated.
- **AI Integration Logic**: Mocks and verifies the Gemini AI analysis pipeline without real API limits.

Run tests using:
```bash
python manage.py test
```

---

## 📸 UI Screenshots

### Authentication & Dashboard

**Login Page**
![Login Page](screenshots/1.%20login%20page.jpeg)

**Registration Page**
![Registration Page](screenshots/2.%20registration%20page.jpeg)

**Dashboard Page**
![Dashboard Page](screenshots/3.%20dashboard%20page.jpeg)

**Profile Page**
![Profile Page](screenshots/12.%20profile%20page.jpeg)

### Job Applications

**Applications Page**
![Applications Page](screenshots/4.%20applications%20page.jpeg)

**Applications Page (With Filter)**
![Applications Page with Filter](screenshots/5.%20applications%20page%20with%20filter.jpeg)

**Add Application Page**
![Add Application Page](screenshots/6.%20add%20application%20page.jpeg)

**Application Details Page**
![Application Details Page](screenshots/7.%20application%20details%20page.jpeg)

**Edit Application Page**
![Edit Application Page](screenshots/7.%20edit%20application%20page.jpeg)

**Delete Application Page**
![Delete Application Page](screenshots/11.%20delete%20application%20page.jpeg)

### Interviews & AI

**Add Interview Page**
![Add Interview Page](screenshots/8.%20add%20interview%20page.jpeg)

**Edit Interview Page**
![Edit Interview Page](screenshots/9.%20edit%20interview%20page.jpeg)

**Delete Interview Page**
![Delete Interview Page](screenshots/10.%20delete%20interview%20page.jpeg)

### Mobile Responsiveness

<table>
  <tr>
    <td align="center"><b>Mobile Dashboard</b></td>
    <td align="center"><b>Mobile Application Details</b></td>
    <td align="center"><b>Mobile AI Insights</b></td>
  </tr>
  <tr>
    <td align="center"><img src="screenshots/13.%20mobile%20responsive%20dashboard%20page.png" alt="Mobile Dashboard" width="300"></td>
    <td align="center"><img src="screenshots/14.%20mobile%20responsive%20application%20details%20page.png" alt="Mobile Application Details" width="300"></td>
    <td align="center"><img src="screenshots/15.%20mobile%20responsive%20ai%20insights.png" alt="Mobile AI Insights" width="300"></td>
  </tr>
</table>

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
│   ├── asgi.py
│   ├── settings.py               # Settings & API configuration
│   ├── urls.py                   # Global Routing
│   └── wsgi.py
├── static/                       # Static Assets
│   ├── css/
│   │   └── style.css             # Custom modular CSS
│   ├── js/
│   │   ├── auth.js               # Auth UI logic
│   │   ├── main.js               # Core UI Interactions
│   │   └── tailwind-config.js    # Tailwind themes
│   └── favicon.svg               # Website Favicon
├── templates/                    # HTML Templates (Tailwind CSS)
│   ├── base.html                 # Responsive Navigation & Base Layout
│   └── tracker/                  # All app templates
│       ├── application_confirm_delete.html
│       ├── application_detail.html
│       ├── application_form.html
│       ├── application_list.html
│       ├── dashboard.html
│       ├── interview_confirm_delete.html
│       ├── interview_form.html
│       ├── login.html            # Login Template
│       ├── profile.html
│       └── register.html         # Registration Template
├── tracker/                      # Primary Tracker App
│   ├── migrations/               # Database Migrations
│   ├── admin.py                  # Admin Panel Configurations
│   ├── ai_utils.py               # Gemini API Integration & Parsing Engine
│   ├── apps.py
│   ├── forms.py                  # User, Application & Interview Forms
│   ├── models.py                 # JobApplication, Interview, JobAnalysis, Category
│   ├── tests.py                  # 29 Comprehensive Automated Tests
│   ├── urls.py                   # App URL Routing
│   └── views.py                  # Authentication, Application CRUD & AI Views
├── .env                          # Secret API Keys (Not committed to Git)
├── .env.sample                   # Sample Environment Variables
├── db.sqlite3                    # Local SQLite Database
├── manage.py                     # Django Command Utility
├── README.md                     # Project Documentation
├── requirements.txt              # Core Python Dependencies
└── seed_data.py                  # Database Seeding Script
```

---

## 📊 Database Schema & Data Models

1. **`UserProfile`**: One-to-one relationship with `User`, storing candidate professional title, technical skills, years of experience, and bio used for AI Job Match analysis.
2. **`Category`**: Pre-defined or custom job category taxonomy (e.g., Frontend, Backend).
3. **`JobApplication`**: Core model containing job details, company, location, salary, status, tags, and user foreign key.
4. **`Interview`**: One-to-many relationship with `JobApplication`, storing interview type, date/time, meeting link, and preparation notes.
5. **`JobAnalysis`**: One-to-one relationship with `JobApplication`, storing AI-generated insights (Summary, Skills, Experience, Tech stack, Prep guide, Match Score, Match Analysis, Generated Interview Questions).

---

## ⚙️ Local Setup & Installation Guide

Follow these simple steps to run CareerSync locally on your machine:

### 1. Clone the Repository
```bash
git clone https://github.com/ArkaKarmoker/CareerSync
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
Copy the provided `.env.sample` file to create your own `.env` file:
```bash
cp .env.sample .env
```
Update the `.env` file with your credentials:
```env
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

---

## 🔑 Demo User Credentials

If you populated the database using `python seed_data.py`, you can instantly log in using either of the following accounts:

| Role | Username | Password | Details |
| :--- | :--- | :--- | :--- |
| **Standard User** | `arka` | `password123` | Pre-populated with 32 sample jobs across multiple statuses, interviews & AI analysis |
| **Superuser / Admin** | `admin` | `admin123` | Full administrative control via Django Admin Panel ([`http://127.0.0.1:8000/admin/`](http://127.0.0.1:8000/admin/)) |

---

Developed by **[Arka Karmoker](https://github.com/ArkaKarmoker)**
