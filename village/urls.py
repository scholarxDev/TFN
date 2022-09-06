from django.urls import path
from . import views


urlpatterns = [
    path('', views.request_list, name='request_list'),
    path('fundrequest', views.fundrequest, name='fundrequest'),
    path('request_submitted', views.request_submitted, name='request_submitted'),
    path("<int:pk>/", views.request_detail, name="request_detail"),
    

]