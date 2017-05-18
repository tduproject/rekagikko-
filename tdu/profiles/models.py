from django.db import models
from django.utils import timezone

class UserProfile(models.Model):
    name = models.CharField(max_length = 20)
    email = models.EmailField(max_length = 254,default='example@me.com')
    grade = models.CharField(max_length = 5)
    major = models.CharField(max_length = 5)
    text = models.TextField()

    def publish(self):
        self.save()

    def __str__(self):
        return self.name
