from django.contrib import admin
from .models import GovService, GovApplication, Citizen

@admin.register(GovService)
class GovServiceAdmin(admin.ModelAdmin):
    list_display = ["name", "department", "category", "fee", "processing_days", "created_at"]
    list_filter = ["category", "status"]
    search_fields = ["name", "department"]

@admin.register(GovApplication)
class GovApplicationAdmin(admin.ModelAdmin):
    list_display = ["application_id", "citizen_name", "service_name", "status", "submitted_date", "created_at"]
    list_filter = ["status"]
    search_fields = ["application_id", "citizen_name", "service_name"]

@admin.register(Citizen)
class CitizenAdmin(admin.ModelAdmin):
    list_display = ["name", "citizen_id", "email", "phone", "applications_count", "created_at"]
    list_filter = ["status"]
    search_fields = ["name", "citizen_id", "email"]
