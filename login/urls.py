from django.urls import path
from . import views

urlpatterns = [
    path('',views.index,name='Index'),
    path('home/',views.home,name='Home'),
    path('logout/',views.logout,name='Logout'),
    path('signin/',views.signin,name='SignIn'),
    path('success/<int:id>',views.success,name='Success'),
]