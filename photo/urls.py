from django.urls import path
from . import views


urlpatterns = [
    path("upload/", views.upload, name='upload'),
    path("upload/<slug:pk>", views.upload, name='upload'),	

]
