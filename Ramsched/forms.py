from django.forms import ModelForm
from .models import *
from django import forms

class DateInput(forms.DateInput):
    input_type = 'date'

class CreateService(ModelForm):
    class Meta:
        widgets = {'service_date':DateInput()}
        model = Service
        fields = ['service_artist', 'service_client', 'service_date', 'service_type']

class CreateArtist(ModelForm):
    class Meta:
        model = ArtistInformation
        fields = ['artistname']

class CreateClient(ModelForm):
    class Meta:
        model = ClientInformations
        fields = ['last', 'first', 'email', 'phone',  'gender', 'age']

class CreateVoucher(ModelForm):
    class Meta:
        widgets = {'voucher_date':DateInput()}
        model = Voucher
        fields = ['voucher_name', 'voucher_type', 'voucher_date']
        
class CreatePayment(ModelForm):
    class Meta:
        model = Payment
        fields = ['service_id', 'payment_voucher', 'payment_method']

    def __init__(self, *args, **kwargs):
        super(CreatePayment, self).__init__(*args, **kwargs)
        self.fields['payment_voucher'].required = False
