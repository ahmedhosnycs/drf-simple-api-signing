================
Advanced Topics
================

*****************************************
Request Signature from API Consumer View
*****************************************

The consumer should usually obtain the secret key in a secure channel, then he calcualtes the signature and send it with each request. SASigning is expecting the signature to be in ``SIGNATURE`` header.

Skeleton of a Signed Request
-----------------------------

.. http:example:: curl httpie python-requests

    GET /endpoint HTTP/1.1
    Content-Type: application/json
    Host: localhost
    Accept: application/json
    API-SIGNATURE: <hash-calculated-with-secret-key (HMAC)>

What Needed for Signature Calculation from The Client
-----------------------------------------------------

* Secret Key
* Delimeter
* Fields used to construct the signature.
* Hash function used.

Steps for Signature Calculation
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

1. You should generate '<field-1>(delimeter)<field-2>(delimeter)<field-n>(delimeter)<secret key>' string.

**Default string ``<endpoint><method(GET, POST)><secret>``**

The message that calculates the signature contains the fields of the requests separated by a delimeter and concatenated in the end with the secret key.

2. Create HMAC with a Hash function with the secret key.
3. Encode64 the output.

..

    :Default Fields used in SASigning:
        Endpoint (Ex: ``/users/``)
        Request Method (GET, POST, ...)

    :Default Delimeter:
        Empty string (``''``)

    :Default Hash Function:
        SHA256

Python Example
^^^^^^^^^^^^^^

.. code-block:: python

    def compute_signature(secret, method, path):
        """Return computed signature."""
        # method (request.mehtod), path (request.path)
        params = [path, method, secret]
        data = "".join(params)
        computed_sig = hmac.new(
            secret.encode('utf-8'), msg=data.encode('utf-8'),
            digestmod=sha256
        ).digest()
        return b64encode(computed_sig).decode()

NodeJS Example
^^^^^^^^^^^^^^

.. code-block:: nodejs

    var cryto = require('crypto');
    var data = endpoint + '' + method + '' + secretKey
    var hash = crypto.createHmac('sha256', secretKey).update(data);
    hash.digest('base64');


*******************
SASigning Settings
*******************

You can customize how the signature is computed using the following settings.

:``SA_SIGNING_SECRET_KEY``:

**Required String**. It is the secret key used in signature computation in both backend and API consumer.

::

    **IMPORTANT**:
    This secret key should be passed to API consumer in a secure way.
    This version supports only one consumer with one secret key

:``SA_SIGNING_DELIMETER``:

Optional String. By default empty string ``''``

:``SA_SIGNING_FIELDS``:

Optional List. by default ``['path', 'method']``.

::

    It is a list of attributes that are resolved from `request` object.
    If not found in `request` object, it tries to be resolved from `request.META`.
    If not found a `ValueError` exception is raised.

:``SA_SIGNING_HASH_FUNCTION``:

Optional String. By default ``sha256``.

You can use any hash function from ``hashlib`` Library_

.. _Library: https://docs.python.org/3/library/hashlib.html

