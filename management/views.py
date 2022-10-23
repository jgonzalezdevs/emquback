""" management views """
from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny
from django.contrib.auth import get_user_model
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from django.core.exceptions import ObjectDoesNotExist
from django.http import Http404
from management.models import Device, DeviceLog
from .serializers import DeviceSerializer, RegisterSerializer


class RegisterView(generics.CreateAPIView):
    """ a simple view to carry our register """
    user = get_user_model()
    queryset = user.objects.all()
    permission_classes = (AllowAny,)
    serializer_class = RegisterSerializer


class DeviceViewSet(ModelViewSet):
    """ a simple modelview to carry device requests """
    queryset = Device.objects.all()
    serializer_class = DeviceSerializer


class DeviceLogApiView(APIView):
    """ a simple apiview for device log view """

    def post(self, request):
        """ post method to carry Pin's requests """
        if 'ipv4' in request.data:
            try:
                device = Device.objects.get(ipv4=request.data['ipv4'])
                if device.is_active:
                    DeviceLog.objects.create(device = device, device_answered=True)
                    return Response({"status":True, "response":"PONG"})
                DeviceLog.objects.create(device = device, device_answered=False)
                return Response({"status":False, "response":"PONG"})
            except ObjectDoesNotExist:
                raise Http404
        else:
            raise Http404
