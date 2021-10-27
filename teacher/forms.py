from django import forms
from .models import Subject

class LessonForm(forms.ModelForm):
    class Meta:
        model = Subject
        fields = "__all__"
        exclude = ['created_by', "created_at"]

