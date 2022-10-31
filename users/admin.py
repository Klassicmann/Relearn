from django.contrib import admin
from .models import Person, StudentProfile, TeacherProfile

# Register your models here.

admin.site.register(Person)
admin.site.register(StudentProfile)
admin.site.register(TeacherProfile)