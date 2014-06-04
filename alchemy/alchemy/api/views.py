from django.conf import settings
from django.contrib.auth.models import User

from rest_framework import viewsets, routers

from alchemy.accounts.models import Account, Transfer, Tag, Shop

# ViewSets define the view behavior.
class AccountViewSet(viewsets.ModelViewSet):
    model = Account

class TransferViewSet(viewsets.ModelViewSet):
    model = Transfer

class TagViewSet(viewsets.ModelViewSet):
    model = Tag

class ShopViewSet(viewsets.ModelViewSet):
    model = Shop

class UserViewSet(viewsets.ModelViewSet):
    model = User
