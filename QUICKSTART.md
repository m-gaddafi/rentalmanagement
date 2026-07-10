# 🚀 Quick Start Guide

## Your Rental Management API is Ready!

### Server Running
✅ Development server is running on `http://localhost:8000`

### Access Points

| What | URL | Purpose |
|------|-----|---------|
| **API Root** | http://localhost:8000/api/ | View all API endpoints |
| **Admin Panel** | http://localhost:8000/admin/ | Manage data directly |
| **API Auth** | http://localhost:8000/api-auth/ | Login to test API |

### Credentials
- **Username:** `admin`
- **Password:** `(set during installation)`

---

## ⚡ Test the API Immediately

### 1. Open Browser
Go to: http://localhost:8000/api/

You should see the API root with all available endpoints.

### 2. Try Admin Panel
Go to: http://localhost:8000/admin/
Login with admin credentials

### 3. Create Test Data

**Method 1: Using Admin Panel (Easiest)**
1. Go to Admin → Properties → Add Property
2. Fill in the form and save
3. Go to Admin → Units → Add Unit
4. Repeat for other models

**Method 2: Using API with curl**
```bash
# Create a property
curl -X POST http://localhost:8000/api/properties/ \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer YOUR_TOKEN" \
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

## 📊 What You Can Do

### Properties Management
- ✅ Create/Edit/Delete properties
- ✅ Manage units within properties
- ✅ Track occupancy rates
- ✅ View available units

### Tenant Management
- ✅ Register new tenants
- ✅ Link tenants to units and leases
- ✅ Track lease dates and rent amounts
- ✅ Mark tenants as moved out

### Payment Tracking
- ✅ Record rent payments
- ✅ Track payment status (pending, paid, overdue)
- ✅ View overdue payments
- ✅ Record payment methods

### Maintenance
- ✅ Submit maintenance requests
- ✅ Assign to maintenance staff
- ✅ Track request status
- ✅ Record costs

---

## 🔒 Security Notes

### For Development Only
- ⚠️ Current SECRET_KEY is exposed (change in production)
- ⚠️ DEBUG=True (disable in production)
- ⚠️ SQLite database (use PostgreSQL in production)

### Create `.env` for Production
```
DEBUG=False
SECRET_KEY=your-super-secret-key
ALLOWED_HOSTS=yourdomain.com
```

---

## 📖 Full Documentation

See `API_GUIDE.md` for:
- Complete endpoint reference
- Model relationships
- Authentication details
- Custom actions
- Production deployment guide

---

## 💡 Common Tasks

### Create a New Landlord
```bash
POST /api/users/
{
  "username": "john_landlord",
  "email": "john@example.com",
  "first_name": "John",
  "last_name": "Doe",
  "password": "secure_password",
  "role": "landlord",
  "phone": "555-0123"
}
```

### Add a Property
```bash
POST /api/properties/
{
  "name": "Apartment Complex A",
  "address": "456 Oak Ave",
  "city": "Seattle",
  "state": "WA",
  "zip_code": "98101",
  "total_units": 10,
  "property_type": "apartment",
  "description": "Modern apartments",
  "amenities": "Parking, Gym, Pool"
}
```

### Record a Payment
```bash
POST /api/payments/
{
  "tenant": 1,
  "amount": "1200.00",
  "due_date": "2026-08-01",
  "status": "paid",
  "payment_method": "bank_transfer",
  "payment_date": "2026-07-28"
}
```

### Create Maintenance Request
```bash
POST /api/maintenance/requests/
{
  "property": 1,
  "title": "Fix leaky faucet",
  "description": "Kitchen sink faucet is dripping",
  "priority": "medium",
  "unit_number": "101"
}
```

---

## 🎯 Next Steps

1. **Explore Admin Panel** - Get familiar with the interface
2. **Create Sample Data** - Add a few properties and tenants
3. **Test API Endpoints** - Use curl or Postman to test
4. **Review API_GUIDE.md** - Understand all available features
5. **Customize** - Add your business logic

---

## ⚠️ Troubleshooting

**Server not starting?**
- Check port 8000 is free
- Run `python manage.py check`

**Can't access /admin?**
- Ensure superuser exists
- Run `python manage.py createsuperuser`

**Import errors?**
- Activate venv: `.\.venv\Scripts\Activate.ps1`
- Install deps: `pip install -r requirements.txt`

---

## 📝 Additional Resources

- [Django REST Framework Docs](https://www.django-rest-framework.org/)
- [Django Documentation](https://docs.djangoproject.com/)
- [DRF Tutorial](https://www.django-rest-framework.org/tutorial/1-serialization/)

---

**Happy coding! 🎉**

Questions? Check the API_GUIDE.md for comprehensive documentation.
