# JWT Authentication Guide

Your API now uses **JWT (JSON Web Token)** authentication for better security and scalability!

## 🔐 How JWT Works

1. **Register** - Create a user account
2. **Login** - Exchange credentials for access token + refresh token
3. **Access API** - Include access token in request headers
4. **Refresh** - When access token expires, use refresh token to get a new one

---

## 🚀 Getting Started

### 1. Register a New User

```bash
curl -X POST http://localhost:8000/api/register/ \
  -H "Content-Type: application/json" \
  -d '{
    "username": "john_landlord",
    "email": "john@example.com",
    "password": "secure_password123",
    "first_name": "John",
    "last_name": "Doe",
    "role": "landlord"
  }'
```

**Response:**
```json
{
  "message": "User registered successfully",
  "user": {
    "id": 2,
    "username": "john_landlord",
    "email": "john@example.com",
    ...
  }
}
```

### 2. Login & Get Tokens

```bash
curl -X POST http://localhost:8000/api/token/ \
  -H "Content-Type: application/json" \
  -d '{
    "username": "john_landlord",
    "password": "secure_password123"
  }'
```

**Response:**
```json
{
  "access": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9...",
  "refresh": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9...",
  "user": {
    "id": 2,
    "username": "john_landlord",
    "email": "john@example.com",
    "role": "landlord"
  }
}
```

**Save these tokens!**
- `access` - Use for API requests (expires in 1 hour)
- `refresh` - Use to get new access token (expires in 7 days)

### 3. Use Access Token to Make API Requests

```bash
curl http://localhost:8000/api/properties/ \
  -H "Authorization: Bearer YOUR_ACCESS_TOKEN"
```

**Response:** List of properties

---

## 🔄 Refresh Access Token

When your access token expires:

```bash
curl -X POST http://localhost:8000/api/token/refresh/ \
  -H "Content-Type: application/json" \
  -d '{
    "refresh": "YOUR_REFRESH_TOKEN"
  }'
```

**Response:**
```json
{
  "access": "NEW_ACCESS_TOKEN",
  "refresh": "NEW_REFRESH_TOKEN"
}
```

---

## 👤 Get Current User Info

```bash
curl http://localhost:8000/api/me/ \
  -H "Authorization: Bearer YOUR_ACCESS_TOKEN"
```

**Response:**
```json
{
  "id": 2,
  "username": "john_landlord",
  "email": "john@example.com",
  "first_name": "John",
  "last_name": "Doe",
  "role": "landlord",
  "phone": "",
  "address": "",
  ...
}
```

---

## 🚪 Logout

```bash
curl -X POST http://localhost:8000/api/logout/ \
  -H "Authorization: Bearer YOUR_ACCESS_TOKEN"
```

---

## 📋 All Authentication Endpoints

| Endpoint | Method | Purpose | Auth Required |
|----------|--------|---------|---|
| `/api/register/` | POST | Register new user | ❌ No |
| `/api/token/` | POST | Login & get tokens | ❌ No |
| `/api/token/refresh/` | POST | Refresh access token | ❌ No |
| `/api/me/` | GET | Get current user | ✅ Yes |
| `/api/logout/` | POST | Logout | ✅ Yes |

---

## 🔑 Token Configuration

**Current Settings:**
- Access Token Lifetime: **1 hour**
- Refresh Token Lifetime: **7 days**
- Algorithm: **HS256 (HMAC with SHA-256)**

To modify in `settings.py`:
```python
SIMPLE_JWT = {
    'ACCESS_TOKEN_LIFETIME': timedelta(hours=1),
    'REFRESH_TOKEN_LIFETIME': timedelta(days=7),
    ...
}
```

---

## 🛡️ Best Practices

### 1. Store Tokens Safely
- **Access Token**: Keep in memory only (shorter lifetime = safer)
- **Refresh Token**: Store in secure httpOnly cookie or localStorage

### 2. Include Token in Requests
```bash
Authorization: Bearer <ACCESS_TOKEN>
```

### 3. Handle Token Expiration
- Catch 401 Unauthorized response
- Automatically refresh token
- Retry the request
- If refresh fails, redirect to login

### 4. Logout Properly
- Delete tokens from storage
- Make logout API call
- Redirect to login page

---

## 🧪 Test with Postman

1. **Register**
   - POST to `http://localhost:8000/api/register/`
   - Body: JSON with credentials

2. **Login**
   - POST to `http://localhost:8000/api/token/`
   - Body: `{"username": "...", "password": "..."}`
   - Save `access` token

3. **Use Token**
   - GET `http://localhost:8000/api/properties/`
   - Headers: `Authorization: Bearer <YOUR_TOKEN>`

---

## 🧠 Example Frontend Implementation (React)

```javascript
// Login
async function login(username, password) {
  const response = await fetch('http://localhost:8000/api/token/', {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify({ username, password })
  });
  
  const data = await response.json();
  localStorage.setItem('accessToken', data.access);
  localStorage.setItem('refreshToken', data.refresh);
  return data.user;
}

// Make API Request
async function fetchProperties() {
  const token = localStorage.getItem('accessToken');
  const response = await fetch('http://localhost:8000/api/properties/', {
    headers: {
      'Authorization': `Bearer ${token}`
    }
  });
  
  if (response.status === 401) {
    // Token expired, refresh it
    await refreshToken();
    // Retry request
    return fetchProperties();
  }
  
  return response.json();
}

// Refresh Token
async function refreshToken() {
  const refreshToken = localStorage.getItem('refreshToken');
  const response = await fetch('http://localhost:8000/api/token/refresh/', {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify({ refresh: refreshToken })
  });
  
  const data = await response.json();
  localStorage.setItem('accessToken', data.access);
  localStorage.setItem('refreshToken', data.refresh);
}
```

---

## 🔗 API Endpoints (with JWT)

All endpoints require `Authorization: Bearer <TOKEN>` header except:
- `/api/register/` - Registration
- `/api/token/` - Login
- `/api/token/refresh/` - Token refresh

### Example:
```bash
curl -H "Authorization: Bearer eyJ0eXAiOiJKV1QiLCJhbGc..." \
  http://localhost:8000/api/properties/
```

---

## ⚠️ Troubleshooting

**Invalid token / Token is invalid or expired**
- Check token syntax (should start with "Bearer ")
- Refresh the token if expired
- Re-login if refresh token expired

**401 Unauthorized**
- Token is missing or invalid
- Token has expired
- User doesn't have permission

**400 Bad Request on login**
- Wrong username or password
- User doesn't exist
- Check JSON format

---

## 📚 Further Reading

- [JWT.io](https://jwt.io/) - JWT Playground & Debugger
- [DRF SimpleJWT Docs](https://django-rest-framework-simplejwt.readthedocs.io/)
- [OAuth 2.0 vs JWT](https://auth0.com/blog/oauth-2-vs-jwt/)

---

**Your API is now production-ready with secure JWT authentication!** 🎉
