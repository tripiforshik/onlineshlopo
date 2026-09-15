from tkinter.font import names

from django.contrib.auth.views import LoginView,PasswordChangeView,PasswordChangeDoneView
from django.contrib.auth.views import LogoutView,PasswordResetView,PasswordResetDoneView,PasswordResetConfirmView,PasswordResetCompleteView
from django.urls import path,include
from .views import  ProfileView

urlpatterns = [
    path('profile/<str:user_name>/',ProfileView.as_view(),name="profile"),
    path('logout/',LogoutView.as_view(),name='logout'),
    path('login/',LoginView.as_view(),name='login'),
    path('password_change/',PasswordChangeView.as_view(),name='password_change'),
    path('password_change_done/',PasswordChangeDoneView.as_view(),name='password_change_done'),
    path('password_reset/',PasswordResetView.as_view(),name='password_reset'),
    path('password_reset_done/',PasswordResetDoneView.as_view(),name='password_reset_done'),
    path('password_reset/<uidb64>/<token>/',PasswordResetConfirmView.as_view(),name='password_reset_confirm'),
    path('password_reset_complete/',PasswordResetCompleteView.as_view(),name="password_reset_complete")
]