from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.template.loader import render_to_string
from django.http import HttpResponse
from django.db.models import Q
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

def search(request):
    query = request.GET.get("q", "").strip()
    if not query:
        return HttpResponse("")  # Return empty response if no query

    # Search across all relevant models
    payments = Payment.objects.filter(
        Q(project__title__icontains=query) |
        Q(amount__icontains=query) |
        Q(status__icontains=query)
    ).values("id", "project__title", "amount", "status")

    clients = Client.objects.filter(
        Q(name__icontains=query) |
        Q(email__icontains=query) |
        Q(phone_no__icontains=query) |
        Q(company__icontains=query)
    ).values("id", "name", "email", "phone_no", "company")

    projects = Project.objects.filter(
        Q(title__icontains=query) |
        Q(description__icontains=query) |
        Q(status__icontains=query)
    ).values("id", "title", "description", "status")

    requirements = Requirement.objects.filter(
        Q(title__icontains=query) |
        Q(description__icontains=query) |
        Q(requirement_type__icontains=query) |
        Q(status__icontains=query)
    ).values("id", "title", "description", "requirement_type", "status")

    # Combine results into a single dictionary
    results = {
        "payments": list(payments),
        "clients": list(clients),
        "projects": list(projects),
        "requirements": list(requirements),
    }

    # Render the partial template for HTMX
    html = render_to_string("dashboard/search_results.html", {"results": results})
    return HttpResponse(html)
