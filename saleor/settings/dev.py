from .base import *
DATABASES = {
    'default': dj_database_url.config(
        default='postgres://kabdelmagid:Nicodem8s@localhost:5432/saleor',
        conn_max_age=600)}

SECRET_KEY = 'devel'
DEBUG = True
