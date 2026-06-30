# Deployment Guide

## Production Checklist

### Backend
- [ ] Set `SECRET_KEY` to a strong random string
- [ ] Set `ALGORITHM` to HS256 or RS256
- [ ] Configure `DATABASE_URL` to production PostgreSQL
- [ ] Set `FRONTEND_URL` to production domain
- [ ] Configure payment gateway credentials:
  - [ ] `ZARINPAL_MERCHANT_ID`
  - [ ] `CRYPTO_API_KEY`
- [ ] Set `METALS_API_KEY` and `FINNHUB_API_KEY`
- [ ] Enable HTTPS/SSL
- [ ] Set up rate limiting
- [ ] Configure logging

### Frontend
- [ ] Set `NEXT_PUBLIC_API_URL` to production backend URL
- [ ] Configure domain in `next.config.js`
- [ ] Set up CDN for static assets
- [ ] Configure DNS records
- [ ] Set up SSL certificate

## Docker Deployment

```bash
# Build images
docker-compose build

# Start services
docker-compose up -d

# Check logs
docker-compose logs -f
```

## Environment Variables

Create `.env` file:

```env
# Database
DATABASE_URL=postgresql://user:password@db:5432/fintech_db

# API Keys
METALS_API_KEY=your_key
FINNHUB_API_KEY=your_key

# Payment
ZARINPAL_MERCHANT_ID=your_id
CRYPTO_API_KEY=your_key

# Security
SECRET_KEY=generate_with_openssl_rand_hex(32)
ALGORITHM=HS256

# URLs
FRONTEND_URL=https://your-domain.com
NEXT_PUBLIC_API_URL=https://api.your-domain.com
```

## Scaling

### Horizontal Scaling
- Use load balancer (nginx, Cloudflare)
- Multiple backend instances
- Connection pooling for database

### Vertical Scaling
- Increase server resources
- Optimize queries with indexes
- Implement caching (Redis)

## Monitoring

- Set up application monitoring (Sentry)
- Database monitoring
- API performance tracking
- Error logging

## Backup & Recovery

- Daily database backups
- Version control for code
- Document recovery procedures
