# -*- coding: utf-8 -*- #
"""
    index page view handler
"""
from application.handlers import BaseRequestHandler


__author__ = 'fashust'
__email__ = 'fashust.nefor@gmail.com'


class IndexViewHandler(BaseRequestHandler):
    """
        index page handler
    """
    def get(self):
        """
            get
        """
        controller = 'noauth'
        if self.current_user:
            controller = 'user'
        self.render(
            'index_a.html' if self.current_user else 'index_na.html',
            controller=controller
        )