from django.shortcuts import get_object_or_404, render
import stripe
from account.models import UIPrefs
from . models import Event, StripeKeys, EventPurchaseLog
from django.contrib import messages
from . forms import EventForm, AccountVerificationForm
from django.utils.timezone import now
import shortuuid
from geopy.geocoders import Nominatim

def reviewConfirm(request):
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
        event = Event.objects.filter(complete=False)
    
        return render(request, 'event/listcontainer.html', {'events':event})

   if request.method == "POST":
        #get item information
        event = Event.objects.get(id=request.POST['item_id'])

        try:
            preferences = UIPrefs.objects.all().first()
        except IndexError as e:
            print(e)

        if request.user.is_authenticated:
            #Display user's information
            userform = AccountVerificationForm(initial={
                        'email': request.user.email,
                        'first_name': request.user.first_name,
                        'last_name': request.user.last_name,
                        'phone_number': request.user.phone_number,
                        'address': request.user.address,
                        'city': request.user.city,
                        'state': request.user.state,
                    })
            
            userform.fields['email'].disabled = True
        else:
            #blank form
            userform = AccountVerificationForm()
        
        #Event information
        payform = EventForm(initial={
                     'name': event.name,
                     'description': event.description,
                     'price': event.get_display_price
                 })
        
        payform.fields['name'].disabled = True
        payform.fields['description'].disabled = True
        payform.fields['price'].disabled = True

        context = {
            'preferences': preferences,
            'payform': payform,
            "STRIPE_PUBLIC_KEY": apikeys.stripepublic,
            'userform': userform,
            'event':event
        }
        
        return render(request, 'event/reviewevent.html', context)


        # amount = int(request.POST["amount"]) 

        # customer = stripe.Customer.create(
        #     email=request.POST.get("email"),
        #     name=request.POST.get("full_name"),
        #     description="item name",
        #     source=request.POST['stripeToken']
        # )

        # charge = stripe.Charge.create(
        #         customer=customer,
        #             amount=amount,
        #             currency='usd',
        #             description=""
        #         ) 
        # transRetrieve = stripe.Charge.retrieve(
        #             charge["id"],
        #             api_key="key"
        #         )
        # charge.save()
        #return redirect("pay_success/")
   


def chargeEvent(request):
    if request.method == 'POST':
        event = Event.objects.get(id=request.POST['item_id'])

        #Do not contact Stripe for no cost events
        if event.nocost == False:
            charge = stripe.Charge.create(
                amount = request.POST['item_price'],
                currency='usd',
                description=request.POST['item_name'],
                source=request.POST['stripeToken'],
            )

        #Acct. ID cannot be null
        userAccountid = 0
        eventuuid = shortuuid.uuid()

        if request.user.id != None:
            userAccountid = request.user.id

        #Internal OpenCheckIn logging object
        #No cost events also need to be logged
        EventPurchaseLog.objects.create(
            name = request.POST['item_name'],
            userAccountid = userAccountid,
            purchDate = now(),
            confnum = eventuuid
        )

        return render(request, 'event/charge.html', {'eventconfirmation':eventuuid, 'event':event})

def eventlist(request):
    try:
        preferences = UIPrefs.objects.all().first()
    except Exception as e:
        print(e)

    context = {
        'preferences': preferences,
        'events': Event.objects.filter(complete=False)
    }
    
    return render(request, 'event/listcontainer.html', context)

def eventdetail(request, id, slug):
    userAgentVal = ''

    try:
        preferences = UIPrefs.objects.all().first()
        userAgentVal = preferences.mapidentification
    except Exception as e:
        print(e)
    
    event = get_object_or_404(Event, id=id, slug=slug, complete=False)
    
    if request.method == 'POST':
        if userAgentVal == '':
            messages.success(request, f'Map identification field incorrect, please enter your church name followed by an email address.')
        else:
            geolocator = Nominatim(user_agent=userAgentVal)
            location = geolocator.geocode(request.POST.get('location', None))
            if location.latitude == None or location.longitude == None:
                messages.success(request, f'Nothing was found using this search term.')
            else:
                event.latitude = location.latitude
                event.longitude = location.longitude
                event.save()

    context = {
        'preferences': preferences,
        'product':event,
        'latitude': event.latitude,
        'longitude': event.longitude
    }

    #Event price has to be modified after the event.save() otherwise it changes the value in the database.
    event.price = event.price / 100
    return render(request, 'event/detail.html', context)