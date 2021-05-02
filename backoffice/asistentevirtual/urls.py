"""asistentevirtual URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from django.urls import path

from pages.views import home_view
from devices.views import device_index_view, device_show_view, device_create_view, device_update_view, device_delete_view

urlpatterns = [
    path('', home_view, name='home'),
    path('admin/', admin.site.urls),

    path('devices/', device_index_view, name='device-index'),
    path('devices/<int:id>', device_show_view, name='device-show'),
    path('devices/create', device_create_view, name='device-create'),
    path('devices/<int:id>/update/', device_update_view, name='device-update'),
    path('devices/<int:id>/delete/', device_delete_view, name='device-delete'),
]
