

from django.contrib import admin
from django.urls import path
from django.conf.urls import include, url

urlpatterns = [
    path('admin/', admin.site.urls),
    url(r'^funds/', include('app.funder_urls')),
    url(r'^adminstrators/', include('app.administrator_urls')),

]
