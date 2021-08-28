import account.models
from django.db.models.signals import pre_save, post_save
import os
from django.dispatch import receiver
from django.conf import settings
from uuid import uuid4

@receiver(pre_save, dispatch_uid='Pre_pre_save')
def remove_old_file(instance, **kwargs):
    try:
        if hasattr(instance, 'email'):
            if instance.profileimage == 'default.png':
                    pass #Should not delete the default jpg file.
            else:
                if instance.profileimage == '/home/user/Public/OpenCheckIn/src/media/default.png' and (instance.image.path != instance.profileimage):
                    #Should not delete the default jpg file.
                    
                    #Need to rename the user's new files
                    ext = instance.image.name.split('.')[-1]
                    filename = instance.username + '_' + '{}.{}'.format(uuid4().hex, ext)
                
                    #Set the file name
                    instance.image.name = filename
                elif os.path.isfile(instance.profileimage) and (instance.image.path != instance.profileimage):
                    os.remove(instance.profileimage)
                
                    #Need to rename the user's new files
                    ext = instance.image.name.split('.')[-1]
                    filename = instance.username + '_' + '{}.{}'.format(uuid4().hex, ext)
                
                    #Set the file name
                    instance.image.name = filename
                
    except Exception as e:
        print(e)

@receiver(post_save, dispatch_uid='logger_method')
def logger_met(sender, instance, **kwargs):
    if kwargs['created'] is False:
        if hasattr(instance, 'email'):
            maxtimestamp = account.models.AccountLoginLog.objects.filter(userEmailAddress=instance.email).values_list('last_login', flat=True).order_by('-last_login').first()
            
            if maxtimestamp == instance.last_login:
                pass
            else:
                newTimestamp = account.models.AccountLoginLog.objects.create(
                    userEmailAddress = instance.email,
                    userAccountid = instance.id,
                    userfirstname = instance.first_name,
                    userlastname = instance.last_name,
                    last_login = instance.last_login
                )