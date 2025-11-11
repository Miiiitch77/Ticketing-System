def contact_help(request):
    return render(request, 'contact_help.html')
from django.shortcuts import render, get_object_or_404, redirect
from .models import ParkingRecord
from .forms import CarRegistrationForm, CheckoutForm, ExitForm
from django.utils import timezone
from datetime import timedelta

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

def calculate_charge(entry_time, exit_time):
    duration = exit_time - entry_time
    minutes = duration.total_seconds() / 60
    print(f"DEBUG: entry_time={entry_time}, exit_time={exit_time}, minutes={minutes}")
    if minutes <= 30:
        return 0
    elif minutes <= 60:
        return 50
    elif minutes <= 120:
        return 150
    elif minutes <= 180:
        return 200
    elif minutes <= 240:
        return 250
    elif minutes <= 300:
        return 300
    elif minutes <= 360:
        return 350
    elif minutes <= 420:
        return 400
    elif minutes <= 480:
        return 450
    else:
        return 500

def car_registration(request):
    charge = None
    parking_record = None
    if request.method == 'POST':
        form = CarRegistrationForm(request.POST)
        if form.is_valid():
            reg = form.cleaned_data['registration_number']
            entry = form.cleaned_data['entry_time']
            exit = form.cleaned_data['exit_time']
            charge = calculate_charge(entry, exit)
            hours_parked = (exit-entry).total_seconds()/3600
            parking_record = ParkingRecord.objects.create(
                car_registration=reg,
                entry_time=entry,
                exit_time=exit,
                hours_parked=hours_parked,
                charge=charge
            )
    else:
        form = CarRegistrationForm()
    return render(request, 'car_registration.html', {'form': form, 'charge': charge, 'parking_record': parking_record})


def checkout(request, record_id):
    parking_record = get_object_or_404(ParkingRecord, id=record_id)
    charge = parking_record.charge
    if request.method == 'POST':
        form = CheckoutForm(request.POST)
        if form.is_valid():
            # Simulate payment validation
            parking_record.paid = True
            parking_record.save()
            return render(request, 'checkout_success.html', {'parking_record': parking_record, 'charge': charge})
    else:
        form = CheckoutForm()
    return render(request, 'checkout.html', {'form': form, 'charge': charge, 'parking_record': parking_record})

def exit_parking(request):
    message = None
    if request.method == 'POST':
        form = ExitForm(request.POST)
        if form.is_valid():
            reg = form.cleaned_data['registration_number']
            record = ParkingRecord.objects.filter(car_registration=reg).order_by('-id').first()
            if record:
                if record.paid:
                    message = f"Exit allowed for {reg}. Payment confirmed."
                else:
                    message = f"Exit denied for {reg}. Please complete payment."
            else:
                message = f"No parking record found for {reg}."
    else:
        form = ExitForm()
    return render(request, 'exit_parking.html', {'form': form, 'message': message})

