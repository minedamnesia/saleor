from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^about_us/$', views.about_us, name='about_us'),
    url(r'^faq/$', views.faq, name='faq'),
    url(r'^policy/$', views.policy, name='policy'),
    url(r'^shipping_policy/$', views.shipping_policy, name='shipping_policy'),
    url(r'^tos/$', views.tos, name='tos'),
    url(r'^upcoming_events/$', views.upcoming_events, name='upcoming_events'),
    url(r'^brewing_guide/$', views.brewing_guide, name='brewing_guide')
]
