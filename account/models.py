from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from phone_field import PhoneField
from datetime import datetime
from django.db.models.signals import pre_save, post_save
from checkin.signals import remove_old_file, logger_met
import qrcode
from io import BytesIO
from django.core.files import File
from PIL import Image, ImageDraw

class MyAccountManager(BaseUserManager):
	def create_user(self, email, username, password=None):
		if not email:
			raise ValueError('Users must have an email address')
		if not username:
			raise ValueError('Users must have a username')

		user = self.model(
			email=self.normalize_email(email),
			username=username,
		)

		user.set_password(password)
		user.save(using=self._db)
		return user

	def create_superuser(self, email, username, password):
		user = self.create_user(
			email=self.normalize_email(email),
			password=password,
			username=username,
		)
		user.is_admin = True
		user.is_staff = True
		user.is_superuser = True
		user.save(using=self._db)
		return user

class Account(AbstractBaseUser):
    email = models.EmailField(verbose_name="email",
		max_length=60, unique=True)
    username = models.CharField(max_length=100, unique=True)
    first_name = models.CharField(verbose_name="First Name", max_length=255, blank=True)
    middle_name = models.CharField(verbose_name="Middle Name", max_length=255, blank=True)
    last_name = models.CharField(verbose_name="Last Name", max_length=255, blank=True)
    phone_number = PhoneField(blank=True, help_text='Contact phone number')
    address = models.CharField(max_length=255, blank=True)
    city = models.CharField(max_length=60, blank=True)
    state = models.CharField(max_length=60, blank=True)
    is_parent = models.BooleanField(verbose_name="Parent", default=False)
    is_volunteer = models.BooleanField(verbose_name="Volunteer", default=False)
    is_missionary = models.BooleanField(verbose_name="Missionary", default=False)
    is_pastor = models.BooleanField(verbose_name="Pastor", default=False)
    is_admin = models.BooleanField(verbose_name="Administrator", default=False)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(verbose_name="Staff", default=False)
    is_superuser = models.BooleanField(verbose_name="Superuser", default=False)
    date_joined = models.DateTimeField(verbose_name='date joined', auto_now_add=True)
    last_login = models.DateTimeField(verbose_name='last login', auto_now=True)
    image = models.ImageField(default='default.png', upload_to='profile_pics')
    profileimage = models.TextField(default='default.png')
    youth = models.ManyToManyField('Youth', through='Family')

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    objects = MyAccountManager()

    def __str__(self):
        return self.first_name + ' ' + self.middle_name + ' ' + self.last_name

    def has_perm(self, perm, obj=None):
        return self.is_admin

    def has_module_perms(self, app_label):
        return True

#Call the signal to remove old picture file
pre_save.connect(remove_old_file, sender=Account)
post_save.connect(logger_met, sender=Account)

class AccountLoginLog(models.Model):
    userEmailAddress = models.EmailField(verbose_name="Email address", max_length=60)
    userAccountid = models.IntegerField(verbose_name="Account number",default=0)
    userfirstname = models.CharField(verbose_name="First Name", max_length=255, blank=True)
    userlastname = models.CharField(verbose_name="Last Name", max_length=255, blank=True)
    last_login = models.DateTimeField(verbose_name='Last login', auto_now=False)

class Youth(models.Model):
    youth_first_name = models.CharField(verbose_name="First Name", max_length=255, blank=True)
    youth_middle_name = models.CharField(verbose_name="Middle Name", max_length=255, blank=True)
    youth_last_name = models.CharField(verbose_name="Last Name", max_length=255, blank=True)
    youth_birth_day = models.DateField(verbose_name="Birthday", default=datetime.now)
    date_joined = models.DateTimeField(verbose_name='date joined', default=datetime.now)
    last_checkin = models.DateTimeField(verbose_name='last checkin', default=datetime.now)
    last_checkout = models.DateTimeField(verbose_name='last checkout', default=datetime.now)
    pre_check = models.BooleanField(default=False)
    is_checked_in = models.BooleanField(default=False)
    famlink_guardian = models.ManyToManyField(Account, related_name='users_account', through='Family', verbose_name="Guardian")
    image = models.ImageField(default='default.png', upload_to='profile_pics')

    def __str__(self):
        return self.youth_first_name + ' ' + self.youth_last_name

