from django.db import models
from django.urls import reverse
from django.utils.timezone import now

missionType = [
    ('new', 'New'),
    ('planned', 'Planned'),
    ('current', 'Current'),
    ('complete', 'Complete'),
    ('supported', 'Supported'),
]

class Event(models.Model):
    name = models.CharField(max_length=200, db_index=True)
    slug = models.SlugField(max_length=200, db_index=True, null=True)
    image = models.ImageField(upload_to='events/%Y/%m/%d', blank=True)
    description = models.TextField(blank=True)
    startdate = models.DateField(default=now)
    enddate = models.DateField(default=now)
    price = models.IntegerField(default=0)
    complete = models.BooleanField(default=False)
    nocost = models.BooleanField(default=False)
    latitude = models.FloatField(default=0)
    longitude = models.FloatField(default=0)
    created = models.DateTimeField(auto_now_add=True, null=True)
    updated = models.DateTimeField(auto_now=True)
    ismission = models.BooleanField(default=False)
    type = models.CharField(verbose_name="Mission type", max_length=24, choices=missionType, default='new')
    
    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse("eventdetail", args=[self.id, self.slug])

    def get_display_price(self):
        #Divide number by 100 to only have dollars shown,
        #return number up by two decimals.
        return "{0:.2f}".format(self.price / 100)

class EventPurchaseLog(models.Model):
    name = models.CharField(max_length=200)
    userAccountid = models.IntegerField(verbose_name="Account number",default=0)
    purchDate = models.DateTimeField(auto_now=True)
    confnum = models.CharField(default="num", max_length=80)

class StripeKeys(models.Model):
    apikeys = models.CharField(max_length=8, default="API keys")
    stripepublic = models.CharField(verbose_name="Stripe Public Key", max_length=150, default="STRIPE_PUBLIC_KEY")
    stripesecret = models.CharField(verbose_name="Stripe Secret Key", max_length=150, default="STRIPE_SECRET_KEY")

    class Meta:
        verbose_name = "Stripe Keys"
        verbose_name_plural = "Stripe Keys"