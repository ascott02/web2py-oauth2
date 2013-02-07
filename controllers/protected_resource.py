#!/usr/bin/python
# -*- coding: utf-8 -*-


@validate_access_token
def index():
    """Protected resource. For test purposes. It uses a decorator to validate
    the token. You can find it at models/utils.py.
    """

    response.headers['Content-Type'] = json_headers()
    response.view = json_service()

    msg = "The colonel's 7 secret herbs and spices are..."

    return meta_data(CODES['ok'], MESSAGES['ok'],
                     dict(data='Protected resource {0}'.format(msg)))
