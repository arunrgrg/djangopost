from unicodedata import category
from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Post(models.Model):

    category = (
        ('couple jokes','couple jokes'),
        ('politics','politics'),
        ('science', 'science'),
        ('movies','movies'),
        ('health', 'health'),
        ('finance','finance'),      
    )

    post_description = models.CharField(max_length=1000)
    post_img = models.CharField(max_length=1000)
    post_category=models.CharField(max_length=50,choices=category,null=True)
    user = models.ForeignKey(User, on_delete= models.CASCADE)


class Like(models.Model):

    user = models.ForeignKey(User, on_delete= models.CASCADE)
    post = models.ForeignKey(Post)
  




