from django.db import models
from django.contrib.auth.models import AbstractUser, User

# your models here.
class Speciality(models.Model):
    # django already set auto primary key
    Speciality_name = models.CharField(max_length=200)


class Classe(models.Model):
    class_name = models.CharField(max_length=200)
    speciality = models.ForeignKey(Speciality, on_delete=models.CASCADE)


class Subject(models.Model):
    class_id = models.ForeignKey(Classe, on_delete=models.CASCADE)


class Person(models.Model):
    person_id = models.ForeignKey(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=11, blank=False, null=True)
    current_address = models.CharField(max_length=100, null=True)
    image = models.ImageField(default='default.jpg', upload_to='profile_pics')
    email = models.CharField(max_length=200)
    person_type = models.BooleanField(default=True)
    status = models.BooleanField(default=True)


class StudentProfile(models.Model):
    student = models.ForeignKey(Person, on_delete=models.CASCADE)
    classe = models.ForeignKey(Classe, on_delete=models.CASCADE)


class TeacherProfile(models.Model):
    teacher = models.ForeignKey(Person, on_delete=models.CASCADE)
    bio = models.CharField(max_length=255, blank=True)



