from django.contrib import admin

from .models import Job


@admin.register(Job)
class JobAdmin(admin.ModelAdmin):
    list_display = ["title", "employment_type", "location", "is_active", "created_at"]
    list_filter = ["is_active", "employment_type"]
    list_editable = ["is_active"]
    search_fields = ["title", "description"]