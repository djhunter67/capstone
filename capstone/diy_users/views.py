from capstone.forms import UserAuthorizeForm, UserCreationsForm
from colorama import Fore as F
from django.contrib.auth import authenticate
from django.contrib.auth import login as django_login
from django.contrib.auth import logout as django_logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render
from django.urls import reverse
from django.contrib import messages
from datetime import datetime

from reservations.models import Reservation


R = F.RESET


@login_required
def profile(request, username):
    """form for logging a user in; redirect to /profile/ after logging in"""

    if request.method == 'GET':

        user_data = request.user

        context = {
            "user_data": user_data,
            "res": Reservation.objects.order_by('-reservation_date')[0],         
        }

        return render(request, "profile.html", context)


def login(request):
    """form for logging a user in;redirect to /profile/ after logging in"""

    if request.method == "GET":

        form = UserAuthorizeForm()

        return render(request, 'login.html', {"form": form, "next_path": request.GET.get("next")})

    next_path = request.POST.get("next_path")
    # print(next_path.split('/'))

    form = UserAuthorizeForm(initial=request.POST)

    username = form.initial.get('username')[0]
    password = form.initial.get('password')[0]
    user = authenticate(request, username=username, password=password)
    if user is not None:
        print(f"{F.GREEN}{user} Logged in!{R}")
        django_login(request, user)

        if next_path != "None":
            try:
                return redirect(reverse(f"reservations:{next_path.strip('/')}"))
            except:
                return redirect(reverse(f"diy_users:{next_path.split('/')[1]}", args=[next_path.split('/')[2]]))

        return redirect(reverse("diy_users:profile", args=[user.username]))

    context = {
        "form": UserAuthorizeForm(),
        "errors": "Password  or Username are incorrect",
    }

    return render(request, 'login.html', context)


def register(request):
    """form for creating a new user; redirect to /profile/ after registering"""

    if request.method == "GET":
        form = UserCreationsForm()
        return render(request, 'register.html', {"form": form})

    form = UserCreationsForm(data=request.POST)

    if form.is_valid():
        new_user = form.save(commit=False)
        new_user.set_password(form.cleaned_data['password'])
        new_user.save()
        
        new_user = form.save()
        # new_user.reservation = False

        messages.add_message(request, messages.SUCCESS, f"Registration Successful {new_user.username}! You may now log in.")


        return redirect(reverse('diy_users:profile', kwargs={'username': new_user.username}))

    context = {
        "form": UserCreationsForm(),
        "errors": form.errors,
    }

    return render(request, "register.html", context)


def logout(request):

    django_logout(request)
    return redirect(reverse("hunter_diy_garage:index"))