class Family(models.Model):
    guardian = models.ForeignKey(Account, on_delete=models.CASCADE)
    youth = models.ForeignKey('Youth', on_delete=models.CASCADE)
    guardian_is_active = models.BooleanField(default=True)

class YouthCheckInLog(models.Model):
    youth_first_name = models.CharField(verbose_name="First Name", max_length=255, blank=True)
    youth_last_name = models.CharField(verbose_name="Last Name", max_length=255, blank=True)
    youthid = models.IntegerField(verbose_name="Account number",default=0)
    checked_in_by = models.IntegerField(verbose_name="Checked in by",default=0)
    last_checkin = models.DateTimeField(verbose_name='last checkin')
    last_checkout = models.DateTimeField(verbose_name='last checkout', null=True, blank=True)
    checked_out_by = models.IntegerField(verbose_name="Checked out by", null=True, blank=True)

class UIPrefs(models.Model):
    church_name = models.CharField(verbose_name="Church Name", max_length=255, default="Open Check In")
    church_phone = models.CharField(verbose_name="Church Phone Number", max_length=16, default="+1-550-555-1234")
    church_address = models.CharField(verbose_name="Church Address", max_length=255, default="123 street place")
    church_postal_code = models.CharField(verbose_name="Postal code", max_length=25, default="99999-9999")
    show_address_two = models.BooleanField(verbose_name="Show more address", default=False)
    church_address_two = models.CharField(verbose_name="Church Address two", max_length=255, default="Optional lot number")
    open_registration = models.BooleanField(verbose_name="Open registration", default=True)
    intranet = models.BooleanField(verbose_name="Intranet login", default=True)
    main_background = models.ImageField(default='crosses.jpg')
    enable_qr = models.BooleanField(default=True)
    map = models.BooleanField(verbose_name="Enable map", default=True)
    latitude = models.CharField(verbose_name="Latitude", max_length=20, default="25.036289")
    longitude = models.CharField(verbose_name="Longitude", max_length=20, default="-77.481326")
    latzoom = models.CharField(verbose_name="Latitude zoom", max_length=20, default="25.054631")
    lonzoom = models.CharField(verbose_name="Longitude zoom", max_length=20, default="-77.458766")
    enable_marker = models.BooleanField(verbose_name="Enable map marker", default=True)
    latmarker = models.CharField(verbose_name="Latitude marker", max_length=20, default="25.045844")
    lonmarker = models.CharField(verbose_name="Longitude marker", max_length=20, default="-77.470222")
    mapheight = models.CharField(verbose_name="Map height", max_length=20, default="400")
    mapwidth = models.CharField(verbose_name="Map width", max_length=20, default="600")

    class Meta:
        verbose_name = "UI Preference"
        verbose_name_plural = "Preferences"

class CheckInQr(models.Model):
    code = models.CharField(max_length=200)
    qr_code = models.ImageField(upload_to='qrcodes', blank=True)
    creatorid = models.IntegerField(verbose_name="Created by user",default=0)
    completed = models.BooleanField(default=False)
    createddate = models.DateTimeField(verbose_name='Date created', auto_now=True)

    def __str__(self):
        return str(self.code)

    def save(self, *args, **kwargs):
        qrcode_img = qrcode.make(self.code)
        canvas = Image.new('RGB', (325, 325), 'white')
        canvas.paste(qrcode_img)
        filename = f'qr_code-{self.code}.png'
        buffer = BytesIO()
        canvas.save(buffer,'PNG')
        self.qr_code.save(filename, File(buffer), save=False)
        canvas.close()
        super().save(*args, **kwargs)