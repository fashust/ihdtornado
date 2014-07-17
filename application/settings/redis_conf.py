# -*- coding: utf-8 -*- #
"""
    redis configuration
"""
import redis


__author__ = 'fashust'
__email__ = 'fashust.nefor@gmail.com'


REDIS_HOST = 'localhost'
REDIS_PORT = 6379
REDIS_DB = 0
REDIS_PASSWORD = None

REDIS_CONNECTION = redis.Redis(
    host=REDIS_HOST,
    port=REDIS_PORT,
    db=REDIS_DB,
    password=REDIS_PASSWORD
)