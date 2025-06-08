from django.db import models

missionColor = [
    ('white', 'White'),
    ('pink', 'Pink'),
    ('lightgray', 'Light Gray'),
    ('red', 'Red'),
    ('orange', 'Orange'),
    ('purple', 'Purple'),
    ('blue', 'Blue'),
    ('green', 'Green'),
]

class MapPointPrefs(models.Model):
    newPointColor = models.CharField(verbose_name="New point color", max_length=24, choices=missionColor, default='pink')
    newMissionIcon = models.CharField(verbose_name="New mission icon", max_length=40, default='fa-bars', blank=True)
    newIconColor = models.CharField(verbose_name="New icon color", max_length=24, choices=missionColor, default='white')
    plannedPointColor = models.CharField(verbose_name="Planned point color", max_length=24, choices=missionColor, default='lightgray')
    plannedMissionIcon = models.CharField(verbose_name="Planned mission icon", max_length=40, default='fa-bars', blank=True)
    plannedIconColor = models.CharField(verbose_name="Planned icon color", max_length=24, choices=missionColor, default='white')
    currentPointColor = models.CharField(verbose_name="Current point color", max_length=24, choices=missionColor, default='red')
    currentMissionIcon = models.CharField(verbose_name="Current mission icon", max_length=40, default='fa-bars', blank=True)
    currentIconColor = models.CharField(verbose_name="Current icon color", max_length=24, choices=missionColor, default='white')
    completePointColor = models.CharField(verbose_name="Complete point color", max_length=24, choices=missionColor, default='orange')
    completeMissionIcon = models.CharField(verbose_name="Complete mission icon", max_length=40, default='fa-bars', blank=True)
    completeIconColor = models.CharField(verbose_name="Complete icon color", max_length=24, choices=missionColor, default='white')
    supportedPointColor = models.CharField(verbose_name="Supported point color", max_length=24, choices=missionColor, default='purple')
    supportedMissionIcon = models.CharField(verbose_name="Supported mission icon", max_length=40, default='fa-bars', blank=True)
    supportedIconColor = models.CharField(verbose_name="Supported icon color", max_length=24, choices=missionColor, default='white')