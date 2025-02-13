# from accounts.models import NewUser
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.admin import User

from tutorprofile.models import TutorInfo, PersonalInformation
#
#
# @receiver(post_save, sender=NewUser)
# def post_profile_save(sender, instance, created, **kwargs):
#     if created:
#         TutorInfo.objects.create(user=instance)
#
#
# @receiver(post_save, sender=NewUser)
# def post_profile_save(sender, instance, created, **kwargs):
#     if created:
#         PersonalInformation.objects.create(user=instance)


@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
    if created:
        PersonalInformation.objects.create(user=instance)


@receiver(post_save, sender=User)
def save_profile(sender, instance, **kwargs):
    instance.profile.save()
