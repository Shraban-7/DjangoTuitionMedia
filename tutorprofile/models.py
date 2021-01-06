from django.conf import settings
from django.contrib.auth.models import User
from django.core.validators import RegexValidator
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver

# from accounts.models import NewUser
from tuition.models import *
from PIL import Image


# Create your models here.


class TutorInfo(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    tuition_status = (('Available', 'Available'), ('Busy', 'Busy'), ('Deactivate', 'Deactivate'))
    tutoring_style = [('Online', 'Online'), ('Private', 'Private'),
                      ('Coaching', 'Coaching'), ('Group', 'Group')]
    Choice_place = (
        ('class_room', 'Class Room'),
        ('Coaching_center', 'Coaching Center'),
        ('home_visit', 'Home Visit'),
        ('my_place', 'My Place')
    )
    prefer_medium = [('English', 'English'), ('Bangla', 'Bangla'),
                     ('Arabic', 'Arabic'), ('Other', 'Other')]
    per_day_choice = [('1 day/week', '1 day/week'), ('2 day/week', '2 day/week'), ('3 day/week', '3 day/week'),
                      ('4 day/week', '4 day/week'),
                      ('5 day/week', '5 day/week'), ('6 day/week', '6 day/week'), ('7 day/week', '7 day/week')]
    class_choice = [('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5'), ('6', '6'), ('7', '7'), ('8', '8'),
                    ('9', '9'), ('10', '10'), ('11', '11'), ('12', '12'), ('Admission Test', 'Admission Test'),
                    ('KG school', 'KG school'),
                    ('Specific Skill Develop', 'Specific Skill Develop'), ('other', 'other')]
    phone_number = models.CharField(max_length=15, unique=True)
    highest_education = models.CharField(max_length=200)
    expected_salary = models.CharField(max_length=20)
    current_tuition_status = models.CharField(max_length=12, choices=tuition_status)
    day_per_week = models.CharField(max_length=12, choices=per_day_choice)
    prefer_tutoring_style = models.CharField(max_length=10, choices=tutoring_style)
    place_of_learning = models.CharField(max_length=19, choices=Choice_place)
    prefer_medium_tutor = models.CharField(max_length=10, choices=prefer_medium)
    prefer_class = models.CharField(max_length=50, choices=class_choice)
    prefer_subjects = models.ManyToManyField(Subject, related_name='subjects')
    video_tutorial = models.URLField(null=True, blank=True)
    prefer_district_to_teach = models.ForeignKey(Country, on_delete=models.CASCADE)
    prefer_area_to_teach = models.CharField(max_length=600, null=True)


class PersonalInformation(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    profile_pic = models.ImageField(upload_to='profile_pic', default='avatar.png')
    birth_date = models.DateField(auto_now=False, auto_now_add=False)
    religion = models.CharField(max_length=50)
    fb_account = models.URLField(null=True, blank=True)
    yt_channel = models.URLField(null=True, blank=True)
    linkedin_pf = models.URLField(null=True, blank=True)
    permanent_address = models.CharField(max_length=250)

    experience = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return f'{self.user.username} Profile'


# @receiver(post_save, sender=User)
# def create_user_profile(sender, instance, created, **kwargs):
#     if created:
#         PersonalInformation.objects.create(user=instance)
#
#
# @receiver(post_save, sender=User)
# def save_user_profile(sender, instance, **kwargs):
#     instance.profile.save()

# def create_profile(sender, **kwargs):
#     if kwargs['created']:
#         user_profile = TutorInfo.objects.create(user=kwargs['instance'])
#
#
# post_save.connect(create_profile, sender=User)
