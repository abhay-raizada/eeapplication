from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'crawler', views.index, name='index'),
    url(r'website', views.website, name = 'website')
]