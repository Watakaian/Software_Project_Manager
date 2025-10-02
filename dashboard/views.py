from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from projects.models import Project, Requirement
from clients.models import Client
from payments.models import Payment

# Create your views here.
@login_required
def index(request):
    projects = Project.objects.all()[:5]
    project_status_choices = Project.STATUS_CHOICES  # expose choices
    requirement_status_choices = Requirement.STATUS_CHOICES  # expose choices
    requirement_type_choices = Requirement.TYPE_CHOICES  # expose choices
    payment_status_choices = Payment.STATUS_CHOICES  # expose choices
    clients = Client.objects.all()[:5]
    unpaid_invoices = Payment.objects.filter(status="pending")[:5]
    pending_requirements = Requirement.objects.filter(status="pending") [:5]

    context = {
        "projects": projects,
        "clients": clients,
        "unpaid_invoices": unpaid_invoices,
        "pending_requirements": pending_requirements,
        "project_status_choices": project_status_choices, # To use in add project modal
        "requirement_type_choices": requirement_type_choices,
        "requirement_status_choices": requirement_status_choices,
        "payment_status_choices": payment_status_choices,
    }
    return render(request, "dashboard/index.html", context)
