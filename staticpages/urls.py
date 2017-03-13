from django.conf.urls import url

from . import views


app_name = 'staticpages'
urlpatterns = [
    url(r'^$', views.home, name='home'),
]
