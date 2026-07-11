from django.core.management.base import BaseCommand
from django.utils import timezone
from datetime import timedelta
from user.models import CustomUser
from properties.models import Property, Unit
from tenants.models import Tenant
from payments.models import Payment
from maintenance.models import MaintenanceRequest


class Command(BaseCommand):
    help = 'Populate database with sample data for testing'

    def handle(self, *args, **options):
        self.stdout.write(self.style.SUCCESS('🌱 Starting data seeding...'))

        # Create Landlord Users
        landlord1, created = CustomUser.objects.get_or_create(
            username='landlord1',
            defaults={
                'email': 'landlord1@example.com',
                'first_name': 'John',
                'last_name': 'Smith',
                'role': 'landlord',
                'phone': '555-0101',
                'address': '100 Property Ave',
                'city': 'Portland',
                'state': 'OR',
                'zip_code': '97201'
            }
        )
        if created:
            landlord1.set_password('password123')
            landlord1.save()
            self.stdout.write(self.style.SUCCESS('✓ Created landlord1'))

        # Create Tenant Users
        tenant1, created = CustomUser.objects.get_or_create(
            username='tenant1',
            defaults={
                'email': 'tenant1@example.com',
                'first_name': 'Alice',
                'last_name': 'Johnson',
                'role': 'tenant',
                'phone': '555-0201',
                'address': '123 Rental St',
                'city': 'Portland',
                'state': 'OR',
                'zip_code': '97201'
            }
        )
        if created:
            tenant1.set_password('password123')
            tenant1.save()
            self.stdout.write(self.style.SUCCESS('✓ Created tenant1'))

        tenant2, created = CustomUser.objects.get_or_create(
            username='tenant2',
            defaults={
                'email': 'tenant2@example.com',
                'first_name': 'Bob',
                'last_name': 'Williams',
                'role': 'tenant',
                'phone': '555-0202',
                'address': '456 Lease Ave',
                'city': 'Portland',
                'state': 'OR',
                'zip_code': '97201'
            }
        )
        if created:
            tenant2.set_password('password123')
            tenant2.save()
            self.stdout.write(self.style.SUCCESS('✓ Created tenant2'))

        # Create Maintenance Staff
        maintenance_staff, created = CustomUser.objects.get_or_create(
            username='maintenance1',
            defaults={
                'email': 'maintenance@example.com',
                'first_name': 'Mike',
                'last_name': 'Thompson',
                'role': 'maintenance',
                'phone': '555-0301',
            }
        )
        if created:
            maintenance_staff.set_password('password123')
            maintenance_staff.save()
            self.stdout.write(self.style.SUCCESS('✓ Created maintenance staff'))

        # Create Properties
        property1, created = Property.objects.get_or_create(
            owner=landlord1,
            name='Downtown Apartments',
            defaults={
                'address': '123 Main Street',
                'city': 'Portland',
                'state': 'OR',
                'zip_code': '97201',
                'total_units': 4,
                'property_type': 'apartment',
                'description': 'Modern downtown apartments',
                'amenities': 'Parking, Gym, Pool, Laundry'
            }
        )
        if created:
            self.stdout.write(self.style.SUCCESS('✓ Created Downtown Apartments'))

        property2, created = Property.objects.get_or_create(
            owner=landlord1,
            name='Riverside Condos',
            defaults={
                'address': '456 River Road',
                'city': 'Portland',
                'state': 'OR',
                'zip_code': '97202',
                'total_units': 6,
                'property_type': 'condo',
                'description': 'Beautiful riverside condos',
                'amenities': 'River View, Balcony, Security'
            }
        )
        if created:
            self.stdout.write(self.style.SUCCESS('✓ Created Riverside Condos'))

        # Create Units for Property 1
        unit1, created = Unit.objects.get_or_create(
            property=property1,
            unit_number='101',
            defaults={
                'rent_amount': 1200.00,
                'bedrooms': 1,
                'bathrooms': 1,
                'square_feet': 650,
                'is_available': False,
                'features': 'Hardwood floors, Modern kitchen'
            }
        )
        if created:
            self.stdout.write(self.style.SUCCESS('✓ Created Unit 101'))

        unit2, created = Unit.objects.get_or_create(
            property=property1,
            unit_number='102',
            defaults={
                'rent_amount': 1400.00,
                'bedrooms': 2,
                'bathrooms': 1,
                'square_feet': 850,
                'is_available': False,
                'features': 'Balcony, Stainless steel appliances'
            }
        )
        if created:
            self.stdout.write(self.style.SUCCESS('✓ Created Unit 102'))

        unit3, created = Unit.objects.get_or_create(
            property=property1,
            unit_number='103',
            defaults={
                'rent_amount': 1600.00,
                'bedrooms': 2,
                'bathrooms': 2,
                'square_feet': 950,
                'is_available': True,
                'features': 'Washer/dryer in unit, Walk-in closet'
            }
        )
        if created:
            self.stdout.write(self.style.SUCCESS('✓ Created Unit 103'))

        # Create Units for Property 2
        unit4, created = Unit.objects.get_or_create(
            property=property2,
            unit_number='201',
            defaults={
                'rent_amount': 1800.00,
                'bedrooms': 2,
                'bathrooms': 2,
                'square_feet': 1000,
                'is_available': True,
                'features': 'River view, Fireplace'
            }
        )
        if created:
            self.stdout.write(self.style.SUCCESS('✓ Created Unit 201'))

        # Create Tenant Profiles
        tenant_profile1, created = Tenant.objects.get_or_create(
            user=tenant1,
            defaults={
                'property': property1,
                'unit': unit1,
                'lease_start_date': timezone.now().date() - timedelta(days=180),
                'lease_end_date': timezone.now().date() + timedelta(days=185),
                'monthly_rent': 1200.00,
                'security_deposit': 1200.00,
                'emergency_contact_name': 'Sarah Johnson',
                'emergency_contact_phone': '555-0211',
                'status': 'active'
            }
        )
        if created:
            self.stdout.write(self.style.SUCCESS('✓ Created Tenant Profile 1'))

        tenant_profile2, created = Tenant.objects.get_or_create(
            user=tenant2,
            defaults={
                'property': property1,
                'unit': unit2,
                'lease_start_date': timezone.now().date() - timedelta(days=90),
                'lease_end_date': timezone.now().date() + timedelta(days=275),
                'monthly_rent': 1400.00,
                'security_deposit': 1400.00,
                'emergency_contact_name': 'Mary Williams',
                'emergency_contact_phone': '555-0212',
                'status': 'active'
            }
        )
        if created:
            self.stdout.write(self.style.SUCCESS('✓ Created Tenant Profile 2'))

        # Create Payments
        payment1, created = Payment.objects.get_or_create(
            tenant=tenant_profile1,
            due_date=timezone.now().date(),
            defaults={
                'amount': 1200.00,
                'status': 'paid',
                'payment_method': 'bank_transfer',
                'payment_date': timezone.now().date() - timedelta(days=2),
                'transaction_id': 'TXN-001-2026'
            }
        )
        if created:
            self.stdout.write(self.style.SUCCESS('✓ Created Payment 1'))

        payment2, created = Payment.objects.get_or_create(
            tenant=tenant_profile2,
            due_date=timezone.now().date() + timedelta(days=5),
            defaults={
                'amount': 1400.00,
                'status': 'pending',
                'payment_method': '',
                'transaction_id': ''
            }
        )
        if created:
            self.stdout.write(self.style.SUCCESS('✓ Created Payment 2'))

        # Create Maintenance Requests
        maintenance1, created = MaintenanceRequest.objects.get_or_create(
            property=property1,
            title='Fix leaky faucet',
            defaults={
                'unit_number': '101',
                'reported_by': tenant1,
                'assigned_to': maintenance_staff,
                'description': 'Kitchen sink faucet is dripping constantly',
                'priority': 'medium',
                'status': 'in_progress',
                'estimated_cost': 150.00,
            }
        )
        if created:
            self.stdout.write(self.style.SUCCESS('✓ Created Maintenance Request 1'))

        maintenance2, created = MaintenanceRequest.objects.get_or_create(
            property=property2,
            title='Paint hallway',
            defaults={
                'reported_by': landlord1,
                'assigned_to': maintenance_staff,
                'description': 'Common hallway needs fresh paint',
                'priority': 'low',
                'status': 'open',
                'estimated_cost': 500.00,
            }
        )
        if created:
            self.stdout.write(self.style.SUCCESS('✓ Created Maintenance Request 2'))

        self.stdout.write(self.style.SUCCESS('\n✅ Data seeding completed!'))
        self.stdout.write(self.style.SUCCESS('\n📝 Test Credentials:'))
        self.stdout.write('  Admin: admin / admin123')
        self.stdout.write('  Landlord: landlord1 / password123')
        self.stdout.write('  Tenant: tenant1 / password123')
        self.stdout.write('  Maintenance: maintenance1 / password123')
