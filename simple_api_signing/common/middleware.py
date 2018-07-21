"""Module provides a middleware for API Signing."""
from simple_api_signing.utils import APISigningFlow


class SASigningMiddleware:
    """Middleware that responsible to check the signing headers."""

    def __init__(self, get_response):
        """Constructor."""
        self.get_response = get_response

    def __call__(self, request):
        """Logic that executes for each request."""
        api_signing_flow = APISigningFlow()
        if not api_signing_flow.is_valid(request):
            api_signing_flow.not_valid_handler()

        return self.get_response(request)
