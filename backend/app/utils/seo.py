"""SEO utilities for meta tags and structured data"""
from typing import Dict, Optional
import json

class SEOHelper:
    """Helper for SEO optimization"""
    
    @staticmethod
    def generate_product_schema(product: Dict) -> str:
        """
        Generate Schema.org Product structured data
        """
        schema = {
            "@context": "https://schema.org/",
            "@type": "Product",
            "name": product.get("name_en"),
            "description": product.get("description_en"),
            "image": product.get("image_url"),
            "brand": {
                "@type": "Brand",
                "name": "FinTech Analytics Marketplace"
            },
            "offers": {
                "@type": "Offer",
                "url": product.get("url"),
                "priceCurrency": "USD",
                "price": str(product.get("current_price_usd"))
            }
        }
        return json.dumps(schema)
    
    @staticmethod
    def generate_article_schema(article: Dict) -> str:
        """
        Generate Schema.org Article structured data
        """
        schema = {
            "@context": "https://schema.org",
            "@type": "Article",
            "headline": article.get("title_en"),
            "description": article.get("summary_en"),
            "image": article.get("image_url"),
            "author": {
                "@type": "Organization",
                "name": "FinTech Analytics"
            },
            "datePublished": article.get("published_at"),
            "dateModified": article.get("updated_at")
        }
        return json.dumps(schema)
    
    @staticmethod
    def generate_organization_schema() -> str:
        """
        Generate Schema.org Organization structured data
        """
        schema = {
            "@context": "https://schema.org",
            "@type": "Organization",
            "name": "FinTech Analytics Marketplace",
            "url": "https://fintech-analytics.com",
            "logo": "https://fintech-analytics.com/logo.png",
            "description": "Bilingual financial analytics platform with precious metals marketplace",
            "sameAs": [
                "https://twitter.com/fintech",
                "https://linkedin.com/company/fintech"
            ],
            "contactPoint": {
                "@type": "ContactPoint",
                "contactType": "Customer Service",
                "email": "support@fintech-analytics.com"
            }
        }
        return json.dumps(schema)
