from django.contrib import admin
from .models import Person, StudentProfile, TeacherProfile

# Register your models here.


class PersonAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'person_type')


admin.site.register(Person, PersonAdmin)
admin.site.register(StudentProfile)
admin.site.register(TeacherProfile)