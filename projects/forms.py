from django import forms
from .models import Project, Requirement

class ProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = ["client","title","description","start_date","due_date","status"]

        widgets = {
            "client" : forms.TextInput(attrs={"class":"input input-bordered w-full rounded-full"}),
            "title" : forms.TextInput(attrs={"class":"input input-bordered w-full rounded-full"}),
            "description": forms.Textarea(attrs={"class":"textarea w-full rounded-full"}),
            "start_date" : forms.TextInput(attrs={"class":"input input-bordered w-full rounded-full"}),
            "due_date" : forms.TextInput(attrs={"class":"input input-bordered w-full rounded-full"}),
            "status" : forms.DateInput(attrs={"class":"input input-bordered w-full rounded-full"}),
        }