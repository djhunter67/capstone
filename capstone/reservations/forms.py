from django import forms
from .models import Reservation, AutoBay
from colorama import Fore as F

R = F.RESET


class MakeReservationForm(forms.ModelForm):

    # Choices == [(auto_bay_id, auto_bay_name), ...]
    auto_bay_id = forms.ChoiceField(
        choices=[(i.id, i.name) for i in AutoBay.objects.all()])
    time_limit = forms.ChoiceField(choices=[(i, i) for i in range(1, 11)])
    reservation_date = forms.DateTimeField(input_formats=['%d/%m/%Y %H:%M'])

    class Meta:

        model = Reservation

        fields = [
            "reservation_date",
            "auto_bay_id",
            "time_limit",
        ]

        widgets = {
            "reservation_date": BootstrapDateTimePickerInput(),
            "auto_bay_id": forms.Select(attrs={'class': ''}),
            "time_limit": forms.Select(attrs={'class': ''}),
        }
