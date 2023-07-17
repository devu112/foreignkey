from django.contrib import admin
from django.urls import path,include
from .import views


urlpatterns = [
    path('',views.home,name='home'),
    path('addcourse',views.addcourse,name='addcourse'),
    path('addstudent',views.addstudent,name='addstudent'),
    path('showdetails',views.showdetails,name='showdetails'),
    path('course_db',views.course_db,name='course_db'),
    path('studentdb',views.studentdb,name='studentdb'),
    path('edit/<int:pk>',views.edit,name='edit'),
    path('editdb/<int:pk>',views.editdb,name='editdb'),
    path('delete/<int:pk>',views.delete,name='delete'),
]