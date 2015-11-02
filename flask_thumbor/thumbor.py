#!/usr/bin/python
# -*- coding: utf-8 -*-

# thumbor imaging service
# https://github.com/thumby/flask-thumbor/wiki

# Licensed under the MIT license:
# http://www.opensource.org/licenses/mit-license
# Copyright (c) 2015 thumby.io dev@thumby.io


class FlaskThumbor:
    __name__ = "FlaskThumbor"

    def __init__(self, app=None):
        if app is not None:
            self.init_app(app)

    def init_app(self, app):
        from libthumbor import CryptoURL
        from flask import current_app

        thumbor_server = app.config.get('THUMBOR_SERVER', None)
        thumbor_key = app.config.get('THUMBOR_KEY', None)

        if thumbor_server is None or thumbor_key is None:
            raise RuntimeError(
                'Make sure both THUMBOR_SERVER (URL for the thumbor server that will serve your images) and '
                'THUMBOR_KEY (security key for the thumbor server you\'re connecting to) are set in your '
                'Flask configuration.'
            )


        app.thumbor_crypto = CryptoURL(key=thumbor_key)
        app.thumbor_server = thumbor_server.rstrip('/')

        @app.context_processor
        def utility_processor():
            def thumbor(**kw):
                return '%s%s' % (
                    current_app.thumbor_server,
                    current_app.thumbor_crypto.generate(**kw)
                )

            return dict(thumbor=thumbor)
