=========================================
Simple API Signing for Django (SASigning)
=========================================

This package facilitates the way of API Signing in Django projects.

Detailed documentation is in the "docs" directory.

Quick start
-----------

This package is now available as a middleware.
(Next releases will support different specific features for Django Rest Framework)

Steps:

1. Add "SASigningMiddleware" to your MIDDLEWARE setting like this::

    MIDDLEWARE = [
        'django.middleware.security.SecurityMiddleware',
        'django.contrib.sessions.middleware.SessionMiddleware',
        'django.middleware.common.CommonMiddleware',
        'django.middleware.csrf.CsrfViewMiddleware',
        'django.contrib.auth.middleware.AuthenticationMiddleware',
        'django.contrib.messages.middleware.MessageMiddleware',
        'django.middleware.clickjacking.XFrameOptionsMiddleware',
        # Add the end of middlewares
        'simple_api_signing.common.middleware.SASigningMiddleware',
    ]

References
----------
1. API Request Signing in Django [Link] (https://medium.com/elements/api-request-signing-in-django-bc9389201871)
