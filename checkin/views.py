from django.shortcuts import render, redirect
from account.models import Account, Family, Youth, UIPrefs, YouthCheckInLog, CheckInQr
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from account.forms import RegistrationForm, ProfileUpdateForm, UploadForm
from django.contrib import messages
from django.views.generic import View
from django.http import JsonResponse, HttpResponse
from django.db.models import Q
from django.utils.timezone import now
import cv2
from pyzbar.pyzbar import decode
import time
import warnings
from urllib.parse import unquote_plus
import json

def login(request):
    if request.method == 'POST':
        pass #Need to add a logging object for users

    return render(request, 'checkin/login.html')

def home_screen_view(request):
    try:
        preferred = UIPrefs.objects.all()[0]
    except IndexError:
        preferred = {
            'church_name': 'Open Check In'
        }

    context = {
        'preferences': preferred,
    }
    
    return render(request, 'checkin/home.html', context)

@login_required
def staff_check_youths(request):
    youts = Youth.objects.all()

    context = {
        'youts': youts
    }

    #If account isn't properly credentialed, return to the homepage.
    if not request.user.is_staff:
        return redirect('home')

    return render(request, 'checkin/staffcheckin.html', context)

#Admin logoff control
def logoff(request):
    logout(request)
    return render(request, 'checkin/logout.html')

@login_required
def profile(request):
    if request.method == 'POST':
        p_form = ProfileUpdateForm(request.POST,
            request.FILES, instance=request.user)
        if p_form.is_valid():
            p_form.save()

            #Setup for deleting old image file.  TODO: Re-write this process.
            #Update profileimage field in the database
            request.user.profileimage = request.user.image.path
            p_form.save()
            messages.success(request, f'Your account has been updated!')
            return redirect('profile')
    else:
        p_form = ProfileUpdateForm(instance=request.user)
        fams = Family.objects.all()
        youts = Youth.objects.all()

        obj = None

        try:
            obj = CheckInQr.objects.filter(creatorid=request.user.id).latest('createddate')
        except Exception as e:
            print(e)
        
        if obj is None:
            obj = {
                'code':"newcode",
                'qr_code':"",
                'completed':"True"
            }        

    context = {
        'obj' : obj,
        'p_form': p_form,
        'fams': fams,
        'youts': youts
    }
    return render(request, 'checkin/profile.html', context)

#Ajax
class ProfileCreateYouth(View):
    def post(self, request):
        form = UploadForm(request.POST or None, request.FILES or None)
        youthfn = request.POST.get('youth_first_name', None)
        youthmn = request.POST.get('youth_middle_name', None)
        youthln = request.POST.get('youth_last_name', None)
        youthimg = request.FILES['image']

        obj = Youth.objects.create(
            youth_first_name = youthfn,
            youth_middle_name = youthmn,
            youth_last_name = youthln,
            image = youthimg
        )

        #Register new youth in the Family table
        famobj = Family.objects.create(
            guardian_id = request.user.id,
            youth_id = obj.id,
            guardian_is_active = '1'
        )

        youth = {
            'id':obj.id,
            'youth_first_name':obj.youth_first_name,
            'youth_middle_name':obj.youth_middle_name,
            'youth_last_name':obj.youth_last_name,
            'image':obj.image.url
        }

        data = {
            'youth': youth,
        }
        return JsonResponse(data)

#Ajax
class ProfileUpdateYouth(View):
    def get(self, request):
        id1 = request.GET.get('id', None)
        youthfn = request.GET.get('youth_first_name', None)
        youthmn = request.GET.get('youth_middle_name', None)
        youthln = request.GET.get('youth_last_name', None)

        obj = Youth.objects.get(id=id1)
        obj.youth_first_name = youthfn
        obj.youth_middle_name = youthmn
        obj.youth_last_name = youthln
        obj.save()

        youth = {
            'id':obj.id,
            'youth_first_name':obj.youth_first_name,
            'youth_middle_name':obj.youth_middle_name,
            'youth_last_name':obj.youth_last_name
        }

        data = {
            'youth': youth
        }
        return JsonResponse(data)

#Ajax
class ProfileDeleteYouth(View):
    def get(self, request):
        id1 = request.GET.get('id', None)

        #Find the cooresponding family object in the through table and retrieve its ID number
        youthidmatch = Family.objects.filter(youth_id=id1).values_list('id', flat=True).first()

        #Remove the family object, then the youth object
        Family.objects.get(id=youthidmatch).delete()
        Youth.objects.get(id=id1).delete()

        data = {
            'deleted': True
        }
        return JsonResponse(data)

