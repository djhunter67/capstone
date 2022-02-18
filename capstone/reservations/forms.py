from random import choice
from django import forms
from .models import Reservation, AutoBay
from django.utils import timezone
# from bootstrap_datepicker_plus import DatePickerInput


class DateInput(forms.DateTimeInput):
    input_type = 'datetime-local'
    input_format = "['%d/%m/%Y %I:%M']"


class MakeReservationForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super(MakeReservationForm, self).__init__(*args, **kwargs)
        self.initial['reservation_date'] = timezone.now()
    
    # Choices == [(auto_bay_id, auto_bay_name), ...]
    auto_bay_id = forms.ModelChoiceField(
        queryset=AutoBay.objects.all())

    time_limit = forms.ChoiceField(choices=[(i, f"{i} hrs.") for i in range(1, 11)])
    # reservation_date = forms.DateTimeField(options={"format": "mm/dd/yyyy",
    #                                             "autoclose": True})

    class Meta:

        model = Reservation

        fields = [
            "reservation_date",
            "auto_bay_id",
            "time_limit",
        ]

        widgets = {
            "reservation_date": DateInput()
            # "auto_bay_id": forms.Select(attrs={'class': ''}),
            # "time_limit": forms.Select(attrs={'class': ''}),
        }
