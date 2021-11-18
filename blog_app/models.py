from django.db import models
from django.contrib.auth.models import User
# Create your models here.
# class User(models.Model):
#     name = models.CharField(max_length=50)
#     age = models.PositiveIntegerField()
#     address = models.CharField(max_length=50)
#     username = models.CharField(max_length=50)
#     password = models.CharField(max_length=50)
     
#     def __str__(self):
#         return self.username
    
class Blog(models.Model):
    title = models.CharField(max_length=50)
    content = models.TextField(max_length=500)
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    
    def __str__(self):
        return self.title + " by " + self.user.username
    
class Comment(models.Model):
    comment = models.CharField(max_length=100)
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE)
    commented_user = models.ForeignKey(User, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.comment + " for "+ self.blog.title + " by "+ self.commented_user.username
    

    
