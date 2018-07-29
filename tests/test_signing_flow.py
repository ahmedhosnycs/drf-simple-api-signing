"""Testcases for api signing flow."""
import hashlib
import hmac
from base64 import b64encode

import pytest
from django.test.client import RequestFactory

from simple_api_signing.exceptions import SignatureHeaderMissing
from simple_api_signing.utils import APISigningFlow


class TestSigningFlow(object):
    """Testcases for APISigningFlow class."""

    def setup_class(self):
        """Initialize common objects."""
        self.api_signing = APISigningFlow()
        self.request_factory = RequestFactory()

    def test_initialization(self):
        """Unit test for initializing the APISigningFlow class."""
        assert self.api_signing.delimeter == '$'
        assert 'method' in self.api_signing.signature_fields
        assert self.api_signing.hash_func_name == 'sha256'
        assert self.api_signing.secret_key == 'secret-key'

    def test_missing_signing_header(self):
        """Test valid request headers."""
        request = self.request_factory.get('/')
        with pytest.raises(SignatureHeaderMissing):
            self.api_signing.is_valid(request)

    def test_invalid_signature(self):
        """Test invalid signature sent."""
        headers = {
            "HTTP_SIGNATURE": "wrong-signature"
        }
        request = self.request_factory.get('/', **headers)
        assert not self.api_signing.is_valid(request)

    def test_valid_signature(self):
        """Test valid signature."""
        message = '$'.join(['/', 'GET', self.api_signing.secret_key])
        message = message.encode('utf-8')
        computed_signature = hmac.new(
            self.api_signing.secret_key.encode('utf-8'),
            msg=message,
            digestmod=hashlib.sha256
        ).digest()
        expected_sig = b64encode(computed_signature).decode()
        headers = {
            "HTTP_SIGNATURE": expected_sig
        }
        request = self.request_factory.get('/', **headers)
        assert self.api_signing.is_valid(request)
