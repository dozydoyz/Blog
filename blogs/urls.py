from django.urls import path
from . import views

app_name = 'blogs'

urlpatterns = [

    path('', views.index_view, name='index'),
  
    path('add/', views.add_view, name='add_new'),

    path('edit/<int:blog_id>/', views.edit_view, name='edit_existing'),
]