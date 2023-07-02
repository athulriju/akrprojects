from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    # path('delete/<int:id>/', views.delete, name='delete'),
    # path('update/<int:id>/', views.update, name='update'),   
    path('list', views.List.as_view(), name='list'),
    path('detail/<int:pk>/', views.Detail.as_view(), name='detail'),
    path('update/<int:pk>/', views.Update.as_view(), name='update'),
    path('delete/<int:pk>/', views.Delete.as_view(), name='delete'),
]
