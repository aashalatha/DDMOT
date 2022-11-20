from django.urls import path
from . import views
from django.contrib.auth import views as auth

urlpatterns = [
    path('', views.index,name='home'),
    path('donor', views.donor,name='donor'),
    path('hospital', views.hospital,name='hospital'),
    path('hospital_login', views.hsplogin,name='hospital_login'),
    path('login', views.stafflogin,name='login'),
    path('hospitalhome',views.hospitalhome,name='hospitalhome'),
    path('patient', views.patient,name='patient'),
    path('braindeath', views.braindeath,name='braindeath'),
    path('logout', views.logout_view, name='logout'),
    path('waitinglist',views.waitinglist,name='waitinglist'),
    path('staff', views.staff,name='staff'),
    path('list', views.list,name='list'),
    path('editdonor', views.editdonor,name='editdonor')
    #path('formView',views.formView,name='formView')
]