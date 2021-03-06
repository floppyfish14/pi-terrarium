from django.conf.urls import url

from . import views

app_name = 'humidity'
urlpatterns = [
        url(r'^$', views.index, name='index'),
        url(r'^input/$', views.input, name='input'),
        url(r'^thanks/$', views.thanks, name='thanks'),
        url(r'^daily/$', views.daily, name='daily'),
        url(r'^monthly/$', views.monthly, name='monthly'),
]
