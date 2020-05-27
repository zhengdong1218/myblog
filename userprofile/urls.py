from . import views
from django.urls import path,include

urlpatterns = [
    path('login/', views.user_login, name='login'),
    path('logout/', views.user_logout, name='logout'),
    path('register/', views.user_register, name='register'),
    path('delete/<int:id_user_delete>/', views.user_delete, name='delete'),
]