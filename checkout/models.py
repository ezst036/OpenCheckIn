from django.db import models
from django.urls import reverse

class Category(models.Model):
    name = models.CharField(max_length=200, db_index=True)
    slug = models.SlugField(max_length=200, unique=True)

    class Meta:
        ordering = ('name',)
        verbose_name = 'category'
        verbose_name_plural = 'categories'
    
    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse("bycategory", args=[self.slug])
    
class Product(models.Model):
    category = models.ForeignKey(Category, related_name='products', on_delete=models.CASCADE, default=True)
    name = models.CharField(max_length=200, db_index=True)
    slug = models.SlugField(max_length=200, db_index=True, null=True)
    image = models.ImageField(upload_to='products/%Y/%m/%d', blank=True)
    description = models.TextField(blank=True)
    price = models.IntegerField(default=0)
    available = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True, null=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ('name',)
        index_together = (('id', 'slug'),)
    
    def __str__(self):
        return self.name
    
    def __getitem__(self,key):
        return getattr(self,key)

    def get_absolute_url(self):
        return reverse("productdetail", args=[self.id, self.slug])

    def get_display_price(self):
        #Divide number by 100 to only have dollars shown,
        #return number up by two decimals.
        return "{0:.2f}".format(self.price / 100)

class StripeKeys(models.Model):
    apikeys = models.CharField(max_length=8, default="API keys")
    stripepublic = models.CharField(verbose_name="Stripe Public Key", max_length=150, default="STRIPE_PUBLIC_KEY")
    stripesecret = models.CharField(verbose_name="Stripe Secret Key", max_length=150, default="STRIPE_SECRET_KEY")

    class Meta:
        verbose_name = "Stripe Keys"
        verbose_name_plural = "Stripe Keys"

#Records final sales
class PurchaseLog(models.Model):
    userAccountid = models.IntegerField(verbose_name="Account number",default=0)
    purchAmount = models.DecimalField(max_digits=15, decimal_places=2)
    purchDate = models.DateTimeField(auto_now=True)
    totalqty = models.IntegerField(default=0)
    confnum = models.CharField(default="num", max_length=80)
    isdelivered = models.BooleanField()

#Records each individual item sold
class ItemPurchaseLog(models.Model):
    prodname = models.CharField(max_length=200)
    prodid = models.IntegerField(default=0)
    prodqty = models.IntegerField(default=0)
    userAccountid = models.IntegerField(verbose_name="Account number",default=0)
    purchDate = models.DateTimeField(auto_now=True)
    confnum = models.CharField(default="num", max_length=80)