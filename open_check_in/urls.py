from django.contrib import admin
from django.urls import path, re_path
from account.views import registration_view
from django.conf import settings
from django.views.static import serve
from django.contrib.auth import views as auth_views
from checkin import views as views_from_checkin
from connect.views import connectview
from connect.admin import connectadmin
from tithe import views as titheview
from checkout import views as checkoutview
from event import views as event_views
from missionmap import views as mission_views

admin.site.site_header = "Open Check In Administration"
admin.site.site_title = "Administration Portal"
admin.site.index_title = "Welcome to Open Check In"

urlpatterns = [
    re_path(r'^admin/logout/', views_from_checkin.logoff),
    path('admin/', admin.site.urls),
    path('', views_from_checkin.home_screen_view, name="home"),
    path('test/', views_from_checkin.test_view, name="test"),
    path('checkyouth/', views_from_checkin.staff_check_youths, name="check"),
    path('register/', registration_view, name="register"),
    path('profile/', views_from_checkin.profile, name="profile"),
    path('login/', auth_views.LoginView.as_view(template_name='checkin/login.html'), name='login'),
    #path('login/', views_from_checkin.login, name="login"),
    path('logout/', auth_views.LogoutView.as_view(template_name="checkin/logout.html", next_page=None), name='logout'),
    path('smalllogin/', auth_views.LoginView.as_view(template_name='checkin/smalllogin.html'), name='smalllogin'),
    path('passwordchange', views_from_checkin.PasswordChange.as_view(template_name='checkin/passwordchangeform.html'), name='passwordchange'),
    path('passwordchangecomplete', views_from_checkin.passwordChangeComplete, name='passwordchangecomplete'),
    re_path(r'^media/(?P<path>.*)$', serve,{'document_root': settings.MEDIA_ROOT}),
    re_path(r'^static/(?P<path>.*)$', serve,{'document_root': settings.STATIC_URL}),
    path('ajax/profile/createYouth/', views_from_checkin.ProfileCreateYouth.as_view(), name='ajax_call_createyouth'),
    path('ajax/profile/updateYouth/', views_from_checkin.ProfileUpdateYouth.as_view(), name='ajax_call_updateYouth'),
    path('ajax/profile/deleteYouth/', views_from_checkin.ProfileDeleteYouth.as_view(), name='ajax_call_deleteYouth'),
    path('ajax/checkyouth/staffCheck/', views_from_checkin.StaffCheckInYouth.as_view(), name='ajax_call_staffCheck'),
    path('ajax/checkyouth/camCheck/', views_from_checkin.CamCheck.as_view(), name='ajax_call_camCheck'),
    path('ajax/checkyouth/createQR/', views_from_checkin.createQR.as_view(), name='ajax_call_createQR'),
    path('ajax/checkyouth/guardianPreCheck/', views_from_checkin.GuardianPreCheck.as_view(), name='ajax_call_guardianPreCheck'),
    path('ajax/profile/homeLocation/', views_from_checkin.HomeLocation.as_view(), name='ajax_set_homeLocation'),
    path('missions/', mission_views.index, name='missionmap'),
    path('fullscreenmap/', mission_views.index, name='fullscreenmap'),
    path('paycharge/', checkoutview.paycharge, name='paycharge'),    
    path('connect/', connectview, name='digitalconnect'),
    path('connectadmin/', connectadmin.urls),
    path('tithe/', titheview.index, name='tithe'),
    path('charge/', titheview.charge, name='charge'),
    path('detail/', checkoutview.cartdetails, name='cartdetails'),
    path('add/<int:productid>/', checkoutview.addtocart, name='addtocart'),
    path('remove/<int:productid>/', checkoutview.removefromcart, name='removefromcart'),
    path('store/<int:id>/<slug:slug>/', checkoutview.productdetail, name='productdetail'),
    path('revieworder/', checkoutview.MainView.as_view(), name='revieworder'),
    path('complete/', checkoutview.SuccessView.as_view(), name='complete'),
    path('cancel/', checkoutview.CancelView.as_view(), name='cancel'),
    path('reviewevent/', event_views.reviewConfirm, name='reviewevent'),
    path('chargeevent/', event_views.chargeEvent, name='chargeevent'),
    path('eventlist/', event_views.eventlist, name='eventlist'),
    path('list/', checkoutview.productlist, name='productlist'),
    path('event/<int:id>/<slug:slug>/', event_views.eventdetail, name='eventdetail'),
    path('<slug:categoryslug>/', checkoutview.productlist, name='bycategory'),
]