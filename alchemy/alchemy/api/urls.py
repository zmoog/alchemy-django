from django.conf.urls import include, patterns, url
from django.contrib.auth.models import User

from rest_framework import routers

from .views import AccountViewSet, TransferViewSet, TagViewSet, ShopViewSet, UserViewSet


# Routers provide an easy way of automatically determining the URL conf.
router = routers.DefaultRouter()
router.register(r'accounts', AccountViewSet)
router.register(r'transfers', TransferViewSet)
router.register(r'tags', TagViewSet)
router.register(r'shops', ShopViewSet)
router.register(r'users', UserViewSet)


# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browseable API.
urlpatterns = patterns('',
    url(r'^', include(router.urls)),
    url(r'^auth/', include('rest_framework.urls', namespace='rest_framework'))
)
