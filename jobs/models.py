from django.db import models

# Create your models here.
class Job(models.Model):
    #Images 
    image = models.ImageField(upload_to='images/')
    #Summary
    summary = models.CharField(max_length=200) 
    location = models.CharField(max_length=200,default='Pune,India' )
    designation = models.CharField(max_length=200 ,default='SE')
    duration = models.CharField(max_length=200,default='')
    
    def __str__(self):
        return self.summary