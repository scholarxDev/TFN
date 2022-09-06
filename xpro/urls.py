from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('signup/', views.signup, name='signup'),
    path('signup/student/', views.student, name='student'),
    path('signup/school/', views.school, name='school'),
    path('signup/sponsor/', views.sponsor, name='sponsor'),
    path('signup/sponsor/', views.sponsor, name='sponsor'),
    path('activation_sent/', views.activation_sent, name='activation_sent'),
    path('activate/<uidb64>/<token>/', views.activate, name='activate'),
    path('student/dashboard/', views.studentDashboard, name='student-dashboard'),
    path('student/profile/', views.studentProfile, name='student-profile'),
    path('student/profile/edit/', views.editStudentProfile, name='edit-student-profile'),
    path('school/dashboard/', views.schoolDashboard, name='school-dashboard'),
    path('school/profile/', views.schoolProfile, name='school-profile'),
    path('school/profile/edit/', views.editSchoolProfile, name='edit-school-profile'),
    path('sponsor/success', views.sponsorSuccess, name='sponsor-success'),
    path('sponsor/dashboard/', views.sponsorDashboard, name='sponsor-dashboard'),
    path('sponsor/profile/', views.sponsorProfile, name='sponsor-Profile'),
    path('sponsor/profile/edit/', views.editSponsorProfile, name='edit-sponsor-profile'),
 
]