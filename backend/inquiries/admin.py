from django.contrib import admin

from .models import Inquiry


@admin.register(Inquiry)
class InquiryAdmin(admin.ModelAdmin):
    list_display = ["name", "email", "company", "project_type", "budget", "status", "created_at"]
    list_filter = ["status", "project_type", "budget", "created_at"]
    search_fields = ["name", "email", "company", "message"]
    readonly_fields = ["created_at"]
    list_editable = ["status"]
