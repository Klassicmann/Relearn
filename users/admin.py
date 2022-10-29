from django.contrib import admin
from .models import Speciality, Classe, Subject, Person, StudentProfile, TeacherProfile

# Register your models here.

admin.site.register(Speciality)
admin.site.register(Classe)
admin.site.register(Subject)
admin.site.register(Person)
admin.site.register(StudentProfile)
admin.site.register(TeacherProfile)