from django.urls import path

from Calciapp import views

urlpatterns = [
    path('',views.home),
    path('read',views.read_data),
]