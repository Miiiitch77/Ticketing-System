from django.db import models

class ParkingRecord(models.Model):
    car_registration = models.CharField(max_length=20)
    entry_time = models.DateTimeField(null=True, blank=True)
    exit_time = models.DateTimeField(null=True, blank=True)
    hours_parked = models.FloatField(default=0)
    charge = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    time_created = models.DateTimeField(auto_now_add=True)
    paid = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.car_registration} - {self.charge} Ksh"


