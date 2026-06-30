'use client';

import { useEffect, useState } from 'react';
import ProductCard from '@/components/ProductCard';

interface ShopPageProps {
  params: {
    locale: 'en' | 'fa';
  };
}

const translations = {
  en: {
    title: 'Precious Metals Shop',
    subtitle: 'Live prices updated every minute',
    category_gold: 'Gold',
    category_silver: 'Silver',
    category_platinum: 'Platinum',
    loading: 'Loading products...',
    error: 'Failed to load products',
  },
  fa: {
    title: 'فروشگاه فلزات گران‌بها',
    subtitle: 'قیمت‌های زنده که هر دقیقه بروزرسانی می‌شود',
    category_gold: 'طلا',
    category_silver: 'نقره',
    category_platinum: 'پلاتین',
    loading: 'در حال بارگذاری...',
    error: 'بارگذاری محصولات ناموفق',
  },
};

export default function Shop({ params }: ShopPageProps) {
  const t = translations[params.locale];
  const [products, setProducts] = useState<any[]>([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState('');

  useEffect(() => {
    fetchProducts();
    // Refresh prices every minute
    const interval = setInterval(fetchProducts, 60000);
    return () => clearInterval(interval);
  }, []);

  const fetchProducts = async () => {
    try {
      const response = await fetch(`${process.env.NEXT_PUBLIC_API_URL}/products/`);
      if (!response.ok) throw new Error('Failed to fetch');
      const data = await response.json();
      setProducts(data.products || []);
    } catch (err) {
      setError(t.error);
    } finally {
      setLoading(false);
    }
  };

  const handleAddToCart = (productId: string) => {
    console.log('Added to cart:', productId);
    // TODO: Implement cart logic
  };

  return (
    <main className={`py-16 bg-gray-50 ${params.locale === 'fa' ? 'rtl' : 'ltr'}`}>
      <div className="container mx-auto px-4">
        <h1 className="text-4xl font-bold mb-4">{t.title}</h1>
        <p className="text-xl text-gray-600 mb-8">{t.subtitle}</p>

        {loading && <p>{t.loading}</p>}
        {error && <p className="text-red-600">{error}</p>}

        {products.length > 0 && (
          <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-8">
            {products.map((product) => (
              <ProductCard
                key={product.id}
                id={product.id}
                name={params.locale === 'en' ? product.name_en : product.name_fa}
                metal_type={product.metal_type}
                current_price_usd={product.current_price_usd}
                current_price_rial={product.current_price_rial}
                purity_percentage={product.purity_percentage}
                weight_grams={product.weight_grams}
                is_available={product.is_available}
                onAddToCart={handleAddToCart}
                language={params.locale}
              />
            ))}
          </div>
        )}
      </div>
    </main>
  );
}
