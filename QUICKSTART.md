# 🚀 Quick Start Guide

## Your Rental Management API is Ready!

### 🔐 NEW: JWT Authentication Enabled!
Your API now uses **secure JWT tokens** instead of basic auth. [Learn more](JWT_AUTHENTICATION.md)

### Server Running
✅ Development server is running on `http://localhost:8000`

### Access Points

| What | URL | Purpose |
|------|-----|---------|
| **API Root** | http://localhost:8000/api/ | View all API endpoints |
| **Admin Panel** | http://localhost:8000/admin/ | Manage data directly |
| **API Auth** | http://localhost:8000/api-auth/ | Browse API (fallback auth) |

### Login Credentials
- **Admin Username:** `admin`
- **Admin Password:** (set during installation)

---

## ⚡ Quick API Test (With JWT)

### Step 1: Get Access Token
```bash
curl -X POST http://localhost:8000/api/token/ \
  -H "Content-Type: application/json" \
  -d '{"username": "admin", "password": "admin123"}'
```

Copy the `"access"` token from response.

### Step 2: Use Token to Access API
```bash
curl http://localhost:8000/api/properties/ \
  -H "Authorization: Bearer YOUR_ACCESS_TOKEN"
```

### Step 3: Create Test Data
Use Admin Panel or API to add:
- Properties
- Tenants  
- Payments
- Maintenance Requests

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

## � Authentication Endpoints

| Endpoint | Purpose |
|----------|---------|
| `POST /api/register/` | Create new user |
| `POST /api/token/` | Login & get tokens |
| `POST /api/token/refresh/` | Refresh access token |
| `GET /api/me/` | Get current user |
| `POST /api/logout/` | Logout |

**See [JWT_AUTHENTICATION.md](JWT_AUTHENTICATION.md) for detailed examples**

---

## � Documentation

- **[JWT_AUTHENTICATION.md](JWT_AUTHENTICATION.md)** - Complete JWT guide & examples
- **[API_GUIDE.md](API_GUIDE.md)** - Full endpoint reference
- **[README.md](README.md)** - Project overview
