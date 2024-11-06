from django.urls import path
from . import views
urlpatterns = [  
    path('',views.indexpage, name='index'),
    path('login/', views.loginPage,name='login'),
    path('register/', views.registerpage,name='register'), 
    path('profile/', views.profilepage,name='profile'),
    path('logout/',views.logoutpage, name='logout'),
    path('edit-profile/',views.editprofile,name='editprofile'),
    path('add-job/',views.addjobpage,name='addjob'),
    path('view-job/',views.viewjobpage,name='viewjobs'),
    path('edit-job/<int:job_id>/', views.editjobpage, name='editjob'),
    path('delete-job/<int:job_id>/', views.deletejobpage, name='deletejob'), 
    path('jobs/', views.jobsearchpage, name='jobsearch'),
    path('job-apply/<int:job_id>/',views.jobapplypage,name='jobapply'),
    path('applied-job-user/',views.applieduserjobpage,name='appliedjobuser'),
    path('applied-job-view/',views.appliedjobviewpage,name='appliedjobview'),
    path('skill-match/',views.skillMatchingPage,name='skillmatch')

]