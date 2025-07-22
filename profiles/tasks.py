# profiles/tasks.py

from celery import shared_task
from django.core.mail import send_mail
from django.conf import settings

@shared_task
def send_welcome_email(email, name,identity):
    subject = "Welcome to Naukri Clone!"
    if identity == "jobseeker":
        message = f"""
                    Hi {name},

                    Welcome to Naukri Clone! 

                    We're excited to have you on board as you take the next step in your career journey. With thousands of job listings and top companies hiring, you're just a few clicks away from your dream job.

                    Here is what you can do next:
                    Complete your profile to get the best job recommendations  
                    Explore and apply to jobs that match your skills and interests  
                    Save jobs for later, and follow companies you admire  
                    Write reviews to share your workplace experiences  

                    We believe in your potential and are here to help you succeed.  
                    If you need any support, feel free to contact our team.

                    Happy job hunting!  
                    — The Naukri Clone Team
                    """
    else:
        message = f"""
                    Hi {name},

                    Welcome to Naukri Clone! 

                    We're thrilled to have your company join our growing network of employers who are hiring top talent every day. With your new employer account, you can start connecting with qualified candidates in just a few steps.

                    Here is what you can do next:
                    Complete your company profile to attract the right candidates  
                    Post job openings and track applicants in real-time  
                    View jobseeker profiles, resumes, and engagement  
                    Respond to company reviews and build your employer brand  

                    We are committed to helping you build a stronger team, faster.

                    If you need any assistance, do not hesitate to reach out to us.

                    Best regards,  
                    — The Naukri Clone Team
                    """
    from_email = settings.DEFAULT_FROM_EMAIL
    recipient_list = [email]

    send_mail(subject, message, from_email, recipient_list)
