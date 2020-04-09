from django.conf.urls import url
from django.contrib import admin
from app.funder_views.index import index
from app.funder_views.donate import donation
from app.funder_views.grants import grant
urlpatterns = [
    url(r'^$', index, name='index'),
    url(r'^donate/', donation, name="donation"),
    url(r'^grants/', grant, name="grant")
]