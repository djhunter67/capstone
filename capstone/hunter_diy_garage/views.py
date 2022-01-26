from django.shortcuts import render

# Create your views here.


def index(request):

    return render(request, "index.html")


def about(request):

    return render(request, "about.html")


def login(request):

    return render(request, "login.html")


def register(request):

    return render(request, "register.html")


def blog(request):

    return render(request, "blog.html")


def reservation(request):

    return render(request, "reservation.html")


def tools(request):

    return render(request, "tools.html")


def bays(request):

    return render(request, "bays.html")


def contact(request):

    return render(request, "contact.html")


def layout(request):

    return render(request, "layout.html")


def cancellation(request):

    return render(request, "cancellation.html")


def logout(request):

    return render(request, "logout.html")


def price(request):

    return render(request, "price.html")


def rules(request):

    return render(request, "rules.html")
