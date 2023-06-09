from django.db import models

# Create your models here.
# each user will have a profile 
# each profile will have a list of platforms
# each platform will have a list of jobs
# each job contains a title, company, description, and platform, and a link to the job posting, applied boolean, and date applied
# User -> Profile -> Platform -> Job 
class User(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100, unique=True, null=False)
    email = models.CharField(max_length=100, unique=True, null=False)
    password = models.CharField(max_length=100, null=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    # def __str__(self):
    #     return self.name

# linkdingin, indeed, glassdoor, etc
# exmaple: linkedin, linkedin.com, linkedin.png, user,
class Platform(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    website = models.CharField(max_length=100)
    logo = models.CharField(max_length=100)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    email = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    def __str__(self):
        return self.name

# example: software engineer, google, description, linkedin, link, false, 2021-01-01
class Job(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=100)
    company = models.CharField(max_length=100)
    description = models.TextField()
    platform = models.ForeignKey(Platform, on_delete=models.CASCADE)
    link = models.CharField(max_length=100)
    applied = models.BooleanField(default=False)
    date_applied = models.DateField()
    def __str__(self):
        return self.title


