"""Different functions that is used to facilitate API Signing flow."""
import hashlib
import hmac
from base64 import b64encode

from django.conf import settings

from simple_api_signing.exceptions import (APIAccessDenied,
                                           SignatureHeaderMissing,
                                           SignatureMissMatch)


class APISigningFlow(object):
    """APISigningFlow controls signing flow."""

    def __init__(self, *args, **kwargs):
        """Constructor that initialize settings."""
        self.delimeter = getattr(settings, "SA_SIGNING_DELIMETER", '')
        self.signature_fields = getattr(
            settings,
            "SA_SIGNING_FIELDS",
            ['path', 'method']  # DEFAULT VALUES
        )
        self.hash_func_name = getattr(
            settings, "SA_SIGNING_HASH_FUNCTION", "sha256"
        )
        try:
            self.hash_func = getattr(hashlib, self.hash_func_name)
            self.secret_key = settings.SA_SIGNING_SECRET_KEY
        except AttributeError as e:
            exception_message = "Missing Simple API Signing Configuration. "
            raise AttributeError(exception_message + str(e))

    def is_valid(self, request, rest_exception=False):
        """Compare signature with the expected."""
        api_signature = request.META.get('HTTP_SIGNATURE', None)
        if not api_signature:
            if not rest_exception:
                raise SignatureHeaderMissing()
            raise APIAccessDenied()

        fields_values = self._get_fields_values(request)
        message = self.delimeter.join(fields_values)
        message = message.encode('utf-8')
        computed_signature = hmac.new(
            self.secret_key.encode('utf-8'),
            msg=message,
            digestmod=self.hash_func
        ).digest()
        expected_sig = b64encode(computed_signature).decode()
        # compare between expected and sent
        return expected_sig == api_signature

    def _get_fields_values(self, request):
        """Resolve fields to values."""
        fields_values = []
        for field in self.signature_fields:
            value = None
            try:
                value = getattr(request, field)
            except AttributeError:
                value = getattr(request.META, field, None)
            except ValueError:
                pass
            if not value:
                raise ValueError(
                    "{} cannot be resolved from request object".format(field)
                )
            fields_values.append(value)

        # Always append secret at the end of the fields
        fields_values.append(self.secret_key)
        return fields_values

    def not_valid_handler(self, rest_exception=False):
        """Handler invoked when the signature is not valid."""
        if not rest_exception:
            raise SignatureMissMatch("Signature Missmatch")
        raise APIAccessDenied()
