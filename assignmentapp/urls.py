
from django.contrib import admin
from django.urls import path,include
from . import views

urlpatterns = [
    path('',views.home,name='home'),
    path('login/',views.login_user,name='login'),
    path('register/',views.register,name='register'),
    path('submit/',views.submit,name='submit'),
    path('logout/',views.logout_user,name='logout'),
    path('dashboard/',views.teacher_dashboard,name='dashboard'),
    path('assignment/update/<int:id>/',views.update_assignment,name='update_assignment'),
]
