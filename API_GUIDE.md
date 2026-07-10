# Rental Management API - Complete Setup Guide

## ✅ Project Setup Complete!

Your rental management system is now fully functional with a Django REST Framework API. Here's what's been built:

---

## 🏗️ Architecture Overview

### Database Models

#### User (Custom User Model)
- Extended Django User with additional fields
- Roles: Landlord, Tenant, Maintenance Staff, Admin
- Fields: phone, address, city, state, zip_code, profile_picture

#### Properties
- Rental properties/buildings
- Owner: References CustomUser (Landlord)
- Tracks: total units, amenities, property type

#### Units
- Individual rental units within properties
- Fields: unit_number, rent_amount, bedrooms, bathrooms, square_feet, is_available
- Unique constraint: property + unit_number

#### Tenants
- Tenant rental information
- Links: User + Property + Unit
- Fields: lease dates, monthly rent, security deposit, emergency contact, status

#### Payments
- Rent payment records
- Tracks: amount, due date, payment date, status, payment method
- Status options: pending, paid, overdue, partial, cancelled

#### MaintenanceRequest
- Maintenance issue tracking
- Links: Property + reported_by (User) + assigned_to (User)
- Fields: title, description, priority, status, estimated/actual cost

---

## 🔌 API Endpoints

### Base URL
```
http://localhost:8000/api/
```

### Users
- `GET/POST /api/users/` - List/Create users
- `GET/PUT/DELETE /api/users/{id}/` - Retrieve/Update/Delete user
- `GET /api/users/me/` - Get current authenticated user
- `POST /api/users/{id}/set_password/` - Change password

### Properties
- `GET/POST /api/properties/` - List/Create properties
- `GET/PUT/DELETE /api/properties/{id}/` - Retrieve/Update/Delete property
- `GET /api/properties/{id}/units_summary/` - Property units summary

### Units
- `GET/POST /api/units/` - List/Create units
- `GET/PUT/DELETE /api/units/{id}/` - Retrieve/Update/Delete unit
- `GET /api/units/available/` - List available units
- Filter by property: `?property_id={id}`

### Tenants
- `GET/POST /api/tenants/` - List/Create tenants
- `GET/PUT/DELETE /api/tenants/{id}/` - Retrieve/Update/Delete tenant
- `GET /api/tenants/active/` - List active tenants
- `POST /api/tenants/{id}/move_out/` - Mark tenant as moved out

### Payments
- `GET/POST /api/payments/` - List/Create payments
- `GET/PUT/DELETE /api/payments/{id}/` - Retrieve/Update/Delete payment
- `GET /api/payments/overdue/` - List overdue payments
- `GET /api/payments/pending/` - List pending payments
- `POST /api/payments/{id}/mark_paid/` - Mark payment as paid

### Maintenance
- `GET/POST /api/maintenance/requests/` - List/Create requests
- `GET/PUT/DELETE /api/maintenance/requests/{id}/` - Retrieve/Update/Delete request
- `GET /api/maintenance/requests/open/` - List open requests
- `GET /api/maintenance/requests/urgent/` - List urgent requests
- `POST /api/maintenance/requests/{id}/start_work/` - Start working on request
- `POST /api/maintenance/requests/{id}/complete/` - Mark request as completed

---

## 🔐 Admin Panel

Access at: `http://localhost:8000/admin/`

**Credentials:**
- Username: `admin`
- Password: (set during migration)

All models are registered with rich admin interfaces including:
- Inline editing (Units within Properties)
- Filtering and searching
- Custom display fields
- Fieldset organization

---

## 🚀 Getting Started

### 1. Start the Development Server
```bash
# Activate virtual environment
.\.venv\Scripts\Activate.ps1

# Run server
python manage.py runserver 8000
```

### 2. Create Test Data

Use the admin panel or API to create:
- A Landlord user
- A Property with Units
- A Tenant user and Tenant profile
- Sample Payments and Maintenance Requests

### 3. Test API Endpoints

```bash
# Get API root
curl http://localhost:8000/api/

# List properties (requires authentication)
curl -u admin:password http://localhost:8000/api/properties/

# Create a property
curl -X POST http://localhost:8000/api/properties/ \
  -H "Content-Type: application/json" \
  -u admin:password \
  -d '{
    "name": "Downtown Apartments",
    "address": "123 Main St",
    "city": "Portland",
    "state": "OR",
    "zip_code": "97201",
    "total_units": 5,
    "property_type": "apartment"
  }'
```

