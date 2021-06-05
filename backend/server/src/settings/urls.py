from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.settings, name='settings'),
    path('<int:ip>/ptz_up', views.ptz_up, name='ptz_up'),
    path('<int:ip>/ptz_down', views.ptz_down, name='ptz_down'),
    path('<int:pk>/ptz_left', views.ptz_left, name='ptz_left'),
    path('<int:pk>/ptz_right', views.ptz_right, name='ptz_right'),
    path('<int:pk>/set_focus', views.set_focus, name='set_focus'),
    path('<int:pk>/apply_settings', views.apply_settings, name='apply_settings'),
]
