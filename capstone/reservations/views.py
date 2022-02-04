from django.shortcuts import redirect, render
from django.urls import reverse
from reservations.forms import MakeReservationForm
from django.contrib.auth.decorators import login_required

# Create your views here.


@login_required
def reservations(request):

    if request.method == "GET":

        form = MakeReservationForm()

        return render(request, "reservation.html", {"form": form})

    print(request.POST)

    form = MakeReservationForm(data=request.POST)

    print(form.is_valid())
    print(form.errors.as_json())
    if form.is_valid():
        print("VALID!!!!")
        form.save()

        print(form.base_fields)


    return redirect(reverse("hunter_diy_garage:index"))
