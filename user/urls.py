from django.urls import path
from . import views

urlpatterns = {
    
    path('index', views.index),
    path('createAccount', views.user_signup),
    path('login',views.user_login)

}