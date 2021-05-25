from django.conf.urls import url
from django.urls import path, include
from .views import DeviceListApiView


urlpatterns = [
    path('devices', DeviceListApiView.as_view()),
]