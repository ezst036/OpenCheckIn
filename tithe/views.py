from django.contrib import messages
from django.shortcuts import render
import re
from django.utils.timezone import now
import stripe
from account.models import UIPrefs
from . models import TitheLog, StripeKeys

def index(request):
    #Always return the first available
    apikeys = StripeKeys.objects.all().first()

    try:
        stripe.api_key = apikeys.stripepublic
    except Exception as e:
        #Deleted keys
        messages.success(request, f'API keys not yet setup by the administrator.')
    
    try:
        preferences = UIPrefs.objects.all().first()
    except Exception as e:
        print(e)

    context = {
        'preferences': preferences,
        'publickey':stripe.api_key
    }
    
    return render(request, 'tithe/index.html', context)

def charge(request):
    #Always return the first available
    apikeys = StripeKeys.objects.all().first()

    try:
        stripe.api_key = apikeys.stripesecret
    except Exception as e:
        #Deleted keys
        messages.success(request, f'API keys not yet setup by the administrator.')
        request.method = 'GET'
    
    if request.method == 'GET':
        #Go to main page and prevent null data errors
        return render(request, 'tithe/index.html')

    if request.method == 'POST':
        amount = request.POST['amount']
        found = re.findall('[0-9]+', amount)
        submitTotal = int(''.join(found))

        try: #External call outside to Stripe servers
            customer = stripe.Customer.create(
            email=request.POST['email'],
            source=request.POST['stripeToken']
        )
        except Exception as e:
            messages.success(request, f'API keys are expired or incorrect.')
            return render(request, 'tithe/index.html')
        
        charge = stripe.Charge.create(
            customer=customer,
            amount=submitTotal,
            currency='usd',
            description="Donation"
        )

        #Cannot be null
        userAccountid = 0

        if request.user.id != None:
            userAccountid = request.user.id

        #Internal OpenCheckIn logging object
        TitheLog.objects.create(
            userEmailAddress = request.POST['email'],
            userAccountid = userAccountid,
            giveAmount = submitTotal,
            givingType = 'tithe',
            giveDate = now()
        )

        #stripe.Customer.get
    
    return render(request, 'tithe/success.html', {'amount':amount})