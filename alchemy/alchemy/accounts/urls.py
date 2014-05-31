from django.conf.urls import patterns, url
from .views import AccountList, AccountDetail
from .views import TransferList, TransferDetail
from .views import TagList, TagDetail
from .views import ShopList, ShopDetail


urlpatterns = patterns('',

    url(r'^a/$', AccountList.as_view(), name='account_list'),
    url(r'^a/(?P<pk>[^/]+)/$', AccountDetail.as_view(), name='account_detail'),

    url(r'^t/$', TransferList.as_view(), name='transfer_list'),
    url(r'^t/(?P<pk>[^/]+)/$', TransferDetail.as_view(), name='transfer_detail'),

    url(r'^tag/$', TagList.as_view(), name='tag_list'),
    url(r'^tag/(?P<pk>[^/]+)/$', TagDetail.as_view(), name='tag_detail'),

    url(r'^shop/$', ShopList.as_view(), name='shop_list'),
    url(r'^shop/(?P<pk>[^/]+)/$', ShopDetail.as_view(), name='shop_detail'),
)
