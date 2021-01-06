from django.contrib import admin
from .models import TuitionPost, Country, Class, Subject, Medium, City

# Register your models here.
admin.site.register(TuitionPost)
admin.site.register(Country)
admin.site.register(City)
admin.site.register(Class)
admin.site.register(Subject)
admin.site.register(Medium)
