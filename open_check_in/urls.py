from django.contrib import admin
from django.urls import path
from account.views import registration_view
from django.conf.urls import url
from django.conf import settings
from django.views.static import serve
from django.contrib.auth import views as auth_views
from checkin import views as views_from_checkin

admin.site.site_header = "Open Check In Administration"
admin.site.site_title = "Administration Portal"
admin.site.index_title = "Welcome to Open Check In"

urlpatterns = [
    url(r'^admin/logout/', views_from_checkin.logoff),
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
    url(r'^media/(?P<path>.*)$', serve,{'document_root': settings.MEDIA_ROOT}),
    url(r'^static/(?P<path>.*)$', serve,{'document_root': settings.STATIC_URL}),
    path('ajax/profile/createYouth/', views_from_checkin.ProfileCreateYouth.as_view(), name='ajax_call_createyouth'),
    path('ajax/profile/updateYouth/', views_from_checkin.ProfileUpdateYouth.as_view(), name='ajax_call_updateYouth'),
    path('ajax/profile/deleteYouth/', views_from_checkin.ProfileDeleteYouth.as_view(), name='ajax_call_deleteYouth'),
    path('ajax/checkyouth/staffCheck/', views_from_checkin.StaffCheckInYouth.as_view(), name='ajax_call_staffCheck'),
    path('ajax/checkyouth/camCheck/', views_from_checkin.CamCheck.as_view(), name='ajax_call_camCheck'),
    path('ajax/checkyouth/createQR/', views_from_checkin.createQR.as_view(), name='ajax_call_createQR'),
    path('ajax/checkyouth/guardianPreCheck/', views_from_checkin.GuardianPreCheck.as_view(), name='ajax_call_guardianPreCheck'),
]