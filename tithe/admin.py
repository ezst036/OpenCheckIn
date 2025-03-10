from django.contrib import admin
from . models import TitheLog, StripeKeys

@admin.register(TitheLog)
class TitheLogAdmin(admin.ModelAdmin):
    list_display = ['userEmailAddress', 'userAccountid', 'giveAmount', 'givingType', 'giveDate']

@admin.register(StripeKeys)
class StripeKeysAdmin(admin.ModelAdmin):
    readonly_fields = ('apikeys',)
    list_display = ['apikeys', ]