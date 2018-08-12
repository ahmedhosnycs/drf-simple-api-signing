==========================
Installation & Quick Start
==========================

To install the package, run the following command in your virtual environment

``pip install drf-simple-api-signing``


Configuration
-------------

* Add your `Secret Key` that will be used in signature computation.

``SA_SIGNING_SECRET_KEY = 'some-random-secret-key'``

By adding this setting, your signature will be calculated using this secret key.

* Add ``SASigningPermission`` permission class as Django Rest Framework setting::
    
    REST_FRAMEWORK = {
        'DEFAULT_PERMISSION_CLASSES': {
            ...
            # Other permission classes
            'simple_api_signing.common.rest_permission.SASigningPermission',
            # Other permission classes
            ...
        }
    }


By Adding only those settings, your API now will only accept signed signatures.
Below we will explain how to receive signatures from the Frontend or API consumers.

Exclude Specific Endpoint from Signature Checking
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Sometimes you want specific endpoint to be avaliable for public consumers, it can be for testing or marketing or other purposes. To exclude endpoint from being checked by signature, you can do this::

    class MyAPIViewSet(ViewSet):
        permission_classes = ()
        ...


Apply API Signing Checking only For Specific Endpoint
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Instead of adding this to ``DEFAULT_PERMISSION_CLASSES``, you can apply API signature only on specific endpoints::

    from simple_api_signing.common.rest_permission import SASigningPermission


    class MyAPIViewSet(ViewSet):
        permission_classes = (SASigningPermission,)
        ....

Use SASigning Directly with Django, without DRF
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

This package also is compatible using only django, without django rest framework.

Instead of putting the ``permission_class`` in ``settings.py`` we have to add **SASigningMiddleware** to the ``MIDDLEWARE`` setting like this:

**NOTE: Using it as a middleware will apply signature verification over all the Django views, endpoints and requests.**::

    MIDDLEWARE = [
        ..,
        'simple_api_signing.common.middleware.SASigningMiddleware',
    ]
