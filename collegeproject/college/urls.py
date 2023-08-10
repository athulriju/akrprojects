from . import views
from django.contrib import admin
from django.urls import include, path

urlpatterns = [
   
   
    path('',views.index,name='index'),
    path('register',views.register,name='register'),
    path('login',views.login,name='login'),
    path('logout',views.logout,name='logout'),
    path('home',views.home,name='home'),
    path('enquiry',views.enquiry,name='enquiry'),
    # path('ajax/load-branches/', views.load_branches, name='ajax_load_branches'),
    # path('get-topics-ajax/', views.get_topics_ajax, name="get_topics_ajax"),
    path('get_courses/', views.get_courses, name='get_courses'),
    # path('show_message/', views.show_message, name='show_message'),
]