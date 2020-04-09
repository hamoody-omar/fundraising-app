from django.conf.urls import url
from django.contrib import admin
from app.funder_views.index import index
from app.funder_views.donate import donation
from app.funder_views.sponsor import sponsor

urlpatterns = [
    url(r'^$', index, name='index'),
    url(r'^donate/', donation, name="donation"),
    url(r'^sponsor/', sponsor, name="sponsor"),
]
