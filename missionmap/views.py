from django.shortcuts import render
import folium
from account.models import UIPrefs
from event.models import Event
from missionmap.models import MapPointPrefs
from django.views.decorators.clickjacking import xframe_options_exempt

@xframe_options_exempt
def index(request):
    try:
        basepref = UIPrefs.objects.all()[0]
    except Exception as e:
        basepref = {
            'latitude': '25.036289',
            'longitude': '-77.481326',
            'church_name': 'invalid',
            'church_address': 'invalid',
            'church_phone': 'invalid'
        }
        print(e)
    
    ourmap = folium.Map(location=[basepref.latitude, basepref.longitude], zoom_start=9)

    preferences = UIPrefs.objects.all()
    for pref in preferences:
        #Add church locations
        homeCoords = (pref.latitude, pref.longitude)
        hometooltip = "This is home"
        homeicon = folium.Icon(color='green', icon='fa-bars', icon_color='white', prefix='fa')
        homeframe = folium.IFrame(pref.church_name +
                                ' <a href=https://www.bible.com/>Bible.com</a> <br />' +
                                pref.church_address + '<br />' +
                                pref.church_phone)
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
    colorprefs = MapPointPrefs.objects.all()
    
    if len(colorprefs) == 0:
        #create a simple preference object automatically
        MapPointPrefs.objects.create(
            newPointColor = 'pink', newMissionIcon = 'fa-bars', newIconColor = 'white',
            plannedPointColor = 'lightgray', plannedMissionIcon = 'fa-bars', plannedIconColor = 'white',
            currentPointColor = 'red', currentMissionIcon = 'fa-bars', currentIconColor = 'white',
            completePointColor = 'orange', completeMissionIcon = 'fa-bars', completeIconColor = 'white',
            supportedPointColor = 'purple', supportedMissionIcon = 'fa-bars', supportedIconColor = 'white',
        )
        colorprefs = MapPointPrefs.objects.all() #load new obj for use

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
                    eicon = folium.Icon(color=colorprefs[0].newPointColor, icon=colorprefs[0].newMissionIcon, icon_color=colorprefs[0].newIconColor, prefix='fa')
                if event.type == "planned":
                    etooltip = "Planned hover message"
                    eicon = folium.Icon(color=colorprefs[0].plannedPointColor, icon=colorprefs[0].plannedMissionIcon, icon_color=colorprefs[0].plannedIconColor, prefix='fa')
                if event.type == "current":
                    etooltip = "Current hover message"
                    eicon = folium.Icon(color=colorprefs[0].currentPointColor, icon=colorprefs[0].currentMissionIcon, icon_color=colorprefs[0].currentIconColor, prefix='fa')
                if event.type == "complete":
                    etooltip = "Complete hover message"
                    eicon = folium.Icon(color=colorprefs[0].completePointColor, icon=colorprefs[0].completeMissionIcon, icon_color=colorprefs[0].completeIconColor, prefix='fa')
                if event.type == "supported":
                    etooltip = "Supported hover message"
                    eicon = folium.Icon(color=colorprefs[0].supportedPointColor, icon=colorprefs[0].supportedMissionIcon, icon_color=colorprefs[0].supportedIconColor, prefix='fa')

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