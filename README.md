# Simple API Signing for Django (SASigning)
![](https://travis-ci.org/ahmedhosnycs/drf-simple-api-signing.svg?branch=master)

## STATUS
* First Release (29 July 2018)

-----------------------------------------------------------
-----------------------------------------------------------


This package facilitates the way of API Signing in Django projects. This can be used when you are intending to build an API to add an extra layer of security. One of the key features of this package is that it tries to maximaize the customization of security.

If you want to understand more about how the API signing works, please check *Links section* below.

## Quick Start
You can use this package in two modes:

1. As a global middleware request signing.
2. As a Django Rest Framework permission class.

* First, install the package, run the following command:
```
pip install drf-simple-api-signing
```

* Add your `Secret Key` that will be used in signature computation.
```
SA_SIGNING_SECRET_KEY = 'some-random-secret-key'
```

By adding this setting, your signature will be calculated using this secret key.


By default, expected signature will be constructed using the following attributes:

    * Endpoint (request.path)
    * Method (GET, POST, PUT, ...)
    * SA_SIGNING_SECRET_KEY
    with empty delimeter and sha256 as a hashing function.

### Global Middlware Mode


* Add ***SASigningMiddleware*** to your `MIDDLEWARE` setting like this:


```
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
```

### DRF Permission Class

* Inside a view, you can import the ***SASigningPermission*** permission.

```
from simple_api_signing.common.rest_permission import SASigningPermission


class APIViewSet(ViewSet):
    permission_classes = (SASigningPermission, )
    ...
    ...
```

* You can also add this class in `settings.py`

```
REST_FRAMEWORK = {
    'DEFAULT_PERMISSION_CLASSES': {
        'simple_api_signing.common.rest_permission. SASigningPermission',
    }
}
```


***NOTE:*** **Signature should always be sent as a Request Header with name `SIGNATURE`.**

### Signature Setting Customization

You can customize how the signature is computed using the following settings.



**`SA_SIGNING_SECRET_KEY`**

Required String. It is the secret key used in signature computation in both backend and API consumer.

***(SECURITY Caution):***

This secret key should be passed to API consumer in a secure way.

This version supports only one consumer with one secret key


**`SA_SIGNING_DELIMETER`**

Optional String. By default `''`

**`SA_SIGNING_FIELDS`**

Optional List. by default `['path', 'method']`.

It is a list of attributes that are resolved from `request` object.

If not found in `request` object, it tries to be resolved from `request.META`.

If not found a `ValueError` exception is raised.

**`SA_SIGNING_HASH_FUNCTION`**

Optional String. By default `sha256`.

You can use any hash function from `hashlib` [library](https://docs.python.org/3/library/hashlib.html).


## Links
* [API Request Signing in Django](https://medium.com/elements/api-request-signing-in-django-bc9389201871)

## Contribution

We encourage developers to contribute, so please feel free to fix bugs, improve things, provide documentation.

Contribution steps are simple:

1. Create an issue and explain your feature/bugfix.
2. This indeed should initiate the discussion about it.
3. Once it is approved, it will be labeled with `accepted`.
4. Fork the repo and make sure that all unit tests are working on your development environment.
5. Create a branch from `develop`.
6. Before submitting a Pull Request, make sure to rebase with the latest thing on `develop`.
7. Collaborators will review, then you have to address their comments in your PR.
