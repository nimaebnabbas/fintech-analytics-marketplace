"""Updated main.py with all routes"""
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from dotenv import load_dotenv
import os

# Import routes
from app.routes import auth, products, orders, subscriptions, analytics, payments

load_dotenv()

app = FastAPI(
    title="FinTech Analytics Marketplace",
    description="Bilingual fintech platform with analytics and precious metals marketplace",
    version="0.1.0"
)

# CORS Configuration
app.add_middleware(
    CORSMiddleware,
    allow_origins=[os.getenv("FRONTEND_URL", "http://localhost:3000")],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include routers
app.include_router(auth.router, prefix="/api/v1")
app.include_router(products.router, prefix="/api/v1")
app.include_router(orders.router, prefix="/api/v1")
app.include_router(subscriptions.router, prefix="/api/v1")
app.include_router(analytics.router, prefix="/api/v1")
app.include_router(payments.router, prefix="/api/v1")

@app.get("/api/health")
async def health_check():
    """Health check endpoint"""
    return {"status": "ok", "message": "Server is running"}

@app.get("/api/v1/")
async def root():
    """Root endpoint"""
    return {
        "message": "Welcome to FinTech Analytics Marketplace",
        "version": "0.1.0",
        "languages": ["fa", "en"],
        "docs": "/docs"
    }

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(
        "main:app",
        host="0.0.0.0",
        port=8000,
        reload=True
    )
