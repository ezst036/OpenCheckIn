from django.shortcuts import render, redirect
from account.models import UIPrefs
from .models import TwilioPrefs
from .forms import ConnectForm
from django.contrib import messages
from twilio.rest import Client

def connectview(request):
    if request.method == 'GET':
        #Pre-populate user information in the new form
        if request.user.is_authenticated:
            if len(request.user.first_name) < 1 or len(request.user.last_name) < 1:
                messages.success(request, f'Your user profile is incomplete.  Username and email were filled in.')
                form = ConnectForm(initial={
                    'first_name': request.user.username,
                    'last_name': request.user.email
                })
            else:
                form = ConnectForm(initial={
                    'first_name': request.user.first_name,
                    'last_name': request.user.last_name
                })
    
    if request.method == 'POST':
        #Receive filled out form from user
        form = ConnectForm(request.POST)
        if form.is_valid():
            sendmessage = True

            try:
                prefs = TwilioPrefs.objects.all()[0]
            except IndexError:
                sendmessage = False
                messages.success(request, f'Messaging is not configured, please contact an administrator.')
            
            #Should not send notifications for new member Connect messages
            #Confirm default sid and token information to prevent errors
            if form.cleaned_data['messagetype'] == 'prayer' and sendmessage == True:

                if not (prefs.acctsid == 'TWILIO_ACCOUNT_SID' or
                    prefs.accttoken == 'TWILIO_AUTH_TOKEN'):

                    firstname = form.cleaned_data['first_name']
                    lastname = form.cleaned_data['last_name']
                    title = form.cleaned_data['title']
                    usermessage = form.cleaned_data['title']
                
                    client = Client(prefs.acctsid, prefs.accttoken)
                    #send text message to phone with Twilio
                    message = client.messages.create(
                                                body=f'message sent from: - {firstname} {lastname} - {title} - {usermessage}',
                                                from_=prefs.accountnumber,
                                                to=prefs.recipientnumber
                                            )

                    print(message.sid)
                else: messages.success(request, f'Messaging keys are not configured, please contact an administrator.')

            else: messages.success(request, f'Your message has been received and will be reviewed by the Prayer Team.')
            
            form.save()
            return redirect('home')
    
    #Blank form for users who are not logged in
    if not request.user.is_authenticated:
        form = ConnectForm()
    
    try:
        preferences = UIPrefs.objects.all().first()
    except Exception as e:
        print(e)

    context = {
        'preferences': preferences,
        'form': form
    }
    
    return render(request, 'form.html', context)