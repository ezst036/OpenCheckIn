from django.shortcuts import get_object_or_404, render, redirect
from account.models import UIPrefs
from checkout.forms import CartForm
from . cart import ShoppingCart
from . models import Category, Product, StripeKeys, PurchaseLog, ItemPurchaseLog
from django.views.decorators.http import require_POST
import stripe
from django.views.generic import TemplateView
from django.utils.timezone import now
import uuid
from django.contrib import messages

def LandingPageView(request):
    return render(request, 'checkout/home.html')

@require_POST
def addtocart(request, productid):
    cart=ShoppingCart(request)
    product = get_object_or_404(Product, id=productid)
    form = CartForm(request.POST)
    if form.is_valid():
        cd = form.cleaned_data
        cart.add(product=product, quantity=cd['quantity'], update_quantity=cd['override'])
    
    return redirect('cartdetails')

def removefromcart(request, productid):
    cart=ShoppingCart(request)
    product = get_object_or_404(Product, id=productid)
    cart.remove(product)
    return redirect('cartdetails')

def cartdetails(request):
    enablecontinue = True
    apikeys = StripeKeys.objects.all().first()

    try: #Checkout button disabled if stripe keys null or default values
        stripe.api_key = apikeys.stripesecret
        
        if (apikeys.stripesecret == 'STRIPE_PUBLIC_KEY' or
            apikeys.stripepublic == 'STRIPE_SECRET_KEY'):
            enablecontinue = False
            #Preference exists but not setup
            messages.success(request, f'API keys are improperly configured, please contact an administrator. Transaction disabled.')
    except Exception as e:
        messages.success(request, f'API keys not yet setup by the administrator. Transaction disabled.')
        enablecontinue = False
    
    try:
        preferences = UIPrefs.objects.all().first()
    except Exception as e:
        print(e)

    totalprice=0
    cart=ShoppingCart(request)
    for item in cart:
        item['update_quantity_form'] = CartForm(initial={'quantity':item['quantity'], 'override':True})
        totalprice+=item['price']
    
    if totalprice <= 0:
        messages.success(request, f'Total price of all items equals zero. Transaction disabled.')
        enablecontinue = False
    
    context = {
        'preferences': preferences,
        'cart':cart,
        'enablecontinue':enablecontinue
    }

    return render(request, 'checkout/shoppingcart.html', context)

def productlist(request, categoryslug=None):
    try: #Always return the first available
        preferences = UIPrefs.objects.all().first()
    except Exception as e:
        #Deleted preferences
        print(e)

    #If registration is closed, return to the homepage or if a database does not exist yet
    if preferences is None:
        return redirect('home')
    elif not preferences.store:
        return redirect('home')

    category = None
    categories = Category.objects.all()
    products = Product.objects.filter(available=True)
    if categoryslug:
        category = get_object_or_404(Category, slug=categoryslug)
        products = products.filter(category=category)
    
    context = {
        'preferences': preferences,
        'category':category,
        'categories':categories,
        'products':products
    }

    return render(request, 'checkout/list.html', context)

def productdetail(request, id, slug):
    try:
        preferences = UIPrefs.objects.all().first()
    except Exception as e:
        print(e)

    product=get_object_or_404(Product, id=id, slug=slug, available=True)
    cart_product_form = CartForm()
    product.price=product.price / 100

    context = {
        'preferences': preferences,
        'product':product,
        'cart_product_form':cart_product_form
    }

    return render(request, 'checkout/detail.html', context)

class MainView(TemplateView):
    template_name = "checkout/revieworder.html"
    
    def get_context_data(self, **kwargs):
        # apikeys null check above in cartdetails function
        apikeys = StripeKeys.objects.all().first()      
        stripe.api_key = apikeys.stripesecret

        total_price_in_cart=0
        total_decimal = 0

        cart=ShoppingCart(self.request)
        for item in cart:
            itemprice = (item['price'] * item['quantity'])
            total_decimal+=((item['price'] * item['quantity']) / 100)
            total_price_in_cart+=itemprice
            item['update_quantity_form'] = CartForm(initial={'quantity':item['quantity'], 'override':True})

        context = super().get_context_data(**kwargs)
        context['key'] = apikeys.stripepublic
        context.update({
            "viewamount": total_decimal, #User will see a normal dollar and cents amount
            "payamount": total_price_in_cart, #Stripe counts in pennies for payment
            #"products": products, #provide products to loop through and display for review
            "STRIPE_PUBLIC_KEY": apikeys.stripepublic,
        })
        return context

def paycharge(request):
    #Avoid potential empty cart errors by redirecting to the shopping
    #cart page if the user has accidentally navigated to this url
    if request.method == "GET":
        return render(request, 'checkout/shoppingcart.html')

    if request.method == "POST":
        total_price_in_cart=0

        cart=ShoppingCart(request)
        for item in cart:
            total_price_in_cart+=(item['price'] * item['quantity'])
            item['update_quantity_form'] = CartForm(initial={'quantity':item['quantity'], 'override':True})

        #newcustomer = stripe.Customer.create(
        #    email=request.user.email,
        #)

        #existcustomer = stripe.Customer.retrieve("cus_1234567890")

        charge = stripe.Charge.create(
            amount=total_price_in_cart,
            #customer=newcustomer,
            currency='usd',
            description='Pay gateway test',
            source=request.POST['stripeToken'],
        )

        return redirect('complete')

class SuccessView(TemplateView):
    def get_context_data(self, **kwargs):
        cart=ShoppingCart(self.request)
        purchaseuuid = uuid.uuid4()

        userAccountid = 0
        try: #If no user logged in
            userAccountid = self.request.user.id
        except Exception as e:
            userAccountid = 0 #re-set

        qtycounter = 0
        totalamount = 0

        for item in cart: #Purchase complete.  The cart should be emptied at the end.
            iterable = item.get('product')

            #Add an entry to the item log
            ItemPurchaseLog.objects.create(
                prodname = iterable['name'],
                prodid = iterable['id'],
                prodqty = item['quantity'],
                userAccountid = userAccountid,
                purchDate = now(),
                confnum = purchaseuuid
            )

            qtycounter += item['quantity']
            totalamount += item['total_price']

            #Set the item quantity to 1 and remove
            item['quantity'] = 1
            cart.remove(item['product'])

        #Add an entry to the purchase log table
        PurchaseLog.objects.create(
            userAccountid = 0,
            purchAmount = totalamount,
            purchDate = now(),
            totalqty = qtycounter,
            confnum = purchaseuuid,
            isdelivered = False
        )

        context = super().get_context_data(**kwargs)
        context['confnum'] = purchaseuuid
        return context

    template_name = "checkout/success.html"

class CancelView(TemplateView):
    template_name = "checkout/cancel.html"

#stripe.Refund.create(
#  charge="ch_1Iz940I2uNlTtwfFU5BcMuzR",
#)

#stripe.Subscription.create(
#  customer="cus_MNfvV0nWzzAMb3",
#  items=[
#    {"price": "price_1LeuZII2uNlTtwfFkt4iqXi9"},
#  ],
#)