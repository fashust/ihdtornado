# -*- coding: utf-8 -*- #
"""
    user data dumping
"""
import json


__author__ = 'fashust'
__email__ = 'fashust.nefor@gmail.com'


def dump_user_data(user, cache, handler , cb, **kwargs):
    """
        dump all user data to python dict
    """
    cache_key = 'user_data:{0}'.format(user.username)
    cache_data = cache.get(cache_key)
    data = {}
    default = {'SELECTED_FLAT': None}
    if cache_data:
        data = json.loads(cache_data.decode('utf-8'))
    else:
        data.update({
            'user': user.as_dict,
            'flats': None,
            'menu': handler.render_string(
                'menu.html',
                **default
            ).decode('utf-8'),
            'data': handler.render_string(
                'data.html',
                **default
            ).decode('utf-8')
        })
        cache.set(cache_key, json.dumps(data), 60)
    cb(data)