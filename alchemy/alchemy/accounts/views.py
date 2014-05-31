from django.views.generic import ListView
from django.views.generic import DetailView

from .models import Account
from .models import Transfer
from .models import Tag
from .models import Shop


class AccountList(ListView):
    model = Account
    paginate_by = 10

class AccountDetail(DetailView):
    model = Account


class TransferList(ListView):
    model = Transfer
    paginate_by = 10

class TransferDetail(DetailView):
    model = Transfer


class TagList(ListView):
    model = Tag
    paginate_by = 10

class TagDetail(DetailView):
    model = Tag


class ShopList(ListView):
    model = Shop
    paginate_by = 10

class ShopDetail(DetailView):
    model = Shop
