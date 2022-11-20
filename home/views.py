from django.http import HttpResponse
from django.shortcuts import render,redirect
from .forms import *
from django.core.files.storage import FileSystemStorage
from django.contrib import messages
from django.contrib.auth import authenticate,login

# Create your views here.

def index(request):
    return render(request,'index.html')

def hospitalhome(request):
    return render(request,'hospitalhome.html')

def state(request):
    dict_state ={
        'state':State.objects.all()
    }
    return render(request,dict_state)

def district(request):
    dict_district ={
        'district':District.objects.all()
    }
    return render(request,dict_district)


def organ(request):
    dict_organ ={
        'organ':Organ.objects.all()
    }
    return render(request,dict_organ)

def blood_group(request):
    dict_bg ={
        'bg':BloodGroup.objects.all()
    }
    return render(request,dict_bg)  

def hospital(request):
    if request.method == "POST":
        print(request)
        form = HospitalForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return render(request,'confirmation.html')
    form = HospitalForm()
    return render(request,'hospital.html',{'form':form})

def staff(request):
    if request.method == "POST":
        print(request)
        form = StaffForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return render(request,'confirmation.html')
    form = StaffForm()
    return render(request,'staff.html',{'form':form})

def donor(request):
    if request.method == "POST":
        form = DonorForm(request.POST,request.FILES)
        if form.is_valid():
            uploaded_file = request.FILES['aadhar_doc']
            fs = FileSystemStorage()
            fs.save(uploaded_file.name,uploaded_file)
            form.save()
            return render(request,'confirmation.html')
    form = DonorForm()
    return render(request,'donor.html',{'form':form})


def patient(request):
    if request.method == "POST":
        form = PatientForm(request.POST,request.FILES)
        if form.is_valid():
            email = request.POST.get('email')
            if Patient.objects.filter(email=email).count()>0:
                return HttpResponse('Username already exists.')
        else:
            uploaded_file = request.FILES['aadhar_doc']
            fs = FileSystemStorage()
            fs.save(uploaded_file.name,uploaded_file)
            form.save()
            return render(request,'message.html')
    form = PatientForm()
    return render(request,'patient.html',{'form':form})


def braindeath(request):
    if request.method == "POST":
        form = BrainDeathForm(request.POST,request.FILES)
        if form.is_valid():
            
            uploaded_file = request.FILES['consent_form']
            fs = FileSystemStorage()
            fs.save(uploaded_file.name,uploaded_file)
            form.save()
            return render(request,'message.html')
    form = BrainDeathForm()
    return render(request,'braindeath.html',{'form':form})

def hsplogin(request):
    msg =''
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        hsptl = Hospital.objects.filter(username=username,password=password).count()
        if hsptl > 0:
            request.session['hospitalhome'] = True
            msg = "Login Successfully!!"
            return redirect('hospitalhome')
        else:
            msg = 'Invalid credentials!! Please try again..'
    form = HospitalLogin()
    return render(request,'hospital_login.html',{'form':form,'msg':msg})

def stafflogin(request):
    msg =''
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        staff = Staff.objects.filter(email=email,password=password)
        donor = Donor.objects.filter(email=email,password=password)
        patient = Patient.objects.filter(email=email,password=password)
        if staff:
            request.session['waitinglist'] = email
            msg = "Login Successfully!!"
            return redirect('waitinglist')
        elif donor:
            request.session['editdonor'] = email
            msg = "Login Successfully!!"
            return redirect('editdonor')
        elif patient:
            request.session['approve'] = email
            msg = "Login Successfully!!"
            return redirect('approve')
        else:
            msg = 'Invalid credentials!! Please try again..'
    form = StaffLogin()
    return render(request,'login.html',{'form':form,'msg':msg})

def logout_view(request):
    return redirect('login')

def waitinglist(request):
    #st = Staff.objects.all().values_list('hname',flat=True)
    #bd = BrainDeath.objects.filter(hname__in=st)

    #bd1 = BrainDeath.objects.all().values_list('hname',flat=True)
    bd1 = BrainDeath.objects.all()
    #st1 = BrainDeath.objects.filter(hname__in = bd1)
    #print(st1)
    print(bd1)
    #if st1 is not None and st1.hname == bd1.hname :
        #obj = BrainDeath.objects.all()
        #bd2 = BrainDeath.objects.all().values_list('organ')
        #pt = Patient.objects.all().values_list('organ')
        #bd3 = BrainDeath.objects.all().values_list('organ')
        #pt1 = Patient.objects.all().values_list('organ')
        #if bd2 == pt and bd3 == pt1:
        #    bd4 = BrainDeath.objects.all()
        #    return render(request,'waitinglist.html',{'data':obj})

    return render(request,'waitinglist.html',{'data':bd1})

def list(request):

    return render(request,'list.html')

def editdonor(request):

    return render(request,'editdonor.html')