TorchMed
==============================

Software Development and Online Services for Healthcare.

https://torchmed.com

LICENSE: MIT

TECHNOLOGIES
------------

- Python 3.4+
- Django 1.9+
- PostgreSQL 9.5+
- Gunicorn 19.6.0
- Nginx 1.11.1
- Docker-Compose 1.7+
- Fabric Python 3
- Django-Environ

HOW TO RUN IT
-------------

.. code-block::
   
   git clone https://www.github.com/torchmed/torchmed
   cd torchmed
   cp env.example .env
   docker-compose up

And finally access http://locahost:8080

FEATURES
--------

- 3 languages (English, Portuguese and Polish)
- Send Email using Backend

TODO
--------

- Integrate TravisCI
- User Registration
- Improve Templates
- Enable Dashboard
- Write and translate more texts