#Ajax
class createQR(View):
    def get(self, request):
        thetime = now()
        thedate = str(thetime.month).zfill(2) + str(thetime.day).zfill(2) + str(thetime.year).zfill(4)
        familyids = Family.objects.filter(guardian_id=request.user.id).values_list('youth_id', flat=True)        
        filtered = list(Youth.objects.filter(id__in=familyids).filter(pre_check=1).values_list('id', flat=True))
        
        #Create a basic object to gracefully handle no code created.
        obj = {
            'code':"none",
            'qr_code':""
        }

        #If any results are found, do the work.
        if len(filtered) > 0:
            delim = "-"
            filtered.insert(0, request.user.id)
            filtered.insert(0, thedate)
            strbuilder = list(map(str, filtered))
        
            newQRcode = CheckInQr.objects.create(
                code = delim.join(strbuilder),
                creatorid = request.user.id,
                completed = False 
            )
        
            obj = {
                'code':newQRcode.code,
                'qr_code':newQRcode.qr_code.url
            }

        #TODO: Use consistent coding for QR display in HTML.
        #Template uses a-href-insert instead of {{python.objects}}.

        data = {
            'obj': obj
        }
        return JsonResponse(data)
    
#Ajax
class StaffCheckInYouth(View):
    def get(self, request):
        sentjson = unquote_plus(request.META['QUERY_STRING'])
        data = json.loads(sentjson)

        for yout in data['youths']:
            print(yout['id'])
            print(yout['is_checked_in'])

            #Begin original methods here
            #id1 = request.GET.get('id', None)
            #youthcn = request.GET.get('is_checked_in', None).capitalize()

            obj = Youth.objects.get(id=yout['id'])
            obj.is_checked_in = yout['is_checked_in']

            maxtimestamp = YouthCheckInLog.objects.filter(youthid=yout['id']).values_list('last_checkin', flat=True).order_by('-last_checkin').first()
            youthidmatch = YouthCheckInLog.objects.filter(youthid=yout['id']).values_list('id', flat=True).order_by('-last_checkin').first()

            #If checking in functions
            if obj.is_checked_in == True:
                obj.last_checkin = now()
                obj.pre_check = 0

                newlogobj = YouthCheckInLog.objects.create(
                    youth_first_name = obj.youth_first_name,
                    youth_last_name = obj.youth_last_name,
                    youthid = yout['id'],
                    checked_in_by = request.user.id,
                    last_checkin = now()
                )
            else: #checking out
                obj.last_checkout = now()
                obj.pre_check = 0

                updlogobj = YouthCheckInLog.objects.get(id=youthidmatch)
                updlogobj.checked_out_by = request.user.id
                updlogobj.last_checkout = now()
                updlogobj.save()

            #Checkin complete, save record to database
            obj.save()

        responsedata = {}
        return JsonResponse(responsedata)

#Ajax
class CamCheck(View):
    def get(self, request):
        scanresult = camControl()
        scanresulttype = scanresult[1]
        scanresultdecode = str(scanresult[0])
        resultsubstring = scanresultdecode[2:-1]
        
        #Only pull single object where completed = 0
        qrobj = CheckInQr.objects.get(code=resultsubstring, completed=0)

        qrcodearray = qrobj.code.split('-')

        qrcreateddate = qrcodearray[0]
        qruserid = qrcodearray[1]

        #remove userid and date so that only youth items remain
        #remove parent first, remove date second.
        del qrcodearray[1]
        del qrcodearray[0]

        multiqrobjs = Youth.objects.filter(id__in=(qrcodearray))
        qrobj = CheckInQr.objects.filter(code=qrobj.code).latest('createddate')

        qrobj.completed = True

        #Auto save function after camera scan, save to db
        qrobj.save()
        
        #Empty youth list object.  For loop will add JSON objects as necessary
        youth = []

        for yout in multiqrobjs:
            youth.append(
                {
                    'id':yout.id,
                    'youth_first_name':yout.youth_first_name,
                    'youth_middle_name':yout.youth_middle_name,
                    'youth_last_name':yout.youth_last_name,
                    'image':yout.image.url,
                    'is_checked_in':yout.is_checked_in
                }
            )

        data = {
            'youth': youth
        }
        return JsonResponse(data)

#Ajax
class GuardianPreCheck(View):
    def get(self, request):
        id1 = request.GET.get('id', None)
        youthcn = request.GET.get('pre_check', None).capitalize()

        obj = Youth.objects.get(id=id1)
        obj.pre_check = youthcn
        obj.save()

        youth = {
            'id':obj.id,
            'pre_check':obj.pre_check
        }

        data = {
            'youth': youth
        }
        return JsonResponse(data)

def camControl():
    warnings.filterwarnings("error")

    #TODO: Handle errors better if the camera is simply unplugged
    cap = cv2.VideoCapture(0)
    whatgotscanned = ''

    cap.set(3, 640)
    cap.set(4, 480)
    camera = True
    while camera == True:
        success, frame = cap.read()

        print(frame)

        scans = decode(frame)

        if len(scans) == 1:
            whatgotscanned = scans[0]
            time.sleep(1)
            camera = False

        #for code in decode(frame):
            #print(code.type)
            #print(code.data.decode('utf-8'))
            #time.sleep(3)
        
        cv2.imshow('open_check_in-qr-scan', frame)
        if cv2.waitKey(1) == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()

    return whatgotscanned