from django.db import models

messagetypes = [
    ('newmember', 'New member'),
    ('prayer', 'Prayer request'),
]

class TwilioPrefs(models.Model):
    acctsid = models.CharField(verbose_name="Twilio SID", max_length=100, default="TWILIO_ACCOUNT_SID")
    accttoken = models.CharField(verbose_name="Authorization token", max_length=100, default="TWILIO_AUTH_TOKEN")
    accountnumber = models.CharField(verbose_name="Your Twilio number", max_length=40, default="+15017122661")
    recipientnumber = models.CharField(verbose_name="Message recipients", max_length=200, default="+15558675310")

class ContactConnect(models.Model):
    title=models.CharField(max_length=100)
    body=models.TextField()
    messagetype = models.CharField(max_length=24, choices=messagetypes, default='newmember')
    first_name = models.CharField(verbose_name="First Name", max_length=255, blank=True)
    last_name = models.CharField(verbose_name="Last Name", max_length=255, blank=True)
    userAccountid = models.IntegerField(verbose_name="Account number",default=0)

    def __str__(self):
        return self.title
    
    def save(self, *args, **kwargs):
        #try:
        #    prefs = TwilioPrefs.objects.all()[0]
        #except IndexError:
        #    self.messagetype = 'newmember'
        
        #Should not send notifications for new member Connect messages
        #Confirm default sid and token information to prevent errors
        #if self.messagetype == 'prayer':

            #if not (prefs.acctsid == 'TWILIO_ACCOUNT_SID' or 
                #prefs.accttoken == 'TWILIO_AUTH_TOKEN'):
            
                #client = Client(prefs.acctsid, prefs.accttoken)
                #message = client.messages.create(
                #                            body=f'message sent from: - {self.first_name} {self.last_name} - {self.title} - {self.body}',
                #                            from_=prefs.accountnumber,
                #                            to=prefs.recipientnumber
                #                        )

                #print(message.sid)

        return super().save(*args, **kwargs)