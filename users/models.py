from django.db import models
from django.contrib.auth.models import User
import os
from django.urls import reverse


class UserProfileInfo(models.Model):

    #creating a relationship with user class (not inheriting)
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    #adding additional attributes
    bio = models.CharField(max_length=500)
    profile_pic = models.ImageField(verbose_name="Profile Picture", blank=True)
    teacher = 'teacher'
    student = 'student'
    user_types = [
        (teacher, 'teacher'),
        (student, 'student'),
    ]
    user_type = models.CharField(max_length=10, choices=user_types, default=student)

    def __str__(self):
        return self.user.username

class Contact(models.Model):
    name = models.CharField(max_length=150)
    email = models.CharField(max_length=150)
    feedback = models.TextField()

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('index')
