from django import forms

class ExitForm(forms.Form):
    registration_number = forms.CharField(label='Car Registration', max_length=20)

class CheckoutForm(forms.Form):
    payment_method = forms.ChoiceField(label='Payment Method', choices=[('mpesa', 'M-Pesa'), ('card', 'Credit Card')])
    transaction_reference = forms.CharField(label='Transaction Reference', max_length=100)

class CarRegistrationForm(forms.Form):
    registration_number = forms.CharField(label='Car Registration', max_length=20)
    entry_time = forms.DateTimeField(label='Entry Time', widget=forms.DateTimeInput(attrs={'type': 'datetime-local'}))
    exit_time = forms.DateTimeField(label='Exit Time', widget=forms.DateTimeInput(attrs={'type': 'datetime-local'}))
