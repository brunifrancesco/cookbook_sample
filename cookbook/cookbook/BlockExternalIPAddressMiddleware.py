
import logging

from django.http import HttpResponse

logger = logging.getLogger('request')

class BlockExternalIPAddress:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request, *args, **kwargs):
        return self.get_response(request)

    def process_view(self, request, *args, **kwargs):
        if request.META['HTTP_HOST'] in ('localhost:8000',):
            return None
        return HttpResponse("Denied", status=403)