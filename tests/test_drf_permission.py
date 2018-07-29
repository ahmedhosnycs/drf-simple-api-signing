"""Testcases for API signing."""
import hashlib
import hmac
from base64 import b64encode

import pytest
from django.test.client import RequestFactory

from simple_api_signing.common.rest_permission import SASigningPermission
from simple_api_signing.exceptions import APIAccessDenied


class TestDRFPermission(object):
    """Testcase for views with SASigningPermission."""

    def setup_class(self):
        """Initialize common objects."""
        self.request_factory = RequestFactory()

    def test_no_signing_header(self):
        """Unit test posting with no signature header."""
        request = self.request_factory.get('/')
        permission = SASigningPermission()
        with pytest.raises(APIAccessDenied):
            permission.has_permission(request)

    def test_invalid_signature(self):
        """Unit test posting with invalid header."""
        headers = {
            "HTTP_SIGNATURE": "wrong-signature"
        }
        request = self.request_factory.get('/', **headers)
        permission = SASigningPermission()
        with pytest.raises(APIAccessDenied):
            permission.has_permission(request)

    def test_valid_signature(self):
        """Unit test posting with valid header."""
        secret = 'secret-key'
        message = '$'.join(['/', 'GET', secret])
        message = message.encode('utf-8')
        computed_signature = hmac.new(
            secret.encode('utf-8'),
            msg=message,
            digestmod=hashlib.sha256
        ).digest()
        expected_sig = b64encode(computed_signature).decode()
        headers = {
            "HTTP_SIGNATURE": expected_sig
        }
        request = self.request_factory.get('/', **headers)
        permission = SASigningPermission()
        assert permission.has_permission(request)
