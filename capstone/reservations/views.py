from django.shortcuts import redirect, render
from django.urls import reverse
from reservations.forms import MakeReservationForm

# Create your views here.


def reservation(request):

    if request.method == "GET":
        form = MakeReservationForm()

        return render(request, "reservation.html", {"form": form})

    form = MakeReservationForm(initial=request.POST)

    if form.is_valid():
        print("Valid")

        return redirect(reverse("hunter_diy_garage:index"))
   
