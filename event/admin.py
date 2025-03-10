from django.contrib import admin
from . models import Event, StripeKeys, EventPurchaseLog

@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug', 'description', 'price']
    prepopulated_fields = {'slug':('name',)}

@admin.register(EventPurchaseLog)
class EventPurchaseLogAdmin(admin.ModelAdmin):
    list_display = ['name', 'userAccountid', 'purchDate', 'confnum']

@admin.register(StripeKeys)
class StripeKeysAdmin(admin.ModelAdmin):
    readonly_fields = ('apikeys',)
    list_display = ['apikeys', ]