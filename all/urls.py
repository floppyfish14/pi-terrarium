from django.conf.urls import url

from . import views

app_name = 'all'
urlpatterns = [
        url(r'^$', views.index, name='index')
,
]
