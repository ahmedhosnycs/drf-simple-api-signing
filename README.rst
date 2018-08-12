===============================================
DRF Simple API Signing (SASigning) Introduction
===============================================

STATUS
^^^^^^

* First Release (29 July 2018)

API Signing Benefits
--------------------

1. Identity Verification: You are sure that the request is coming from who you are expecting.
2. You are sure that the message is not altered in communication channels.
3. You can prevent relay attack (optional).

API Signing Workflow
--------------------

Pseudo code explaining steps of API Signing Check in API::

    1. Read a signature from header.
    2. Construct the message. It may consist of 
       * Secret Key
       * Request Method (PUT, GET, POST, ..)
       * URL Endpoint.
       * Request Body.
       * other arguments
    those parameters are concatenated and separated by **delimeter** symbol.
    3. Hash it with SHA256 using the Secret Key.


What SASigning Do?
------------------

SASigning provides an easy way to configure your API to accept, check and define signatures.
It allows you to review plugin the signature checking in your flow.


========================
SASIGNING DOCUMENTATION
========================

* Visit Docs_.

.. _Docs: https://readthedocs.org/
