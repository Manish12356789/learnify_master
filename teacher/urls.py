from django.urls import path
from . import views

urlpatterns = [
    path('', views.viewSubject, name='subject_list')
    path('details/<id>', views.viewSubjectDetails, name='subject_details_list')
    path('edit/<id>' views.updateSubject, name='lesson_update')
    path('delete/<id>' views.deleteSubject, name='lesson_delete')


]
