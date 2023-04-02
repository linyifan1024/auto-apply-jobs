from django.db import models

# Create your models here.
# each user will have a profile 
# each profile will have a list of platforms
# each platform will have a list of jobs
# each job contains a title, company, description, and platform, and a link to the job posting, applied boolean, and date applied
# User -> Profile -> Platform -> Job 
class User(models.Model):
    name = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    def __str__(self):
        return self.name

class Platform(models.Model):
    name = models.CharField(max_length=50)
    website = models.CharField(max_length=100)
    logo = models.CharField(max_length=100)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    def __str__(self):
        return self.name
    
class Job(models.Model):
    title = models.CharField(max_length=100)
    company = models.CharField(max_length=100)
    description = models.TextField()
    platform = models.ForeignKey(Platform, on_delete=models.CASCADE)
    link = models.CharField(max_length=100)
    applied = models.BooleanField(default=False)
    date_applied = models.DateField()
    def __str__(self):
        return self.title


