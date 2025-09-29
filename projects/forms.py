from django import forms
from projects.models import Project, Requirement

class ProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = ["title", "description", "client", "start_date", "due_date", "status"]
