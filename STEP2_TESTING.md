# Step 2: Testing & Validation

Your API is ready! Let's verify everything works with real data.

## 🧪 Quick API Tests

### 1. Get JWT Token (Login)

**Request:**
```bash
curl -X POST http://localhost:8000/api/token/ \
  -H "Content-Type: application/json" \
  -d '{"username": "landlord1", "password": "password123"}'
```

**Save the `access` token** from the response.

### 2. Test: Get All Properties (As Landlord)

```bash
curl http://localhost:8000/api/properties/ \
  -H "Authorization: Bearer YOUR_ACCESS_TOKEN"
```

**Expected:** List of 2 properties (Downtown Apartments, Riverside Condos)

### 3. Test: Get All Units

```bash
curl http://localhost:8000/api/units/ \
  -H "Authorization: Bearer YOUR_ACCESS_TOKEN"
```

**Expected:** 4 units with rent amounts and availability

### 4. Test: Get All Payments

```bash
curl http://localhost:8000/api/payments/ \
  -H "Authorization: Bearer YOUR_ACCESS_TOKEN"
```

**Expected:** 2 payments (one paid, one pending)

### 5. Test: Get All Tenants

```bash
curl http://localhost:8000/api/tenants/ \
  -H "Authorization: Bearer YOUR_ACCESS_TOKEN"
```

**Expected:** 2 active tenants with lease info

### 6. Test: Get Maintenance Requests

```bash
curl http://localhost:8000/api/maintenance/requests/ \
  -H "Authorization: Bearer YOUR_ACCESS_TOKEN"
```

**Expected:** 2 maintenance requests

---

## 👤 Test as Tenant (Different Permissions)

**Login as Tenant:**
```bash
curl -X POST http://localhost:8000/api/token/ \
  -H "Content-Type: application/json" \
  -d '{"username": "tenant1", "password": "password123"}'
```

**Try to get properties:**
```bash
curl http://localhost:8000/api/properties/ \
  -H "Authorization: Bearer TENANT_TOKEN"
```

**Note:** Tenants can see properties but can only manage their own records.

---

## 🕸️ Advanced API Tests

### Create New Unit

```bash
curl -X POST http://localhost:8000/api/units/ \
  -H "Authorization: Bearer LANDLORD_TOKEN" \
  -H "Content-Type: application/json" \
  -d '{
    "property": 1,
    "unit_number": "104",
    "rent_amount": 1500.00,
    "bedrooms": 2,
    "bathrooms": 1,
    "square_feet": 900,
    "is_available": true,
    "features": "New unit, recently renovated"
  }'
```

### Mark Payment as Paid

```bash
curl -X POST http://localhost:8000/api/payments/2/mark_paid/ \
  -H "Authorization: Bearer LANDLORD_TOKEN" \
  -H "Content-Type: application/json"
```

### Start Maintenance Work

```bash
curl -X POST http://localhost:8000/api/maintenance/requests/1/start_work/ \
  -H "Authorization: Bearer MAINTENANCE_TOKEN" \
  -H "Content-Type: application/json"
```

### Complete Maintenance Request

```bash
curl -X POST http://localhost:8000/api/maintenance/requests/1/complete/ \
  -H "Authorization: Bearer MAINTENANCE_TOKEN" \
  -H "Content-Type: application/json" \
  -d '{
    "completion_notes": "Fixed leaky faucet, tested thoroughly"
  }'
```

---

## 🖥️ Admin Panel Testing

1. Go to: `http://localhost:8000/admin/`
2. Login with: `admin` / `admin123`
3. Explore:
   - Users (see all roles)
   - Properties & Units
   - Tenants & Leases
   - Payments
   - Maintenance Requests

---

## ✅ Validation Checklist

- [ ] Login works with JWT token
- [ ] Can view properties as landlord
- [ ] Can view only own records as tenant
- [ ] Can create new property/unit
- [ ] Can mark payment as paid
- [ ] Can start maintenance work
- [ ] Admin panel displays all data
- [ ] Token refresh works
- [ ] Logout endpoint responds

---

## 📊 Sample Data Overview

**Test Users:**
| Username | Password | Role |
|----------|----------|------|
| admin | admin123 | Admin |
| landlord1 | password123 | Landlord |
| tenant1 | password123 | Tenant |
| tenant2 | password123 | Tenant |
| maintenance1 | password123 | Maintenance |

**Properties:**
- Downtown Apartments (4 units)
- Riverside Condos (6 units)

**Tenants:**
- Alice Johnson (Unit 101 - Active)
- Bob Williams (Unit 102 - Active)

**Payments:**
- Payment 1: Paid (Alice's rent)
- Payment 2: Pending (Bob's rent)

**Maintenance:**
- Fix leaky faucet (In Progress)
- Paint hallway (Open)

---

## 🚀 Next: What's After Step 2?

Once you verify the API works:

**Step 3 Options:**
1. **Frontend Dashboard** - Build React/Vue interface
2. **Email Notifications** - Add payment reminders
3. **Advanced Reports** - Financial dashboards
4. **Mobile App** - iOS/Android with same API
5. **Deployment** - Deploy to production (Heroku, AWS, Azure)
6. **Testing Suite** - Add unit & integration tests

Let me know which direction you want to go! 🎯
