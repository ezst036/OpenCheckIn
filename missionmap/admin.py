from django.contrib import admin
from .models import MapPointPrefs

@admin.register(MapPointPrefs)
class MapPointPrefsAdmin(admin.ModelAdmin):
   list_display = ['newPointColor', 'newMissionIcon', 'newIconColor',
                   'plannedPointColor', 'plannedMissionIcon', 'plannedIconColor',
                   'currentPointColor', 'currentMissionIcon', 'currentIconColor',
                   'completePointColor', 'completeMissionIcon', 'completeIconColor',
                   'supportedPointColor', 'supportedMissionIcon', 'supportedIconColor',
                   ]