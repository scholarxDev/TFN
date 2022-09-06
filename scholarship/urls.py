from django.urls import path
from . import views


urlpatterns = [
    path('search/', views.search, name='search'),
    path('', views.scholarship_list, name='scholarship_list'),
    path("<category>/", views.scholarship_category, name="scholarship_category"),

]

