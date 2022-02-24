from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse
from diy_users.models import DIYUsers
from hunter_diy_garage.models import AutoBay
from reservations.forms import MakeReservationForm
from django.contrib.auth.decorators import login_required
from colorama import Fore as F


R = F.RESET


# Create your views here.


@login_required
def reservations(request):

    if request.method == "GET":

        form = MakeReservationForm()

        return render(request, "reservation.html", {"form": form})

    form = request.POST

    # API Call to JS

    form = MakeReservationForm(form)

    if form.is_valid():

        reservation = form.save(commit=False)
        reservation.diy_user_id = request.user
        reservation.save()
        request.user.reservation = True

    return redirect(reverse("hunter_diy_garage:payment"))
