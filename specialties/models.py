from django.db import models

# Create your models here.
class Specialty(models.Model):
    # django already set auto primary key
    specialty_name = models.CharField(max_length=200)


class Classe(models.Model):
    class_name = models.CharField(max_length=200)
    specialty = models.ForeignKey(Specialty, on_delete=models.CASCADE)


class Subject(models.Model):
    classe = models.ForeignKey(Classe, on_delete=models.CASCADE)
