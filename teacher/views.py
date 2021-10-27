from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from teacher.models import Subject 
from teaching_blog.decorators import teacher_required

@teacher_required
@login_required
def createSubject(request):
    if request.method == "POST":
        form = LessonForm(request.POST)
        if form.is_valid():
            form.save()
        else:
            print(form.errors)
    return render(request, "teacher/lesson_create.html", {"form":form })


@teacher_required
@login_required
def viewSubject(request):
    subjects = Subject.objects.all()
    return render(request, "teacher/lesson_list_view.html", {"subjects":subjects })


@teacher_required
@login_required
def viewSubjectDetails(request, id):
    subjects = Subject.objects.get(id=id)
    return render(request, "teacher/lesson_detail_view.html", {"subjects":subjects })



@teacher_required
@login_required
def updateSubject(request, id):
    subject = Subject.objects.get(id=id)
    form = LessonForm(instance=subject)
    if request.method == "POST":
        form = LessonForm(request.POST, instance=subject)
        if form.is_valid():
            form.save()
            return redirect('subject_details')
    else:
        print(form.error)
    return render(request, "teacher/lesson_update.html", {"form":form })



@teacher_required
@login_required
def deleteSubject(request, id):
    Subject.objects.filter(id=id).delete()
    return redirect('subject_details')
