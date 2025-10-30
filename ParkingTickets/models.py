from django.db import models

class ParkingRecord(models.Model):
    car_registration = models.CharField(max_length=20)
    hours_parked = models.FloatField()
    charge = models.DecimalField(max_digits=10, decimal_places=2)
    time_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.car_registration} - {self.charge} Ksh"
