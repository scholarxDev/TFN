from django.urls import path
from . import views


urlpatterns = [
    path('', views.payment_index, name='payment_index'),
    path('payment_handler/', views.payment_handler, name='payment_handler'),
    path('payment_successful/', views.payment_successful, name='payment_successful'),
]