from django.conf.urls import url
from django.contrib import admin
from app.funder_views.index import index

urlpatterns = [
    url(r'^', index, name='index'),
]