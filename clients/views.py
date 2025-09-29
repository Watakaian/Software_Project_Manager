from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_protect

from clients.models import Client
from clients.forms import ClientForm

# Create your views here.
def client_list(request):
    clients = Client.objects.all()
    return render(request, "clients/client_list.html", {"clients":clients})

@csrf_protect
def create_client(request):
    if request.method == "POST":
        form = ClientForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("dashboard:index")
        else:
            print("FORM ERRORS", form.errors)
            return redirect("dashboard:index")
    return redirect("dashboard:index")