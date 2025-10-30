from django.contrib import admin
from .models import ParkingRecord

@admin.register(ParkingRecord)
class ParkingRecordAdmin(admin.ModelAdmin):
    list_display = ('car_registration', 'hours_parked', 'charge', 'time_created')
