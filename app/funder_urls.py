from django.conf.urls import url
from django.contrib import admin
from app.funder_views.index import index
from app.funder_views.donate import donation

urlpatterns = [
    url(r'^$', index, name='index'),
    url(r'^donate/', donation, name="donation")
]