from django.contrib import admin
from . models import Event, StripeKeys, EventPurchaseLog

@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    def time_seconds(self, obj):
        return obj.timefield.strftime("%d %b %Y %H:%M:%S")
    time_seconds.admin_order_field = 'timefield'
    time_seconds.short_description = 'Precise Time'
    
    list_display = ['name', 'slug', 'description', 'price', 'startdate', 'enddate']
    prepopulated_fields = {'slug':('name',)}

@admin.register(EventPurchaseLog)
class EventPurchaseLogAdmin(admin.ModelAdmin):
    list_display = ['name', 'userAccountid', 'purchDate', 'confnum']

@admin.register(StripeKeys)
class StripeKeysAdmin(admin.ModelAdmin):
    readonly_fields = ('apikeys',)
    list_display = ['apikeys', ]