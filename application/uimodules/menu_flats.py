# -*- coding: utf-8 -*- #
"""

"""
from tornado.web import UIModule


__author__ = 'fashust'
__email__ = 'fashust.nefor@gmail.com'


class SelectedFlat(UIModule):
    """
        render selected flat
    """
    def render(self, selected_flat, flats):
        """
            render template
        """
        return self.render_string(
            'uimodules/selected_flat.html',
            flats=flats,
            selected_flat=selected_flat
        )
