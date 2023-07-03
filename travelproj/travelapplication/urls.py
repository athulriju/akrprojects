from django.urls import path
from travelapplication import views

urlpatterns = [
    path('', views.demo, name='demo'),
    ]