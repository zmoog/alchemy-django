from django.contrib import admin
from .models import Account
from .models import Transfer
from .models import Tag
from .models import Shop

class AccountAdmin(admin.ModelAdmin):
    list_display = ('title', 'balance', 'created',)

class TransferAdmin(admin.ModelAdmin):
    list_display = ('amount', 'description', 'source', 'destination', 'value_date',)
    exclude = ('tags', 'shops',)

class TagAdmin(admin.ModelAdmin):
    pass

class ShopAdmin(admin.ModelAdmin):
    pass

admin.site.register(Account, AccountAdmin)
admin.site.register(Transfer, TransferAdmin)
admin.site.register(Tag, TagAdmin)
admin.site.register(Shop, ShopAdmin)
