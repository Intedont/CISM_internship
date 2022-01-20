from django.urls import path, include
from django.contrib.auth import views
import blog.views

urlpatterns = [
    path('index/', blog.views.index),
    path('signup/', blog.views.signup),
    path('login/', views.LoginView.as_view(), name='login')
]