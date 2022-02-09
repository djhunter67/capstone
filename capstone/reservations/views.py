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

    print(f"{F.LIGHTGREEN_EX}{form}{R}")
    form = MakeReservationForm(form)

    print(f'Bay: {F.YELLOW}{form["auto_bay_id"].data}{R}')
    print(f'Time: {F.BLUE}{form["time_limit"].data}{R} Hours')
    print(f'{F.BLUE}{form["reservation_date"].data}{R}')
    print(f"{F.CYAN}{form['auto_bay_id'].data}{R}")

    print(f"{F.RED}{form.errors}{R}")
    if form.is_valid():
        print(f"{F.GREEN}VALID!!!!{R}")

        reservation = form.save(commit=False)
        reservation.diy_user_id = request.user
        reservation.save()
        request.user.reservation = True

    return redirect(reverse("hunter_diy_garage:payment"))
