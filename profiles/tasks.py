# profiles/tasks.py

from celery import shared_task
from django.core.mail import send_mail
from django.conf import settings

@shared_task
def send_welcome_email(email, name):
    identity = name.split("@")[1]
    name = name.split("@")[0]
    subject = "Welcome to Naukri Clone!"
    if identity == "jobseeker":
        message = (
        f"Hi {name},\n\n"
        "Welcome to Naukri Clone!\n\n"
        "We're excited to have you join our jobseeker community. As you take the next step "
        "in your career, we're here to support you with thousands of job listings from top companies.\n\n"
        "Here’s what you can do next:\n"
        "- Complete your profile to receive personalized job recommendations\n"
        "- Search and apply to jobs that match your skills and interests\n"
        "- Save jobs for later or follow companies you're interested in\n"
        "- Share your experience by writing reviews about companies\n\n"
        "We believe in your potential and are committed to helping you succeed.\n\n"
        "If you need any assistance, feel free to contact our support team anytime.\n\n"
        "Happy job hunting!\n"
        "The Naukri Clone Team"
    )
    else:
        message = (
        f"Hi {name},\n\n"
        "Welcome to Naukri Clone!\n\n"
        "Thank you for registering your company with us. You now have access to tools that help "
        "you connect with top talent quickly and efficiently.\n\n"
        "Here’s what you can do next:\n"
        "- Set up your company profile with logo, description, and location\n"
        "- Post job listings with detailed descriptions and required skills\n"
        "- Manage applicants, view resumes, and track job applications\n"
        "- Engage with jobseekers and respond to company reviews\n\n"
        "We’re excited to help you build your team with the best candidates.\n\n"
        "If you have any questions, feel free to contact our support team.\n\n"
        "Happy hiring!\n"
        "The Naukri Clone Team"
    )
    from_email = settings.DEFAULT_FROM_EMAIL
    recipient_list = [email]

    send_mail(subject, message, from_email, recipient_list)
