"""
URL configuration for edusphere project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from users.views import (
    InstructorRegistrationView,
    AdminRegistrationView,
    StudentRegistrationView,
    InstructorLoginView,
    AdminLoginView,
    StudentLoginView
)

urlpatterns = [
    path('admin/', admin.site.urls),
    # Registration URLs
    path('register/instructor/', InstructorRegistrationView.as_view(), name='instructor-register'),
    path('register/admin/', AdminRegistrationView.as_view(), name='admin-register'),
    path('register/student/', StudentRegistrationView.as_view(), name='student-register'),
    
    # Login URLs
    path('login/instructor/', InstructorLoginView.as_view(), name='instructor-login'),
    path('login/admin/', AdminLoginView.as_view(), name='admin-login'),
    path('login/student/', StudentLoginView.as_view(), name='student-login'),

]
