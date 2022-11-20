from django.contrib import admin
from django_google_maps import widgets as map_widgets
from django_google_maps import fields as map_fields

from .models import *

# Register your models here.
admin.site.register(State)
admin.site.register(District)
admin.site.register(BloodGroup)
admin.site.register(Donor)
admin.site.register(Organ)
admin.site.register(Hospital)
admin.site.register(Patient)
admin.site.register(BrainDeath)
admin.site.register(Staff)