from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from projects.models import Project, Requirement
from clients.models import Client
from payments.models import Payment

# Create your views here.
@login_required
def index(request):
    projects = Project.objects.all()[:5]
    clients = Client.objects.all()[:5]
    unpaid_invoices = Payment.objects.filter(status="pending")[:5]
    pending_requirements = Requirement.objects.filter(status="pending") [:5]

    context = {
        "projects": projects,
        "clients": clients,
        "unpaid_invoices": unpaid_invoices,
        "pending_requirements": pending_requirements,
    }
    return render(request, "dashboard/index.html", context)
