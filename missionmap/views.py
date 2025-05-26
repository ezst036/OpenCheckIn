from django.shortcuts import render
import folium
from account.models import UIPrefs
from event.models import Event
from django.views.decorators.clickjacking import xframe_options_exempt

@xframe_options_exempt
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
    
    ourmap = folium.Map(location=[preferences.latitude, preferences.longitude], zoom_start=9)

    #Add home church location
    homeCoords = (preferences.latitude, preferences.longitude)
    hometooltip = "This is home"
    homeicon = folium.Icon(color='green', icon='fa-bars', icon_color='white', prefix='fa')
    homeframe = folium.IFrame('Home: ' + preferences.church_name +
                              ' <a href=https://www.bible.com/>Bible.com</a> <br />' +
                              preferences.church_address + '<br />' +
                              preferences.church_phone)
    homepopup = folium.Popup(homeframe, min_width=300, max_width=300)
    folium.Marker(homeCoords,
                  tooltip=hometooltip,
                  icon=homeicon,
                  popup=homepopup).add_to(ourmap)

    # if len(missions) > 0:
    #     for mission in missions:
    #         mcoordinates = (mission.latitude, mission.longitude)
    #         mtooltip = "Hover message"
    #         micon = folium.Icon(color='lightgray', icon='fa-bars', prefix='fa')
    #         miframe = folium.IFrame('Mission name: ' + str(mission.location) + ' <a href=https://www.bible.com/>Bible.com</a>')
    #         mpopup = folium.Popup(miframe, min_width=300, max_width=300)

    #         folium.Marker(mcoordinates,
    #                     tooltip=mtooltip,
    #                     icon=micon,
    #                     popup=mpopup).add_to(ourmap)
    
    events = Event.objects.all()

    if len(events) > 0:
        for event in events:
            if event.ismission == True:
                #ecoordinates, frame, and popup are all the same for all missions.
                ecoordinates = (event.latitude, event.longitude)
                eiframe = folium.IFrame('Event name: ' + str(event.name))
                epopup = folium.Popup(eiframe, min_width=300, max_width=300)

                #FontAwesome icons are configurable, find icons at fontawesome.com
                if event.type == "new":
                    etooltip = "New hover message"
                    eicon = folium.Icon(color='pink', icon='fa-cloud', icon_color='white', prefix='fa')
                if event.type == "planned":
                    etooltip = "Planned hover message"
                    eicon = folium.Icon(color='lightgray', icon='fa-cloud', icon_color='lightblue', prefix='fa')
                if event.type == "current":
                    etooltip = "Current hover message"
                    eicon = folium.Icon(color='red', icon='fa-circle-dot', icon_color='white', prefix='fa')
                if event.type == "complete":
                    etooltip = "Complete hover message"
                    eicon = folium.Icon(color='orange', icon='fa-border-none', icon_color='orange', prefix='fa')
                if event.type == "supported":
                    etooltip = "Supported hover message"
                    eicon = folium.Icon(color='purple', icon='fa-bell', icon_color='white', prefix='fa')

                #Add the marker after it is configured.
                folium.Marker(ecoordinates,
                            tooltip=etooltip,
                            icon=eicon,
                            popup=epopup).add_to(ourmap)

            else: #Non-mission events use the color blue
                ecoordinates = (event.latitude, event.longitude)
                etooltip = "Hover message"
                eicon = folium.Icon(color='blue', icon='fa-bars', icon_color='white', prefix='fa')
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
