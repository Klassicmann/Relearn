from django.db import models
from users.models import User

# Create your models here.


class Question(models.Model):
    usr_id = models.CharField(max_length=200)
    question = models.CharField(max_length=255)
    answered = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    amountvotes = models.IntegerField(default=0)

    def __str__(self):
        return self.question


class Answer(models.Model):
    question_id = models.ForeignKey(
        Question, on_delete=models.CASCADE, blank=False, null=True
    )
    answer = models.TextField(max_length=2550)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    amountvotes = models.IntegerField(default=0)

    def __str__(self):
        return self.answer
