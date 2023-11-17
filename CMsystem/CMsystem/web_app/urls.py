from django.urls import include, path
from . import views
from django.conf import settings

urlpatterns= [
    path('',views.index,name='index'),
    path('aboutus/',views.aboutus,name='aboutus')
]