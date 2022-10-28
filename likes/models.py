from django.db import models
from stackQA.models import Question,Answer
from users.models import User
# Create your models here.

class Like(models.Model):
    liker = models.ForeignKey(User,related_name='liker', on_delete=models.CASCADE)
    post = models.ForeignKey(Question,Answer)