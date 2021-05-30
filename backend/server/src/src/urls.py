"""src URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.contrib.auth.views import LogoutView
from django.views.generic import TemplateView
from django.http import StreamingHttpResponse
from camera.camera import gen_frames

urlpatterns = [
    path('', include('index.urls'),name='home'),
    path('admin/', admin.site.urls, name='admin'),
    path('index/', include('index.urls')),
    path('devices/',include('camera.urls')),
    path('accounts/',include('allauth.urls')),
    path('automation/', include('automation.urls')),
    path('logout/', LogoutView.as_view()),
#    path('monitor/<int:pk>', lambda pk: StreamingHttpResponse(gen_frames(pk),content_type='multipart/x-mixed-replace; boundary=frame'),name='monitor_pk'),
]
