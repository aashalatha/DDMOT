from random import choices
from multiselectfield import MultiSelectField
from django.db import models

# Create your models here.
class State(models.Model):
    state = models.CharField(max_length = 25)

    def __str__(self) -> str:
        return self.state


class District(models.Model):
    state = models.ForeignKey(State,on_delete = models.CASCADE)
    district = models.CharField(max_length = 25)

    def __str__(self) -> str:
        return self.district

class BloodGroup(models.Model):
    bg = models.CharField(max_length = 10)

    def __str__(self) -> str:
        return self.bg

class Organ(models.Model):
    organ = models.CharField(max_length = 50)

    def __str__(self) -> str:
        return self.organ

class Donor(models.Model):
    name = models.CharField(max_length = 255)
    age = models.CharField(max_length = 10)
    dob = models.DateField()
    bloodgroup = models.ForeignKey(BloodGroup,on_delete = models.CASCADE)
    gen = (
        ('Male',"Male"),
        ('Female',"Female"),
        ('Others',"Others")

    )
    gender = models.CharField(max_length = 20, choices=gen)
    address = models.TextField()
    email = models.EmailField(max_length = 255)
    contact = models.CharField(max_length = 255)
    fname = models.CharField(max_length = 255)
    mname = models.CharField(max_length = 255)
    state = models.ForeignKey(State,on_delete = models.CASCADE)
    district = models.ForeignKey(District,on_delete = models.CASCADE)
    organs = (('Liver','Liver'),('Heart','Heart'),('Kidney','Kidney'),('Lungs','Lungs'),('Pancreas','Pancreas'),('Small Intestine','Small Intestine'),('Corneas','Corneas'),('Heart Valves','Heart Valves'),('Skin','Skin'))
    organ = MultiSelectField(choices=organs)
    aadhar = models.CharField(max_length = 255)
    photo = models.ImageField(upload_to = 'donor')
    aadhar_doc = models.FileField(upload_to='aadhar')
    password = models.CharField(max_length=20)


class Hospital(models.Model):
    hname = models.CharField(max_length = 255)
    hid = models.CharField(max_length = 255)
    web = models.URLField(max_length = 255)
    address = models.TextField()
    state = models.ForeignKey(State,on_delete = models.CASCADE)
    district = models.ForeignKey(District,on_delete = models.CASCADE)
    email = models.EmailField(max_length = 255)
    contact = models.CharField(max_length = 255)
    DirName = models.CharField(max_length = 255)
    DirContact = models.CharField(max_length = 255)
    DirEmail = models.EmailField(max_length = 255)
    lic = (
        ('Yes',"Yes"),
        ('No',"No")
    )
    License = models.CharField(max_length = 20, choices=lic)
    CertNumber = models.CharField(max_length = 255)
    LicDate = models.DateField()
    Photo = models.ImageField(upload_to = 'hospital')
    username = models.CharField(max_length = 255)
    password = models.CharField(max_length = 20) 

    def __str__(self) -> str:
        return self.hname

class Patient(models.Model):
    name = models.CharField(max_length = 255)
    age = models.CharField(max_length = 10)
    organ = models.ForeignKey(Organ,on_delete = models.CASCADE)
    dob = models.DateField()
    bloodgroup = models.ForeignKey(BloodGroup,on_delete = models.CASCADE)
    gen = (
        ('Male',"Male"),
        ('Female',"Female"),
        ('Others',"Others")
    )
    gender = models.CharField(max_length = 20, choices=gen)
    address = models.TextField()
    email = models.EmailField(max_length = 255)
    contact = models.CharField(max_length = 255)
    fname = models.CharField(max_length = 255)
    mname = models.CharField(max_length = 255)
    state = models.ForeignKey(State,on_delete = models.CASCADE)
    district = models.ForeignKey(District,on_delete = models.CASCADE)
    aadhar = models.CharField(max_length = 255)
    photo = models.ImageField(upload_to = 'donor')
    aadhar_doc = models.FileField(upload_to='aadhar')
    password = models.CharField(max_length=20)

class Staff(models.Model):
    name = models.CharField(max_length=255)
    staffid = models.CharField(max_length=20)
    hname = models.ForeignKey(Hospital,on_delete = models.CASCADE)
    address = models.TextField()
    email = models.EmailField(max_length = 255)
    contact = models.CharField(max_length = 255)
    password = models.CharField(max_length=20)

class BrainDeath(models.Model):
    name = models.CharField(max_length = 255)
    age = models.CharField(max_length = 10)
    dob = models.DateField()
    bloodgroup = models.ForeignKey(BloodGroup,on_delete = models.CASCADE)
    organs = (('Liver','Liver'),('Heart','Heart'),('Kidney','Kidney'),('Lungs','Lungs'),('Pancreas','Pancreas'),('Small Intestine','Small Intestine'),('Corneas','Corneas'),('Heart Valves','Heart Valves'),('Skin','Skin'))
    organ = MultiSelectField(choices=organs)
    gen = (
        ('Male',"Male"),
        ('Female',"Female"),
        ('Others',"Others")
    )
    gender = models.CharField(max_length = 20, choices=gen)
    address = models.TextField()   
    hname = models.ForeignKey(Hospital,on_delete = models.CASCADE)
    state = models.ForeignKey(State,on_delete = models.CASCADE)
    district = models.ForeignKey(District,on_delete = models.CASCADE)
    consent_form = models.FileField(upload_to='consent_form')
    
    