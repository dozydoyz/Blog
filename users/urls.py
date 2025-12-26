from django.urls import path, include
from . import views

app_name = 'users'

urlpatterns = [
    path('', include('django.contrib.auth.urls')), # 登录
    path('register/', views.register, name='register'), # 注册
]