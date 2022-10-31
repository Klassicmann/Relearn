from django.contrib import admin

from .models import Classe, Specialty, Subject

# Register your models here.
admin.site.register(Specialty)
admin.site.register(Classe)
admin.site.register(Subject)