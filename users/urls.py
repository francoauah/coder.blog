from re import template
from django.urls import path
from .views import UserRegister, UserProfileEdit, PasswordChangesView, ProfilePage, EditProfilePage, CreateProfilePage
from django.contrib.auth import views as auth_views
from . import views 
urlpatterns = [
    path('register/', UserRegister.as_view(), name = 'register'),
    path('edit_profile/', UserProfileEdit.as_view(), name = 'edit_profile'),
    path('password/', PasswordChangesView.as_view(template_name= 'registration/change_password.html')),
    path('password_success', views.password_success, name = 'password_success'),
    path('<int:pk>/profile/', ProfilePage.as_view(), name='profile' ),
    path('<int:pk>/edit_profile_page/', EditProfilePage.as_view(), name='edit_profile_page' ),
    path('create_profile_page/', CreateProfilePage.as_view(), name='create_profile_page' ),
]