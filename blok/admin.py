from django.contrib import admin
from .models import *
from django.contrib.auth.models import Group, User



class CarsAdmin(admin.ModelAdmin):
    list_display = ('number', 'driver_name', 'state_number', 'type_of_car', 'tex_passport_number')
    search_fields =['state_number',]
    
class DriversAdmin(admin.ModelAdmin):
    list_display= ('number','first_name', 'last_name', 'phone_number', 'passport_image', 'address')
    search_fields =['first_name', 'last_name',] 
    
class LitsenceAdmin(admin.ModelAdmin):
    list_display= ( 'number', 'car_state_number', 'given_date', 'deadline_date', 'comments')
    search_fields =['car_state_number__state_number',]
      
         
class PutyovkaAdmin(admin.ModelAdmin):
    list_display= ('date', 'state_number', 'money', 'comments')
    search_fields =['state_number__state_number',]
                 
admin.site.register(Drivers, DriversAdmin)    
admin.site.register(Cars, CarsAdmin)
admin.site.register(Putyovka, PutyovkaAdmin)
admin.site.register(Litsence, LitsenceAdmin)

admin.site.unregister(Group)
admin.site.unregister(User)

# Register your models here.