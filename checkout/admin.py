from django.contrib import admin
from . models import Category, Product, StripeKeys, PurchaseLog, ItemPurchaseLog

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug']
    prepopulated_fields = {'slug':('name',)}

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug', 'price', 'available', 'created', 'updated']
    list_filter = ['available', 'created', 'updated']
    prepopulated_fields = {'slug':('name',)}

@admin.register(PurchaseLog)
class PurchaseLogAdmin(admin.ModelAdmin):
    list_display = ['userAccountid', 'purchAmount', 'purchDate', 'totalqty']

@admin.register(ItemPurchaseLog)
class ItemPurchaseLogAdmin(admin.ModelAdmin):
    list_display = ['prodname', 'prodqty', 'userAccountid', 'purchDate']

@admin.register(StripeKeys)
class StripeKeysAdmin(admin.ModelAdmin):
    readonly_fields = ('apikeys',)
    list_display = ['apikeys', ]