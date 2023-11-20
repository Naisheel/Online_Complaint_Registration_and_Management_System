from django.urls import include, path
from . import views
from django.conf import settings
from django.contrib.auth import views as auth_views

urlpatterns= [
    path('',views.index,name='index'),
    path('aboutus/',views.aboutus,name='aboutus'),
    path('signin/',auth_views.LoginView.as_view(template_name='CMsystem/signin.html'), name='signin'),
    path('logout/', auth_views.LogoutView.as_view(template_name='CMsystem/logout.html'), name='logout'),
    path('register/', views.register, name='register'),
    path('password-reset/',
         auth_views.PasswordResetView.as_view(
             template_name='CMsystem/password_reset.html'
         ),
         name='password_reset'),
    path('password-reset-done/',
         auth_views.PasswordResetDoneView.as_view(
             template_name='CMsystem/password_reset_done.html'
         ),
         name='password_reset_done'),
    path('reset/<uidb64>/<token>/',
         auth_views.PasswordResetConfirmView.as_view(
             template_name='CMsystem/password_reset_confirm.html'
         ),
         name='password_reset_confirm'),
    path('password-reset-complete/',
         auth_views.PasswordResetCompleteView.as_view(
             template_name='CMsystem/password_reset_complete.html'
         ),
         name='password_reset_complete'),
]