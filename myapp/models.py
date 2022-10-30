from django.db import models

# Create your models here.


class Student(models.Model):
    name = models.CharField(max_length=100, blank=False, null=False)
    age = models.IntegerField(blank=True, null=True)
    grade = models.IntegerField(blank=True, null=True)


class Contact(models.Model):
    email = models.EmailField(max_length=50)
    name = models.CharField(max_length=30, blank=True, null=True)
    message = models.TextField(max_length=100, blank=True, null=True)
    