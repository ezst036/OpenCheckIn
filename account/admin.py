from django.contrib import admin
from account.models import Account, Youth, Family, UIPrefs, CheckInQr, YouthCheckInLog
from connect.models import ContactConnect, TwilioPrefs
from django.contrib.auth.admin import UserAdmin
from datetime import datetime

class AccountAdmin(UserAdmin):
    list_display = ('email', 'username', 'first_name', 'last_name', 'is_parent',
        'is_staff', 'is_volunteer', 'is_pastor', 'is_missionary', 'is_active')
    search_fields = ('email', 'username')
    readonly_fields = ('date_joined', 'last_login')

    list_filter = ()
    fieldsets = ()

admin.site.register(Account, AccountAdmin)

class YouthAdmin(admin.ModelAdmin):
    list_display = ('youth_first_name', 'youth_last_name', 'youth_birth_day', 'is_checked_in')
    readonly_fields = ('youth_birth_day', 'date_joined', 'last_checkin', 'last_checkout')
    search_fields = ('youth_first_name', 'youth_last_name')

    actions = ['set_is_checked_in', 'set_check_out']

    def set_is_checked_in(self, request, queryset):
        for youth in queryset:
            youth.last_checkin = datetime.now()
            youth.is_checked_in = True
            youth.save()
    
    set_is_checked_in.short_description = 'Check in'

    def set_check_out(self, request, queryset):
        for youth in queryset:
            youth.last_checkout = datetime.now()
            youth.is_checked_in = False
            youth.save()
    
    set_check_out.short_description = 'Check out'

    filter_horizontal = ()
    list_filter = ()
    fieldsets = ()

admin.site.register(Youth, YouthAdmin)

class FamilyAdmin(admin.ModelAdmin):
    list_display = ('guardian', 'youth', 'guardian_is_active')
    #readonly_fields = ('guardian', 'youth')
    
    filter_horizontal = ()
    list_filter = ()
    fieldsets = ()

admin.site.register(Family, FamilyAdmin)

class PreferenceAdmin(admin.ModelAdmin):
    list_display = ('church_name', 'church_phone', 'open_registration', 'intranet')
    
    filter_horizontal = ()
    list_filter = ()
    fieldsets = ()

admin.site.register(UIPrefs, PreferenceAdmin)

class QrAdmin(admin.ModelAdmin):
    list_display = ('code', 'qr_code', 'creatorid', 'completed', 'createddate')
    readonly_fields = ('code', 'qr_code', 'creatorid')
    
admin.site.register(CheckInQr, QrAdmin)

class CheckinLogAdmin(admin.ModelAdmin):
    list_display = ('youth_first_name', 'youth_last_name', 'last_checkin', 'last_checkout', 'checked_in_by', 'youthid', 'checked_out_by')
    readonly_fields = ('youth_first_name', 'youth_last_name', 'last_checkin', 'last_checkout', 'checked_in_by', 'youthid', 'checked_out_by')

admin.site.register(YouthCheckInLog, CheckinLogAdmin)

admin.site.register(ContactConnect)

admin.site.register(TwilioPrefs)

#class ProductAdmin(admin.ModelAdmin):
#    list_display = ('name', 'price')

#admin.site.register(Product, ProductAdmin)