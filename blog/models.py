from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class mywebblog(models.Model):
    title= models.CharField(max_length=100, unique=True)
    wblog = models.TextField()
    
    createtime = models.DateField(auto_now_add=True)
    update_time = models.DateField(auto_now=True)
    
    
    
    def __str__(self):
        return self.title




