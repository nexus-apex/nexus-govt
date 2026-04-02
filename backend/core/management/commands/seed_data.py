from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
from core.models import GovService, GovApplication, Citizen
from datetime import date, timedelta
import random


class Command(BaseCommand):
    help = 'Seed NexusGovt with demo data'

    def handle(self, *args, **kwargs):
        if not User.objects.filter(username='admin').exists():
            User.objects.create_superuser('admin', 'admin@nexusgovt.com', 'Admin@2024')
            self.stdout.write(self.style.SUCCESS('Admin user created'))

        if GovService.objects.count() == 0:
            for i in range(10):
                GovService.objects.create(
                    name=f"Sample GovService {i+1}",
                    department=f"Sample {i+1}",
                    category=random.choice(["license", "permit", "certificate", "registration", "tax"]),
                    fee=round(random.uniform(1000, 50000), 2),
                    processing_days=random.randint(1, 100),
                    status=random.choice(["active", "suspended"]),
                    documents_required=f"Sample documents required for record {i+1}",
                    description=f"Sample description for record {i+1}",
                )
            self.stdout.write(self.style.SUCCESS('10 GovService records created'))

        if GovApplication.objects.count() == 0:
            for i in range(10):
                GovApplication.objects.create(
                    application_id=f"Sample {i+1}",
                    citizen_name=f"Sample GovApplication {i+1}",
                    service_name=f"Sample GovApplication {i+1}",
                    status=random.choice(["submitted", "under_review", "approved", "rejected", "pending_info"]),
                    submitted_date=date.today() - timedelta(days=random.randint(0, 90)),
                    processed_date=date.today() - timedelta(days=random.randint(0, 90)),
                    remarks=f"Sample remarks for record {i+1}",
                )
            self.stdout.write(self.style.SUCCESS('10 GovApplication records created'))

        if Citizen.objects.count() == 0:
            for i in range(10):
                Citizen.objects.create(
                    name=["Rajesh Kumar","Priya Sharma","Amit Patel","Deepa Nair","Vikram Singh","Ananya Reddy","Suresh Iyer","Meera Joshi","Karthik Rao","Fatima Khan"][i],
                    citizen_id=f"Sample {i+1}",
                    email=f"demo{i+1}@example.com",
                    phone=f"+91-98765{43210+i}",
                    address=f"Sample address for record {i+1}",
                    applications_count=random.randint(1, 100),
                    status=random.choice(["verified", "unverified"]),
                    registered_date=date.today() - timedelta(days=random.randint(0, 90)),
                )
            self.stdout.write(self.style.SUCCESS('10 Citizen records created'))
