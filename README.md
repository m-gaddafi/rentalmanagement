# Rental Management System

A comprehensive Django REST Framework API for managing rental properties, tenants, payments, and maintenance requests.

## 🚀 Quick Start

Get started immediately with our [Quick Start Guide](QUICKSTART.md)

## 📚 Documentation

- **[API Guide](API_GUIDE.md)** - Complete API reference and endpoints
- **[Quick Start](QUICKSTART.md)** - Fast setup and common tasks

## ✨ Features

- **Property Management** - Track multiple properties and units
- **Tenant Management** - Manage leases and tenant information
- **Payment Tracking** - Record and track rent payments
- **Maintenance Requests** - Submit and track maintenance issues
- **Role-Based Access** - Different views for landlords, tenants, and staff
- **REST API** - Full REST API with filtering, searching, and pagination
- **Admin Panel** - Django admin interface for easy data management

## 🛠️ Tech Stack

- Python 3.x
- Django 6.0.7
- Django REST Framework 3.14.0
- SQLite (development) / PostgreSQL (production)

## 📦 Installation

1. Clone the repository:
```bash
git clone <repo-url>
cd rentalmanagement
```

2. Create and activate virtual environment:
```bash
python -m venv .venv
.\.venv\Scripts\Activate.ps1  # Windows
source .venv/bin/activate      # Linux/Mac
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Run migrations:
```bash
python manage.py migrate
```

5. Create superuser:
```bash
python manage.py createsuperuser
```

6. Start server:
```bash
python manage.py runserver 8000
```

## 🌐 Access the Application

- **API**: http://localhost:8000/api/
- **Admin Panel**: http://localhost:8000/admin/
- **API Documentation**: http://localhost:8000/api/ (browsable API)

## 📖 API Endpoints

### Core Endpoints
- `/api/users/` - User management
- `/api/properties/` - Property management
- `/api/units/` - Rental units
- `/api/tenants/` - Tenant management
- `/api/payments/` - Payment tracking
- `/api/maintenance/requests/` - Maintenance requests

See [API_GUIDE.md](API_GUIDE.md) for complete endpoint documentation.

## 🔐 Security

This project is configured for development. For production deployment:
- Change SECRET_KEY in settings
- Set DEBUG=False
- Use PostgreSQL or production database
- Configure ALLOWED_HOSTS
- Set up HTTPS

See [API_GUIDE.md](API_GUIDE.md#production-deployment) for details.

## 💡 Example Usage

### Create a Property
```bash
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

### Get All Properties
```bash
curl http://localhost:8000/api/properties/ -u admin:password
```

## 📝 Project Structure

```
rentalmanagement/
├── user/              # User management app
├── properties/        # Property and unit management
├── tenants/          # Tenant management
├── payments/         # Payment tracking
├── maintenance/      # Maintenance requests
├── rental_project/   # Main project settings
├── manage.py         # Django CLI
├── requirements.txt  # Dependencies
├── API_GUIDE.md      # Complete API documentation
└── QUICKSTART.md     # Quick start guide
```

## 🚀 Next Steps

1. Read the [Quick Start Guide](QUICKSTART.md)
2. Explore the [API Guide](API_GUIDE.md)
3. Add sample data in the admin panel
4. Test API endpoints
5. Customize for your needs

## 📞 Support

For issues or questions:
- Check the [API Guide](API_GUIDE.md#troubleshooting)
- Review [Django documentation](https://docs.djangoproject.com/)
- Check [Django REST Framework docs](https://www.django-rest-framework.org/)

## 📄 License

This project is open source. Modify and use as needed.

---

**Built with Django REST Framework**
 
