"""Module provides a middleware for API Signing."""
from rest_framework.permissions import BasePermission

from simple_api_signing.utils import APISigningFlow


class SASigningPermission(BasePermission):
    """Check the signature as API permission."""

    def has_permission(self, request, *args, **kwargs):
        """Checking the permission in DRF."""
        api_signing_flow = APISigningFlow()
        if not api_signing_flow.is_valid(request, rest_exception=True):
            api_signing_flow.not_valid_handler(rest_exception=True)
        return True
