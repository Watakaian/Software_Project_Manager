from django.db import models
from clients.models import Client
from django.utils import timezone

# Create your models here.
class Project(models.Model):
    STATUS_CHOICES = [
        ("draft", "Draft"),
        ("in_progress", "In Progress"),
        ("completed", "Completed"),
        ("on-hold", "On Hold"),
        ("cancelled", "Cancelled"),
    ]
    client = models.ForeignKey(Client, on_delete=models.CASCADE, related_name="projects")
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True,null=True)
    start_date = models.DateField(default=timezone.now)
    due_date = models.DateField(blank=True, null=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default="draft")
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

class Requirement(models.Model):
    TYPE_CHOICES = [
        ("functional", "Functional"),
        ("non-functional", "Non-Functional"),
    ]

    STATUS_CHOICES = [
        ("pending", "Pending"),
        ("in_review", "In Review"),
        ("approved", "Approved"),
        ("rejected", "Rejected"),
    ]

    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name="requirements")
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    requirement_type = models.CharField(max_length=20, choices=TYPE_CHOICES, default="functional")
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default="pending")
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.title} ({self.get_requirement_type_display()})"
    
