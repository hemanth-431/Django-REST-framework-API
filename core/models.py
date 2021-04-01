from django.contrib.auth import get_user_model
from django.db import models

User=get_user_model()

class Contact(models.Model):
    email=models.EmailField()
    name = models.CharField(max_length=30)
    number = models.CharField(max_length=10) 
    def __str__(self):
        return self.number

class Post(models.Model):
    title=models.CharField(max_length=100)
    description=models.TextField()
    timestamp=models.DateTimeField(auto_now_add=True)
    owner=models.ForeignKey(User,on_delete=models.CASCADE)

    def __str__(self):
        return self.title
