from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Todo(models.Model):
    author = models.ForeignKey(User,on_delete = models.CASCADE)
    text = models.CharField(max_length = 120)
    created_at = models.DateTimeField(auto_now_add = True)

    def __str__(self):
        return self.text


