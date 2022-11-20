from django import forms
from .models import *

class DateInput(forms.DateInput):
    input_type = 'date'

class DonorForm(forms.ModelForm):
    genders =(('Male','Male'),('Female','Female'),('Others',"Others"))
    gender = forms.ChoiceField(choices= genders,widget=forms.RadioSelect(attrs={}))

    class Meta:
        model = Donor
        fields = '__all__'

        widgets = {
            'dob' : DateInput(),
            'password':forms.PasswordInput()
        }
        labels = {
            'name' : "Name",
            'age' : "Age",
            'dob': "Date of Birth",
            'bloodgroup' : "Blood Group",
            'gender' : "Gender",
            'address' : "Address",
            'email' : "Email",
            'contact' : "Contact",
            'fname' : "Father's Name",
            'mname' : "Mother's Name",
            'state' : "State",
            'district' : "District",
            'aadhar' : "Aadhar",
            'photo' : "Upload Photo",
            'aadhar_doc' : "Upload Aadhar",
            'password': "Set Password"
        }
class HospitalForm(forms.ModelForm):
    class Meta:
        model = Hospital
        fields = '__all__'

        widgets = {
            'LicDate' : DateInput(),
            'password':forms.PasswordInput()
        }

        labels = {
            'hname' : "Hospital Name",
            'hid' : "Hospital ID",
            'web' : "Website",
            'address' : "Address",
            'state' : "State",
            'district' : "District",
            'email' : "Email",
            'contact' : "Contact",
            'DirName' : "Director's Name",
            'DirContact' : "Director's Contact",
            'DirEmail' : "Director's Email",
            'License' : "Is License Active",
            'CertNumber' : "Certificate Number",
            'LicDate' : "License Expiry Date",
            'Photo' : "Photo",
            'username' : "Username",
            'password' : "Set Password"
        }

class HospitalLogin(forms.ModelForm):
    class Meta:
        model = Hospital
        fields = ('username','password')

        widgets = {            
            'password':forms.PasswordInput()
        }
        labels={
            'username': "Enter Username",
            'password': "Enter Password"
        }

class PatientForm(forms.ModelForm):
    genders =(('Male','Male'),('Female','Female'),('Others',"Others"))
    gender = forms.ChoiceField(choices= genders,widget=forms.RadioSelect(attrs={}))

    class Meta:
        model = Patient
        fields = '__all__'

        widgets = {
            'dob' : DateInput(),
            'password':forms.PasswordInput()
        }
        labels = {
            'name' : "Name",
            'age' : "Age",
            'organ': "Required Organ",
            'dob': "Date of Birth",
            'bloodgroup' : "Blood Group",
            'gender' : "Gender",
            'address' : "Address",
            'email' : "Email",
            'contact' : "Contact",
            'fname' : "Father's Name",
            'mname' : "Mother's Name",
            'state' : "State",
            'district' : "District",
            'aadhar' : "Aadhar",
            'photo' : "Upload Photo",
            'aadhar_doc' : "Upload Aadhar",
            'password': "Set Password"
        }
def mobile_no(value):
        mobile = str(value)
        if len(mobile) != 10:
            raise forms.ValidationError("Mobile Number Should 10 digit")
class StaffForm(forms.ModelForm):
    class Meta:
        model = Staff
        fields = '__all__'
        widgets = {            
            'password':forms.PasswordInput()
        }
        labels= {
            'name' : "Staff Name",
            'staffid' : "Staff ID",
            'hname': "Hospital Name",
            'address' : "Permanent Address",
            'email': "Email ID",
            'contact' : "Contact",
            'password' : "Set Password"
        }
    

class StaffLogin(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    class Meta:
        model = Staff
        fields = ('email','password')
        labels={
            'email': "Enter Email",
            'password': "Enter Password"
        }

class BrainDeathForm(forms.ModelForm):
    genders =(('Male','Male'),('Female','Female'),('Others',"Others"))
    gender = forms.ChoiceField(choices = genders,widget=forms.RadioSelect(attrs={}))
    class Meta:
        model = BrainDeath
        fields = '__all__'

        widgets = {
            'dob' : DateInput(),
            'password':forms.PasswordInput()
        }
        labels = {
            'name' : "Name",
            'age' : "Age",
            'organ': "Organs",
            'dob': "Date of Birth",
            'bloodgroup' : "Blood Group",
            'gender' : "Gender",
            'address' : "Address"
        }

