from django.db import models

givingType = [
    ('tithe', 'Tithe'),
    ('offering', 'Offering'),
]

class TitheLog(models.Model):
    userEmailAddress = models.EmailField(verbose_name="Email address", max_length=60)
    userAccountid = models.IntegerField(verbose_name="Account number", blank=True)
    giveAmount = models.IntegerField(default=0)
    givingType = models.CharField(verbose_name="Giving type", max_length=24, choices=givingType, default='tithe')
    giveDate = models.DateTimeField(auto_now=True)

class StripeKeys(models.Model):
    apikeys = models.CharField(max_length=8, default="API keys")
    stripepublic = models.CharField(verbose_name="Stripe Public Key", max_length=150, default="STRIPE_PUBLIC_KEY")
    stripesecret = models.CharField(verbose_name="Stripe Secret Key", max_length=150, default="STRIPE_SECRET_KEY")

    class Meta:
        verbose_name = "Stripe Keys"
        verbose_name_plural = "Stripe Keys"