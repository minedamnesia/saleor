from .base import *

DATABASES = {
    'default': dj_database_url.config(
        default='postgres://kabdelmagid:Nicodem8s@localhost:5432/saleor',
        # default='postgres://saleor_kelly:saleor_kelly@localhost:5432/saleor_kelly',
        conn_max_age=600)}

SECRET_KEY = 'devel'
DEBUG = True
STRIPE_PUBLIC_KEY='pk_test_rE7eW0Zba5doK6d3woy8eJDn'
STRIPE_SECRET_KEY='sk_test_4aKKnSvViRa0VASVho9krAGx'
STRIPE_STORE_NAME="Kelly's Tea Salon"
