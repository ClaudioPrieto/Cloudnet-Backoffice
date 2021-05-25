from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import permissions
from devices.models import Device
from .serializers import DeviceSerializer

class DeviceListApiView(APIView):
    # add permission to check if user is authenticated
    # permission_classes = [permissions.IsAuthenticated]

    # 1. List all
    def get(self, request, *args, **kwargs):
        '''
        List all the Device items for given requested user
        '''
        devices = Device.objects.all().order_by('name')
        serializer = DeviceSerializer(devices, many=True, context={'request': request})
        return Response(serializer.data, status=status.HTTP_200_OK)
