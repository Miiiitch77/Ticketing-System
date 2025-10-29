from django.shortcuts import render
from .models import ParkingRecord

def home(request):
    rates = [
        ("0 - 30 mins", "Free"),
        ("30 mins - 1 hr", "Ksh 50"),
        ("1 - 2 hrs", "Ksh 150"),
        ("2 - 3 hrs", "Ksh 200"),
        ("3 - 4 hrs", "Ksh 250"),
        ("4 - 5 hrs", "Ksh 300"),
        ("5 - 6 hrs", "Ksh 350"),
        ("6 - 7 hrs", "Ksh 400"),
        ("7 - 8 hrs", "Ksh 450"),
    ]
    return render(request, 'home.html', {'rates': rates})
