# DRF Simple API Signing (SASigning)
![](https://travis-ci.org/ahmedhosnycs/drf-simple-api-signing.svg?branch=master)
[![Documentation Status](https://readthedocs.org/projects/drf-simple-api-signing/badge/?version=latest)](https://drf-simple-api-signing.readthedocs.io/en/latest/?badge=latest)

## STATUS
* First Release (29 July 2018)

-----------------------------------------------------------
-----------------------------------------------------------

This package facilitates the way of API Signing in Django and DRF projects. This can be used when you are intending to build an API to add an extra layer of security. One of the key features of this package is that it tries to maximaize the customization of security.

If you want to understand more about how the API signing works, please check *Links section* below.

## Quick Start
* First, install the package and run the following command:
```
pip install drf-simple-api-signing
```

### Setup
* Add the `SA_SIGNING_SECRET_KEY` in `settings.py`. It will be used in signature computation.
```
SA_SIGNING_SECRET_KEY = 'some-strong-random-secret-key'
```

* Also you have to add the permission class in the `Rest Framework` configuration in  `settings.py`

```
REST_FRAMEWORK = {
    'DEFAULT_PERMISSION_CLASSES': {
        'simple_api_signing.common.rest_permission.SASigningPermission',
    },
    ...
}
```
**All the endpoints in your project will be protected with this signing.**

### How to use it
Now we have our API ready to listen signed requests.

All the requests have to be sent with a `SIGNATURE` header with the correct value.

This `SIGNATURE` header has to contain the correct value. To generate the correct signature we can to do it in all the languages: Python, JS, PHP, Java, etc.

Python:
```
import hashlib
import hmac
from base64 import b64encode

data = ''.join([path, method, secret])
computed_sig = hmac.new(
                secret.encode('utf-8'), 
                msg=data.encode('utf-8'),
                digestmod=sha256
               ).digest()
b64encode(computed_sig).decode()
```

NodeJS:
```
var cryto = require('crypto');

var data = path + '' + method + '' + secret
var hash = crypto.createHmac('sha256', secret).update(data);
hash.digest('base64');
```

Where:
* `secret` is the value that you put in `SA_SIGNING_SECRET_KEY`
* `path` is the part of the request without the domain and query params. With slash. Example: /login
* `method` is the HTTP method. Example: GET, POST, PUT, DELETE

**Note that this is the example by default, you can check the documentation to add more complexity or change some parts**

Then with this signature you can call the API and will be validated.


## Remove signing from specific endpoints
If you want to remove the permission clss in some endpoint you can remove it using
this in your views:
```
class ExampleViewSet(ViewSet):
    permission_classes = ()
    ...
```
Now all the `ExampleViewSet` will be unprotected without the signing.

## Add signing in specific endpoints
If you want to use this signing only in some endpoints you don't have to put the 
permission class in the default configuration of `Django Rest Framework` in `settings.py`.

* Remove the `SASigningPermission` class from `DEFAULT_PERMISSION_CLASSES` in `REST_FRAMEWORK` in the `settings.py` file if you put it.
* Add the permission directly in the specific view:
```
from simple_api_signing.common.rest_permission import SASigningPermission


class ExampleViewSet(ViewSet):
    permission_classes = (SASigningPermission,)
    ...
```

## Use it directy with Django, without DRF
This package also is compatible using only django, without django rest framework.

Instead of putting the `permission_class` in `settings.py` we have to add **SASigningMiddleware** to the `MIDDLEWARE` setting like this:

**NOTE: if you want to use the middleware you can't do it with an specific endpoint.**

```
    MIDDLEWARE = [
        ..,
        'simple_api_signing.common.middleware.SASigningMiddleware',
    ]
```


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
6. Before submitting a Pull Request, make sure to rebase with the latest commit on `develop`.
7. Collaborators will review, then you have to address their comments in your PR.