---

## 📁 Project Structure

```
rental_project/
├── user/                 # User management
│   ├── models.py        # CustomUser model
│   ├── serializers.py   # User serializers
│   ├── views.py         # UserViewSet
│   ├── admin.py         # Admin configuration
│   └── urls.py          # User URLs
│
├── properties/          # Properties & units
│   ├── models.py        # Property, Unit models
│   ├── serializers.py   # Property serializers
│   ├── views.py         # PropertyViewSet, UnitViewSet
│   ├── admin.py         # Admin configuration
│   └── urls.py          # Property URLs
│
├── tenants/            # Tenant management
│   ├── models.py       # Tenant model
│   ├── serializers.py  # Tenant serializers
│   ├── views.py        # TenantViewSet
│   ├── admin.py        # Admin configuration
│   └── urls.py         # Tenant URLs
│
├── payments/           # Payment tracking
│   ├── models.py       # Payment model
│   ├── serializers.py  # Payment serializers
│   ├── views.py        # PaymentViewSet
│   ├── admin.py        # Admin configuration
│   └── urls.py         # Payment URLs
│
├── maintenance/        # Maintenance requests
│   ├── models.py       # MaintenanceRequest model
│   ├── serializers.py  # Maintenance serializers
│   ├── views.py        # MaintenanceRequestViewSet
│   ├── admin.py        # Admin configuration
│   └── urls.py         # Maintenance URLs
│
├── rental_project/     # Project settings
│   ├── settings.py     # Django settings
│   ├── urls.py         # Main URL configuration
│   ├── wsgi.py         # WSGI app
│   └── asgi.py         # ASGI app
│
├── requirements.txt    # Python dependencies
├── manage.py          # Django CLI
└── db.sqlite3         # SQLite database
```

---

## 🔄 Features Implemented

### Authentication
- Session-based authentication
- User registration endpoints
- Custom user roles

### Authorization
- Role-based filtering (Landlords see their properties, Tenants see their records)
- Permission controls via Django's permission system

### Search & Filtering
- Search by name, address, email
- Filter by status, date range, priority
- Ordering by multiple fields

### Pagination
- Default 10 items per page
- Customizable via page size

### Custom Actions
- Mark payments as paid
- Move out tenants
- Start/complete maintenance work
- View available units
- Property occupancy summaries

---

## 📝 Environment Configuration

Create a `.env` file for production:

```env
DEBUG=False
SECRET_KEY=your-secret-key-here
ALLOWED_HOSTS=localhost,127.0.0.1
DATABASE_URL=postgresql://user:pass@localhost/rental_db
CORS_ALLOWED_ORIGINS=http://localhost:3000
```

---

## 🛠️ Next Steps

### To Extend the Application:

1. **Add Payment Processing**
   - Integrate Stripe or PayPal
   - Add payment notifications

2. **Add Notifications**
   - Email notifications for payments
   - SMS alerts for maintenance

3. **Add Reporting**
   - Generate rent reports
   - Vacancy analysis
   - Maintenance cost reports

4. **Add Frontend**
   - React/Vue.js dashboard
   - Tenant portal
   - Property management interface

5. **Add Advanced Features**
   - Lease document generation
   - Automated payment reminders
   - Expense tracking
   - Document storage (scanned leases, etc.)

6. **Production Deployment**
   - Set up PostgreSQL database
   - Configure Gunicorn/Nginx
   - Set up Celery for async tasks
   - Add monitoring and logging

---

## 📚 Useful Django Commands

```bash
# Create migrations for changes
python manage.py makemigrations

# Apply migrations
python manage.py migrate

# Create superuser
python manage.py createsuperuser

# Access Django shell
python manage.py shell

# Collect static files (production)
python manage.py collectstatic

# Run tests
python manage.py test

# Check for issues
python manage.py check

# Dump data
python manage.py dumpdata > data.json

# Load data
python manage.py loaddata data.json
```

---

## 🐛 Troubleshooting

### Server won't start
- Check for syntax errors: `python manage.py check`
- Ensure migrations are applied: `python manage.py migrate`
- Check port 8000 is not in use

### Import errors
- Ensure virtual environment is activated
- Run `pip install -r requirements.txt`

### Database issues
- Reset database: Delete `db.sqlite3` and run `migrate`
- Check for circular imports in models.py

---

## 📞 Support

For Django REST Framework documentation: https://www.django-rest-framework.org/
For Django documentation: https://docs.djangoproject.com/

Happy coding! 🎉
