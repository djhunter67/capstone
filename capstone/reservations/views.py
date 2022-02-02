from django.shortcuts import render
from reservations.forms import MakeReservationForm

# Create your views here.


def reservation(request):

    if request.method == "GET":
        form = MakeReservationForm()

    return render(request, "reservation.html", {"form": form})
   
