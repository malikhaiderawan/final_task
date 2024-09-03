from django.contrib import admin
from django.urls import path
from e_app import views

urlpatterns = [
    path('',views.home,name='home'),
    path('accounts/login/register/',views.register,name='register'),
    path('accounts/login/',views.Login,name='login'),
    path('logout/',views.Logout,name='logout'),
    path('orders/',views.user_orders,name='orders'),
    path('profile/',views.profile_management,name='profile'),
    path('order_tracking/',views.order_tracking,name='tracking'),

]



