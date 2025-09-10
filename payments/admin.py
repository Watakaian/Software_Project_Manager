from django.contrib import admin
from .models import Payment

# Register your models here.
@admin.register(Payment)
class PaymentAdmin(admin.ModelAdmin):
    list_display = ("project","amount","due_date","status", "created_at")
    list_filter = ("status","project")
    search_fields = ("project__title",)
    ordering = ("-created_at",)