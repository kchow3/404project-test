from django.conf.urls import patterns, url, include
from django.contrib import admin
from .views import *

urlpatterns = [
    # Examples:
    # url(r'^$', 'BloggingAPI.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),

    url(r'^author/$', views.AuthorView.as_view(), name='author-list'),
]
