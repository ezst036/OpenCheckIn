from django.shortcuts import render
import folium
from account.models import UIPrefs
from event.models import Event
from . models import Mission

def index(request):
    try:
        preferences = UIPrefs.objects.all()[0]
    except Exception as e:
        preferences = {
            'latitude': '25.036289',
            'longitude': '-77.481326',
            'church_name': 'invalid',
            'church_address': 'invalid',
            'church_phone': 'invalid'
        }
        print(e)
    
    missions = Mission.objects.all()
    ourmap = folium.Map(location=[preferences.latitude, preferences.longitude], zoom_start=9)

    #Add home church location
    homeCoords = (preferences.latitude, preferences.longitude)
    hometooltip = "This is home"
    homeicon = folium.Icon(color='green', icon='fa-bars', prefix='fa')
    homeframe = folium.IFrame('Home: ' + preferences.church_name +
                              ' <a href=https://www.bible.com/>Bible.com</a> <br />' +
                              preferences.church_address + '<br />' +
                              preferences.church_phone)
    homepopup = folium.Popup(homeframe, min_width=300, max_width=300)
    folium.Marker(homeCoords,
                  tooltip=hometooltip,
                  icon=homeicon,
                  popup=homepopup).add_to(ourmap)

    if len(missions) > 0:
        for mission in missions:
            mcoordinates = (mission.latitude, mission.longitude)
            mtooltip = "Hover message"
            micon = folium.Icon(color='lightgray', icon='fa-bars', prefix='fa')
            miframe = folium.IFrame('Mission name: ' + str(mission.location) + ' <a href=https://www.bible.com/>Bible.com</a>')
            mpopup = folium.Popup(miframe, min_width=300, max_width=300)

            folium.Marker(mcoordinates,
                        tooltip=mtooltip,
                        icon=micon,
                        popup=mpopup).add_to(ourmap)
    
    events = Event.objects.all()

    #Make events optional?
    if len(events) > 0:
        for event in events:
            ecoordinates = (event.latitude, event.longitude)
            etooltip = "Hover message"
            eicon = folium.Icon(color='blue', icon='fa-bars', prefix='fa')
            eiframe = folium.IFrame('Event name: ' + str(event.name))
            epopup = folium.Popup(eiframe, min_width=300, max_width=300)

            folium.Marker(ecoordinates,
                        tooltip=etooltip,
                        icon=eicon,
                        popup=epopup).add_to(ourmap)
    
    if request.path == '/fullscreenmap/':
        #Fullscreen does not inherit from the base, otherwise it is the same
        return render(request, 'missionmap/fullscreen.html', { 'map': ourmap._repr_html_() })

    return render(request, 'missionmap/index.html', { 'map': ourmap._repr_html_(), 'preferences': preferences } )
