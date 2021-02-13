
import logging

logger = logging.getLogger('request')

class LogMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request, *args, **kwargs):
        print("Getting the input...")
        logger.info("Incoming request => %s" %request)
        logger.info("Incoming user => %s" %request.user)
        response = self.get_response(request)
        print("Computed response")
        return response