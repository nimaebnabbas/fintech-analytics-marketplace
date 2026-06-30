# API Documentation

## Base URL
```
http://localhost:8000/api/v1
```

## Authentication

### Register
```http
POST /auth/register
Content-Type: application/json

{
  "email": "user@example.com",
  "username": "username",
  "password": "securepassword",
  "full_name": "Full Name",
  "language": "en"
}
```

### Login
```http
POST /auth/login
Content-Type: application/json

{
  "email": "user@example.com",
  "password": "securepassword"
}

Response:
{
  "access_token": "eyJhbGc...",
  "refresh_token": "eyJhbGc...",
  "token_type": "bearer",
  "user": {...}
}
```

## Products

### Get All Products
```http
GET /products/?skip=0&limit=20
```

### Get Product by ID
```http
GET /products/{product_id}
```

### Get Products by Category
```http
GET /products/category/{category_id}
```

## Analytics

### Get Market Data
```http
GET /analytics/market-data?language=en
```

### Get Market Data by Symbol
```http
GET /analytics/market-data/{symbol}
```

### Get Analytics Reports
```http
GET /analytics/reports?language=en&published_only=true
```

## Subscriptions

### Get Subscription Packages
```http
GET /subscriptions/packages?language=en
```

### Create Subscription
```http
POST /subscriptions/
Authorization: Bearer {access_token}
Content-Type: application/json

{
  "package_id": "uuid",
  "currency": "USD"
}
```

## Payments

### Create Zarinpal Payment
```http
POST /payments/zarinpal/create
Content-Type: application/json

{
  "order_id": "uuid",
  "amount_rial": 5000000
}
```

### Zarinpal Callback
```http
GET /payments/zarinpal/callback?authority=12345&status=OK
```

### Create Crypto Payment
```http
POST /payments/crypto/create
Content-Type: application/json

{
  "order_id": "uuid",
  "amount_usd": 100
}
```

### Get Payment Status
```http
GET /payments/status/{order_id}
```

## Orders

### Create Order
```http
POST /orders/
Authorization: Bearer {access_token}
Content-Type: application/json

{
  "items": [
    {
      "product_id": "uuid",
      "quantity": 10
    }
  ],
  "currency": "USD",
  "shipping_address": "Address here"
}
```

### Get User Orders
```http
GET /orders/user/{user_id}
Authorization: Bearer {access_token}
```

### Get Order Details
```http
GET /orders/{order_id}
Authorization: Bearer {access_token}
```
