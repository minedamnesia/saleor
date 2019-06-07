from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^community/$', views.index, name='community_index')
]
