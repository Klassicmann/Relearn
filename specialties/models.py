from django.db import models

# Create your models here.
class Specialty(models.Model):
    # django already set auto primary key
    specialty_name = models.CharField(max_length=200)
    
    def __str__(self):
        return self.specialty_name


class Classe(models.Model):
    class_name = models.CharField(max_length=200)
    specialty = models.ForeignKey(Specialty, on_delete=models.CASCADE)

    def __str__(self):
        return self.class_name + " " + self.specialty.specialty_name

class Subject(models.Model):
    classe = models.ForeignKey(Classe, on_delete=models.CASCADE)
    subject_name = models.CharField(max_length=200, default=True)
    
    def __str__(self):
        return self.subject_name
