from django.shortcuts import render
from clients import models

# Create your views here.
def client_list(request):
    clients = models.Client.objects.all()
    return render(request, "clients/client_list.html", {"clients":clients})