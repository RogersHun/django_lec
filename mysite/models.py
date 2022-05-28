from django.db import models
from django.contrib.auth.models import User

class MainContent(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    pub_date = models.DateTimeField('date published')

class Comment(models.Model):
    author = models.ForeignKey(User,on_delete=models.CASCADE)
    content_list = models.ForeignKey(MainContent,on_delete=models.CASCADE)
    content = models.TextField()
    create_date = models.DateTimeField(auto_now_add=True)
    modify_date = models.DateTimeField(auto_now=True)