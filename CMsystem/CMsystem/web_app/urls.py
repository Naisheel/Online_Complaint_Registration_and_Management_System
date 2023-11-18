from django.urls import include, path
from . import views
from django.conf import settings
from django.contrib.auth import views as auth_views

urlpatterns= [
    path('',views.index,name='index'),
    path('aboutus/',views.aboutus,name='aboutus'),
    path('signin/',auth_views.LoginView.as_view(template_name='CMsystem/signin.html'), name='signin'),
    path('register/', views.register, name='register')
]