from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from .models import User, Profile, Company,CompanyFollows
from jobs.models import Application, SavedJob, LikedJob,DislikedJob


@receiver(post_save, sender=User)
def create_related_profile(sender, instance, created, **kwargs):
    if created:
        if instance.is_employer:
            Company.objects.create(user=instance)
        else:
            Profile.objects.create(user=instance)
@receiver([post_save, post_delete], sender=Application)
@receiver([post_save, post_delete], sender=SavedJob)
@receiver([post_save, post_delete], sender=LikedJob)
@receiver([post_save, post_delete], sender=DislikedJob)
@receiver([post_save, post_delete], sender=CompanyFollows)
def update_user_interactions_signal(sender, instance, **kwargs):
    from jobs.documents import UserInteractionDocument
    try:
        UserInteractionDocument().update(instance.user)
    except Exception as e:
        print("Error updating interaction doc:", e)
