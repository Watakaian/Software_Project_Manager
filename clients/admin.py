from django.contrib import admin
from .models import Client

# Register your models here.
@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
    list_display = ("name", "email", "phone_no","company", "created_at")
    search_fields = ("name", "email", "company")
    ordering = ("-created_at",)