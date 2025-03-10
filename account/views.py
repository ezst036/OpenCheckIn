from django.contrib import messages
from django.shortcuts import render, redirect
from account.forms import RegistrationForm
from account.models import UIPrefs

def registration_view(request):
    context = {}

    try: #Always return the first available
        preferences = UIPrefs.objects.all().first()
    except Exception as e:
        #Deleted preferences
        print(e)

    #If registration is closed, return to the homepage.
    if not preferences.open_registration:
        return redirect('home')

    if request.POST:
        form = RegistrationForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data.get('email')
            raw_password = form.cleaned_data.get('password')
            account = form.save()
            messages.success(request, f'Account created! Enjoy using Open Check In - Please log in to begin.')
            return redirect('home')
        else:
            context['registration_form'] = form
    else:
        form = RegistrationForm()
        context['registration_form'] = form
    
    return render(request, 'account/register.html', context)