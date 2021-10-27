from django.db import models
from django.contrib.auth.models import User


class Subject(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(max_length=500,blank=True)
    video = models.FileField(verbose_name="Video", blank=True, null=True)
    ppt = models.FileField(verbose_name="Presentations", blank=True)
    notes = models.FileField(verbose_name="Notes", blank=True)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return self.name
