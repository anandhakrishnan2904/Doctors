from django import forms

from .models import booking

class DateInput(forms.DateInput):
    input_type = 'date'

class bookingforms(forms.ModelForm):
    class Meta:
        model = booking
        fields ='__all__'

        widgets = {
            'booking_date': DateInput(),
        }

        labels ={
            'p_name': "patient Name:",
            'p_phone':"patient phone:",
            'P_email':"patient Email:",
            'doc_name' :"Doctor Name:",
            'booking_date': "Patient Date:",
        }