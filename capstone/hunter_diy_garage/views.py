from django.shortcuts import render
from .models import Tool

# Create your views here.


def index(request):

    return render(request, "index.html")


def about(request):

    return render(request, "about.html")


def blog(request):

    return render(request, "blog.html")


def tools(request):

    context = {
        "tools": Tool.objects.all()
    }

    return render(request, "tools.html", context)


def bays(request):

    return render(request, "bays.html")


def contact(request):

    return render(request, "contact.html")


def layout(request):

    return render(request, "layout.html")


def cancellation(request):

    return render(request, "cancellation.html")


def price(request):

    return render(request, "price.html")


def rules(request):

    ruleset = ["Be Kind", "Do Unto Others", "Love Thy Neighbor"]

    return render(request, "rules.html", {"ruleset": ruleset})
