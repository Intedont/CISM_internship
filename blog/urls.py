from django.urls import path, include
from django.contrib.auth import views
import blog.views

urlpatterns = [
    path('', blog.views.index),
    path('signup/', blog.views.signup),
    path('login/', views.LoginView.as_view(), name='login'),
    path('accounts/<slug:username>/', blog.views.profile),
    path('logout/', views.LogoutView.as_view()),
    path('like/<int:id>', blog.views.like),
    path('delete/<int:id>', blog.views.delete),
    path('wastebin/', blog.views.wastebin),
    path('restore/<int:id>', blog.views.restore),
    path('add_comment/<int:id>', blog.views.addComment)
]