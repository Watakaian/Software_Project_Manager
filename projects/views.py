from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from django.views.decorators.http import require_POST
from .models import Project
from .forms import ProjectForm

def project_list(request):
    projects = Project.objects.all()
    return render(request, "projects/project_list.html", {"projects": projects})

@require_POST
def project_delete(request, pk):
    project = get_object_or_404(Project, pk=pk)
    project.delete()
    return HttpResponse("")  # HTMX will remove the row

def project_update_inline(request, pk):
    project = get_object_or_404(Project, pk=pk)
    if request.method == "POST":
        form = ProjectForm(request.POST, instance=project)
        if form.is_valid():
            form.save()
            return render(request, "projects/partials/project_row.html", {"project": project})
    else:
        form = ProjectForm(instance=project)
    return render(request, "projects/partials/project_edit_form.html", {"form": form, "project": project})
