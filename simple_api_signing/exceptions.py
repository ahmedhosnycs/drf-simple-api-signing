"""Custom Exceptions."""
from rest_framework.exceptions import APIException


class SignatureMissMatch(Exception):
    """Raised when the signatures are not matched."""

    pass


class SignatureHeaderMissing(Exception):
    """Raised when the request does not have the signature."""

    pass


class APIAccessDenied(APIException):
    """Raised when SASigning is used as a view permission."""

    status_code = 401
    default_detail = "API Access Denied. Signature is not valid."
    default_code = "api_access_denied"
