from django.db import models
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import User

from specialties.models import Classe
# your models here.


class Person(models.Model):
    person_id = models.ForeignKey(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=11, blank=False, null=True)
    current_address = models.CharField(max_length=100, null=True)
    image = models.ImageField(default='default.jpg', upload_to='profile_pics')
    email = models.CharField(max_length=200)
    
    class PersonType(models.TextChoices):
        student = 'ST',_('Student')
        teacher = 'TE',_('Teacher')

    person_type = models.CharField(
        max_length = 2,
        choices = PersonType.choices,
        default = PersonType.student
    )

    def __str__(self):
        return self.first_name + ' ' + self.last_name


class StudentProfile(models.Model):
    student = models.ForeignKey(Person, on_delete=models.CASCADE)
    classe = models.ForeignKey(Classe, on_delete=models.CASCADE)
    
    def __str__(self):
        return str(
            {
                'Name ' : self.student.first_name + " " + self.student.last_name,
                'Classe ' : self.classe.class_name,
                'Specialty ': self.classe.specialty.specialty_name
            }
        )


class TeacherProfile(models.Model):
    teacher = models.ForeignKey(Person, on_delete=models.CASCADE)
    bio = models.CharField(max_length=255, blank=True)
    
    def __str__(self):
        return self.teacher.first_name + " " + self.teacher.last_name



