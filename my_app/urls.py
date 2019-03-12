# my_app下的urls
from django.conf.urls import url
from . import views

app_name = 'my_app'
urlpatterns = [
    url(r'^$', views.index, name="index")
]
