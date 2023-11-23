"""
URL configuration for airplanes project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.conf.urls import handler404, handler500
from django.contrib import admin
from django.urls import path
from airplanes.views import *

from django.conf import settings
from django.conf.urls.static import static

handler404 = error404
handler500 = error500

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', show_index),
    path('api/upload', api_upload_file),
    path('create/', show_create),
    path('update/', show_update),
    path('api/create', api_create),
    path('api/update', api_update_profpic),
    path('upload/', show_upload),
    path('success/', show_success),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)