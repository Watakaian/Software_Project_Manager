from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from projects.models import Project
from clients.models import Client
from payments.models import Payment

# Create your views here.
@login_required
def index(request):
    projects = Project.objects.all()[:5]
    clients = Client.objects.count()
    unpaid_invoices = Payment.objects.filter(status="pending").count()

    context = {
        "projects": projects,
        "clients": clients,
        "unpaid_invoices": unpaid_invoices,
    }
    return render(request, "dashboard/index.html", context)
