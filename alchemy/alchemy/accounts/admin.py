from django.contrib import admin
from .models import Account
from .models import Transfer
from .models import Tag
from .models import Location

class AccountAdmin(admin.ModelAdmin):
    list_display = ('title', 'balance', 'created',)

class TransferAdmin(admin.ModelAdmin):
    exclude = ('tags', 'locations',)

class TagAdmin(admin.ModelAdmin):
    pass

class LocationAdmin(admin.ModelAdmin):
    pass

admin.site.register(Account, AccountAdmin)
admin.site.register(Transfer, TransferAdmin)
admin.site.register(Tag, TagAdmin)
admin.site.register(Location, LocationAdmin)
