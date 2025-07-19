# Naukri Clone Project

A full-featured job portal built with Django, inspired by Naukri and Glassdoor. This project supports both **Jobseekers** and **Employers** with a modern, user-friendly interface and robust backend.

---
##  Features

### For Jobseekers

- **Registration & Login:** Secure sign-up and login with email, password, and mobile verification.
- **Profile Management:** Add/update full name, location, experience, skills, and upload resume.
- **Job Search:** Search jobs by title, company, or location with live filtering.
- **Apply to Jobs:** One-click application to jobs, with tracking of applied jobs.
- **Save/Like/Dislike Jobs:** Save jobs for later, like jobs for quick access, and dislike jobs to hide them.
- **Company Exploration:** Browse all registered companies, view their profiles, and follow companies.
- **Company Reviews:** Write, edit, or delete reviews for companies, including star ratings and comments.
- **Dashboard:** View stats for saved and applied jobs, and manage followed companies.

### For Employers 

- **Employer Registration & Login:** Register as an employer with company email and details.
- **Company Profile:** Manage company name, logo (Google Drive link), and description.
- **Job Posting:** Post new jobs with title, description, location, and salary.
- **Job Management:** Edit or delete posted jobs, view all jobs posted by the company.
- **View Applicants:** See all applicants for each job, view their profiles and resumes.
- **Company Reviews:** View reviews written by jobseekers for your company.
- **Dashboard:** Quick stats on jobs posted, applications received, and followers.

---

##  Project Structure

```
naukri-glassdoor-project/
│
├── manage.py
├── .env
├── requirements.txt
├── ReadMe.md
├── user-personas.md
├── user-stories.md
├── database-blueprint.md
│
├── naukri/                # Django project settings and root URLs
│   ├── settings.py
│   ├── urls.py
│   ├── wsgi.py
│   └── asgi.py
│
├── profiles/              # User, company, and profile management
│   ├── models.py
│   ├── views.py
│   ├── forms.py
│   ├── urls.py
│   ├── admin.py
│   ├── signals.py
│   ├── templates/
│   │   └── profiles/
│   └── management/
│       └── commands/
│           └── data.py    # Sample data population script
│
├── jobs/                  # Job posting, applications, and job actions
│   ├── models.py
│   ├── views.py
│   ├── forms.py
│   ├── urls.py
│   ├── admin.py
│   ├── templates/
│   │   └── jobs/
│   └── static/
│       ├── my_jobs.css
│       └── jobs.js
│
├── reviews/               # Company reviews and replies
│   ├── models.py
│   ├── views.py
│   ├── urls.py
│   ├── admin.py
│   └── templates/
│       └── reviews/
│
└── staticfiles/           # Collected static files for deployment
```

---

## How to Clone and Run Locally

### 1. Clone the Repository

```bash
git clone git@github.com:BhaskarAnil/naukri_clone_project.git
cd naukri_clone_project
```

### 2. Set Up Python Virtual Environment

```bash
python3 -m venv venv
source venv/bin/activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Configure Environment Variables

- Copy `.env.example` to `.env` (if provided), or create a `.env` file in the root directory.
- Set your Django secret key and database credentials (PostgreSQL recommended):

```
NAUKRI_CLONE_DJANGO_SECRET_KEY=your-secret-key
DB_NAME=your_db_name
DB_USER=your_db_user
DB_PASSWORD=your_db_password
DB_HOST=localhost
DB_PORT=5432
DEBUG=True
ALLOWED_HOSTS=localhost,127.0.0.1
```

### 5. Set Up the Database

- Make sure PostgreSQL is running and a database is created.
- Run migrations:

```bash
python manage.py migrate
```

### 6. Load Sample Data (Optional)

Populate the database with sample employers, jobseekers, and jobs:

```bash
python manage.py data
```

### 7. Create a Superuser (Optional)

```bash
python manage.py createsuperuser
```

### 8. Run the Development Server

```bash
python manage.py runserver
```

- Visit [http://localhost:8000](http://localhost:8000) in your browser.

---

## How to View the Project Output

- **Jobseeker:** Register via `/register/`, complete your profile, search and apply for jobs, follow companies, and write reviews.
- **Employer:** Register via `/employer-register/`, set up your company profile, post jobs, and manage applicants.
- **Admin:** Access Django admin at `/admin/` to manage all data.

---

## Key Files and Directories

- `profiles/models.py` — User, Company, Profile, CompanyFollows models.
- `jobs/models.py` — Job, Application, SavedJob, LikedJob, DislikedJob models.
- `reviews/models.py` — CompanyReview, ReviewReply, ReviewLike models.
- `profiles/views.py`, `jobs/views.py`, `reviews/views.py` — All business logic for user flows.
- `profiles/management/commands/data.py` — Script to populate the database with sample data.
- `profiles/templates/`, `jobs/templates/`, `reviews/templates/` — All HTML templates.
- `jobs/static/` — CSS and JS for job-related pages.

---

## Developer Notes

- **Custom User Model:** The project uses a custom user model (`profiles.User`) with `is_employer` flag.
- **Separation of Concerns:** Jobseeker and employer flows are separated in both backend and frontend.
- **Reusable Templates:** Base templates for jobseeker and employer dashboards.
- **Extensible:** Easily add new features like notifications, messaging, or analytics.

---

## User Personas & Stories

- See [`user-personas.md`](user-personas.md) and [`user-stories.md`](user-stories.md) for detailed personas and user stories.

---

## Database Blueprint

- See [`database-blueprint.md`](database-blueprint.md) for full schema and table relationships.

---

## Testing

- Unit tests are located in `profiles/tests.py` and `jobs/tests.py`.
- To run tests:

```bash
python manage.py test
```

---

## Deployment

- Static files are managed with Django's `collectstatic`.
- For production, configure `DEBUG=False` and set allowed hosts in `.env`.
- Use Gunicorn/Uvicorn and a production-ready database.(suggested render)

---