
from django.conf.urls import include, url
from django.contrib import admin
from the_hello_app.views import say_hello, get_the_time

urlpatterns = [
    url(r'^hello$', say_hello),
    url(r'^time$' , get_the_time),

]


