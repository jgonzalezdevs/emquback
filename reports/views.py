""" report views """
from django.http import Http404
from rest_framework.exceptions import ValidationError
from rest_framework import viewsets
from rest_framework.response import Response
from django.core.exceptions import ObjectDoesNotExist
from management.models import DeviceLog
from .utils.functions import get_ping_counts

class ReportViewSet(viewsets.ViewSet):
    """
    A simple ViewSet for listing or retrieving reports.
    """
    def list(self):
        """ method for report listing """
        ping_counts = get_ping_counts(DeviceLog.objects.all())
        return Response(ping_counts)

    def retrieve(self, request):
        """ method for retrieve report  """
        if "ipv4" in request.GET:
            try:
                ping_counts = get_ping_counts(DeviceLog.objects.filter(
                                        device__ipv4=request.GET["ipv4"])
                                            )
                if len(ping_counts) == 0:
                    raise ValidationError
                return Response(ping_counts)
            except ObjectDoesNotExist:
                raise Http404
        raise ValidationError
