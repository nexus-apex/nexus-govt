from django.db import models

class GovService(models.Model):
    name = models.CharField(max_length=255)
    department = models.CharField(max_length=255, blank=True, default="")
    category = models.CharField(max_length=50, choices=[("license", "License"), ("permit", "Permit"), ("certificate", "Certificate"), ("registration", "Registration"), ("tax", "Tax")], default="license")
    fee = models.DecimalField(max_digits=12, decimal_places=2, default=0)
    processing_days = models.IntegerField(default=0)
    status = models.CharField(max_length=50, choices=[("active", "Active"), ("suspended", "Suspended")], default="active")
    documents_required = models.TextField(blank=True, default="")
    description = models.TextField(blank=True, default="")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return self.name

class GovApplication(models.Model):
    application_id = models.CharField(max_length=255)
    citizen_name = models.CharField(max_length=255, blank=True, default="")
    service_name = models.CharField(max_length=255, blank=True, default="")
    status = models.CharField(max_length=50, choices=[("submitted", "Submitted"), ("under_review", "Under Review"), ("approved", "Approved"), ("rejected", "Rejected"), ("pending_info", "Pending Info")], default="submitted")
    submitted_date = models.DateField(null=True, blank=True)
    processed_date = models.DateField(null=True, blank=True)
    remarks = models.TextField(blank=True, default="")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return self.application_id

class Citizen(models.Model):
    name = models.CharField(max_length=255)
    citizen_id = models.CharField(max_length=255, blank=True, default="")
    email = models.EmailField(blank=True, default="")
    phone = models.CharField(max_length=255, blank=True, default="")
    address = models.TextField(blank=True, default="")
    applications_count = models.IntegerField(default=0)
    status = models.CharField(max_length=50, choices=[("verified", "Verified"), ("unverified", "Unverified")], default="verified")
    registered_date = models.DateField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return self.name
