from django.db import models


class Country(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name


class City(models.Model):
    country = models.ForeignKey(Country, on_delete=models.CASCADE)
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name


class Subject(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Class(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Medium(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class TuitionPost(models.Model):
    per_day_choice = [('1 day/week', '1 day/week'), ('2 day/week', '2 day/week'), ('3 day/week', '3 day/week'),
                      ('4 day/week', '4 day/week'),
                      ('5 day/week', '5 day/week'), ('6 day/week', '6 day/week'), ('7 day/week', '7 day/week')]
    gender = [('Male', 'Male'), ('Female', 'Female'), ('Other', 'Other')]
    style = (('Online', 'Online'), ('Private', 'Private'),
             ('Coaching', 'Coaching'), ('Group', 'Group'))
    prefer_medium = [('English', 'English'), ('Bangla', 'Bangla'),
                     ('Arabic', 'Arabic'), ('Other', 'Other')]
    class_choice = [('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5'), ('6', '6'), ('7', '7'), ('8', '8'),
                    ('9', '9'), ('10', '10'), ('11', '11'), ('12', '12'), ('KG school', 'KG school'),
                    ('Specific Skill Develop', 'Specific Skill Develop'), ('other', 'other')]
    sno = models.AutoField(primary_key=True)
    fullname = models.CharField(max_length=100)
    country = models.ForeignKey(Country, on_delete=models.CASCADE)
    city = models.ForeignKey(City, on_delete=models.SET_NULL, null=True)
    class_other = models.CharField(max_length=23,choices=class_choice)
    medium = models.CharField(max_length=7, choices=prefer_medium, default='Bangla')
    subjects = models.CharField(max_length=250)
    school_college = models.CharField(max_length=500)
    student_quantity = models.CharField(max_length=2)
    student_gender = models.CharField(max_length=6, choices=gender, default='Other')
    detail_tuition = models.TextField()
    day_per_week = models.CharField(max_length=10, choices=per_day_choice, default='3 day/week')
    salary = models.CharField(max_length=50)
    desire_tutor_gender = models.CharField(max_length=6, choices=gender, default='Other')
    preference_tuition_style = models.CharField(max_length=8, choices=style, default='Private')
    address = models.CharField(max_length=250)
    mobile = models.CharField(max_length=11)
    email = models.EmailField(max_length=50)
    available = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.fullname
