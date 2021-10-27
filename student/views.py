from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from teaching_blog.decorators import student_required
from teacher.models import Subject 

@student_required
@login_required
def subject(request):
    subjects = Subject.objects.all()
    return render(request, "user/lesson_list_view.html", {"subjects":subjects })