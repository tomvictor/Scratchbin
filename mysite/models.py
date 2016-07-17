from django.db import models
from django.utils import timezone
# Create your models here.


class accounts(models.Model):
    first_name = models.CharField(max_length=30)
    last_name  = models.CharField(max_length=30)
    email_id   =models.EmailField(max_length=40)
    mobile_no  =models.CharField(max_length=20)
    date_of_birth = models.DateField(default=timezone.now())
    gender_choice = (
        ('M','Male'),('F','Female')
    )
    gender = models.CharField(max_length=10, choices=gender_choice)
    def __str__(self):
        return self.first_name

class notes(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    author =models.ForeignKey('auth.User')
    published_date = models.DateTimeField(default=timezone.now())
    last_update_date = models.DateField(default=timezone.now())
    draft_staus   = models.BooleanField()
    def __str__(self):
        return self.title