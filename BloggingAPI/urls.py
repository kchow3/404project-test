from django.conf.urls import patterns, url, include
from rest_framework import routers
from django.contrib import admin
from .views import *


router = routers.SimpleRouter()
router.register(r'author', AuthorViewSet)

urlpatterns = [
    # Examples:
    # url(r'^$', 'BloggingAPI.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^', include(router.urls)),
]
