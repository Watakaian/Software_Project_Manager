from django.shortcuts import render,redirect
from django.views.decorators.csrf import csrf_protect
from django.views.generic import DetailView, DeleteView, UpdateView
from django.urls import reverse_lazy

from projects.models import Project, Requirement
from clients.models import Client
from projects.forms import ProjectForm, RequirementForm


def project_list(request):
    projects = Project.objects.all()
    return render(request, "projects/project_list.html", {"projects": projects})

@csrf_protect
def create_project(request):
    if request.method == "POST":
        form = ProjectForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("dashboard:index")
        else:
            print("FORM ERRORS:", form.errors)  # debug
            return redirect("dashboard:index")
    return redirect("dashboard:index")

class ProjectDetailView(DetailView):
    model = Project
    template_name = "projects/project_detail.html"
    context_object_name = "project"

class ProjectDeleteView(DeleteView):
    model = Project
    template_name = "projects/project_confirm_delete.html"
    success_url = reverse_lazy("projects:list")  # after delete, go back to project list
    context_object_name = "project"

class ProjectUpdateView(UpdateView):
    model = Project
    fields = ["client", "title", "description", "start_date", "due_date", "status"]
    template_name = "projects/project_update_form.html"
    context_object_name = "project"

    def get_success_url(self):
        return reverse_lazy("projects:detail", kwargs={"pk": self.object.pk})

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["clients"] = Client.objects.all()  # pass clients for dropdown
        return context


def requirement_list(request):
    requirements = Requirement.objects.filter(status="pending")
    return render(request, "projects/requirement_list.html", {"requirements":requirements})

@csrf_protect
def create_requirement(request):
    if request.method == "POST":
        form = RequirementForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("dashboard:index")
        else:
            print("FORM ERRORS:", form.errors)  # debug
            return redirect("dashboard:index")
    return redirect("dashboard:index")

class RequirementDetailView(DetailView):
    model = Requirement
    template_name = "projects/requirement_detail.html"
    context_object_name = "requirement"


class RequirementUpdateView(UpdateView):
    model = Requirement
    fields = ["project","title","description","requirement_type","status"]
    template_name = "projects/requirement_update_form.html"
    context_object_name = "requirement"

    def get_success_url(self):
        return reverse_lazy("projects:requirement_detail",kwargs={"pk":self.object.pk})
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["projects"] = Project.objects.all()
        return context


    def __str__(self):
        return f"{self.title} ({self.get_requirement_type_display()})"


class RequirementDeleteView(DeleteView):
    model = Requirement
    template_name = "projects/requirement_confirm_delete"
    success_url = reverse_lazy("projects:requirement_list")  # after delete, go back to requirement list
    context_object_name = "requirement"
