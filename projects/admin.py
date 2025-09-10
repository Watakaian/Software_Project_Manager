from django.contrib import admin
from .models import Project, Requirement

# Register your models here.

@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ("title", "client", "status", "start_date", "due_date", "created_at")
    list_filter = ("client", "status")
    search_fields = ("title","description")
    date_hierarchy = "start_date"
    ordering = ("-created_at",)


@admin.register(Requirement)
class RequirementAdmin(admin.ModelAdmin):
    list_display = ("title", "project", "requirement_type", "status", "created_at")
    list_filter = ("requirement_type", "status", "project")
    search_fields = ("title", "description")
    ordering = ("-created_at",)

