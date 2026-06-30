# FinTech Analytics Marketplace 🚀

**Bilingual (Farsi/English) Platform for Financial Analysis, Precious Metals Trading & Market Intelligence**

## Features

### 📊 Analytical Section
- Real-time financial market analysis based on political psychology
- Charts for major financial markets during conflict scenarios
- 5 subscription packages (Basic → Elite)
- **Pricing:**
  - Farsi: 5M ریال → 15M ریال (monthly)
  - English: $10 → $100 USD (monthly)

### 🏪 E-Commerce Section
- Precious metals marketplace (Gold, Silver, Platinum)
- Dynamic pricing based on real-time commodity data
- E-catalog with detailed product information

### 🏢 Corporate Section
- Company information
- Contact forms
- Terms & Conditions
- Multi-language support

## Tech Stack

### Backend
- **Framework:** FastAPI (Python)
- **Database:** PostgreSQL
- **API Authentication:** JWT
- **Payment Gateway:** Zarinpal (Rial) + Crypto (Tether - Coming Soon)

### Frontend
- **Framework:** Next.js 14
- **UI:** Tailwind CSS
- **Internationalization:** next-i18n-router + i18next
- **Charts:** Recharts
- **Language:** TypeScript

### External APIs
- **Metals Pricing:** Metals API / Alpha Vantage
- **Financial Markets:** Finnhub (Wartime scenarios)
- **Cryptocurrency:** CoinGecko API

## Project Structure

```
fintech-analytics-marketplace/
├── backend/
│   ├── app/
│   │   ├── main.py
│   │   ├── models/
│   │   ├── routes/
│   │   ├── services/
│   │   └── utils/
│   ├── requirements.txt
│   ├── .env.example
│   └── Dockerfile
├── frontend/
│   ├── pages/
│   ├── components/
│   ├── public/
│   ├── styles/
│   ├── package.json
│   └── next.config.js
├── docker-compose.yml
└── README.md
```

## Installation & Setup

### Prerequisites
- Python 3.11+
- Node.js 18+
- PostgreSQL 15+
- Docker & Docker Compose (optional)

### Quick Start (Docker)
```bash
git clone https://github.com/nimaebnabbas/fintech-analytics-marketplace.git
cd fintech-analytics-marketplace
docker-compose up
```

### Manual Setup

#### Backend
```bash
cd backend
pip install -r requirements.txt
cp .env.example .env
# Configure .env with your API keys
python -m uvicorn app.main:app --reload
```

#### Frontend
```bash
cd frontend
npm install
npm run dev
```

**Access:**
- Frontend: http://localhost:3000
- Backend: http://localhost:8000
- API Docs: http://localhost:8000/docs

## SEO Optimization
- ✅ Server-side rendering (Next.js)
- ✅ Automatic sitemap generation
- ✅ Meta tags & Open Graph
- ✅ Structured data (Schema.org)
- ✅ Performance optimization (Core Web Vitals)
- ✅ Mobile-first responsive design
- ✅ Multi-language support (hreflang)

## Roadmap

- [ ] Phase 1: Core platform setup (Week 1-2)
- [ ] Phase 2: Analytics & subscription system (Week 2-3)
- [ ] Phase 3: E-commerce & payment integration (Week 3)
- [ ] Phase 4: SEO & Optimization (Week 4)
- [ ] Phase 5: Testing & Deployment
- [ ] Phase 6: Cryptocurrency payment gateway
- [ ] Phase 7: Wallet integration

## Environment Variables

See `.env.example` for required configuration.

## API Documentation

Automatic API docs available at: `/docs` (Swagger UI)

## License

MIT License - See LICENSE file

## Support

For issues and feature requests, please create an issue on GitHub.

---

**Created with ❤️ for financial intelligence in uncertain times**
