import json
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import HttpResponse, HttpResponseRedirect, render
from django.urls import reverse
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required

from .models import User

def index(request):
    return HttpResponse("Hello, world!")


def signin_view(request):
    if request.method == "POST":

        # Attempt to sign user in
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)

        # Check if authentication successful
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse("add"))
        else:
            return render(request, "tracker/signin.html", {
                "message": "Invalid username or password."
            })
    else:
        return render(request, "tracker/signin.html")

def signout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse("signin"))

@login_required
def add_view(request):

    # Get the signedin user
    user = None

    if request.user.is_authenticated:
        user = User.objects.get(username=request.user.username)


    return render(request, "tracker/add.html", {
        "user": user
    })