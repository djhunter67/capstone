from capstone.forms import UserAuthorizeForm, UserCreationsForm
from colorama import Fore as F
from django.contrib.auth import authenticate
from django.contrib.auth import login as django_login
from django.contrib.auth import logout as django_logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render
from django.urls import reverse
from diy_users.models import DIYUsers

R = F.RESET


@login_required
def profile(request):
    """form for logging a user in; redirect to /profile/ after logging in"""

    if request.method == 'GET':

        user_data = request.user

        context = {
            "user_data": user_data,
        }

        return render(request, "profile.html", context)


def login(request):
    """form for logging a user in;redirect to /profile/ after logging in"""

    if request.method == "GET":
        form = UserAuthorizeForm()

        return render(request, 'login.html', {"form": form})

    form = UserAuthorizeForm(initial=request.POST)

    username = form.initial.get('username')[0]
    password = form.initial.get('password')[0]
    # print(f"{F.BLUE}{username}{password}{R}")
    user = authenticate(request, username=username, password=password)
    if user is not None:
        print(f"{F.GREEN}{user} Logged in!{R}")
        django_login(request, user)
        return render(request, 'profile.html')
    print(form.is_valid())
    print(f"{F.RED}Returning errors{R} {F.YELLOW}{form.errors}{R}")

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

        # context = {
        #     "form": UserCreationsForm()
        # }

        # Create a profile for the new user
        # DIYUsers.objects.create(user=new_user)

        return redirect(reverse('diy_users:profile', kwargs={'username': new_user.username}))
        # return redirect(reverse('diy_users:profile'))

    context = {
        "form": UserCreationsForm(),
        "errors": form.errors,
    }
    print(f"{F.RED}{form.errors.as_json()}{R}")

    return render(request, "register.html", context)


def logout(request):

    django_logout(request)
    return redirect(reverse("hunter_diy_garage:index"))
