from django.shortcuts import redirect, render
from django.urls import reverse
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

    print(request.POST)

    form = MakeReservationForm(data=request.POST)

    print(f'Bay: {F.YELLOW}{form["auto_bay_id"].data}{R}')
    print(f'Time: {F.BLUE}{form["time_limit"].data}{R} Hours')
    print(f'{F.BLUE}{form["reservation_date"].data}{R}')
    # print(form.is_valid())
    print(f"{F.RED}{form.errors.as_text()}{R}")
    if form.is_valid():
        print("VALID!!!!")

        reservation = form.save(commit=False)
        reservation.diy_user_id = request.user
        reservation.save()

    # print(form.base_fields)

    return redirect(reverse("hunter_diy_garage:index"))
