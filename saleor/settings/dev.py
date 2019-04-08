from .base import *

DATABASES = {
    'default': dj_database_url.config(
        default='postgres://kabdelmagid:Nicodem8s@localhost:5432/saleor',
        # default='postgres://saleor_kelly:saleor_kelly@localhost:5432/saleor_kelly',
        conn_max_age=600)}

SECRET_KEY = 'devel'
DEBUG = True
