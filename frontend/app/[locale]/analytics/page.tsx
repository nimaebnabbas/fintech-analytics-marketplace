'use client';

import { useEffect, useState } from 'react';
import PriceChart from '@/components/PriceChart';

interface AnalyticsPageProps {
  params: {
    locale: 'en' | 'fa';
  };
}

const translations = {
  en: {
    title: 'Financial Analytics',
    subtitle: 'Real-time market analysis during wartime scenarios',
    market_data: 'Market Data',
    loading: 'Loading data...',
    error: 'Failed to load market data',
  },
  fa: {
    title: 'تحلیل مالی',
    subtitle: 'تحلیل بازار بلادرنگ در سناریوهای جنگی',
    market_data: 'داده‌های بازار',
    loading: 'در حال بارگذاری...',
    error: 'بارگذاری داده ناموفق',
  },
};

export default function Analytics({ params }: AnalyticsPageProps) {
  const t = translations[params.locale];
  const [marketData, setMarketData] = useState<any>(null);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState('');

  useEffect(() => {
    fetchMarketData();
  }, []);

  const fetchMarketData = async () => {
    try {
      const response = await fetch(`${process.env.NEXT_PUBLIC_API_URL}/analytics/market-data`);
      if (!response.ok) throw new Error('Failed to fetch');
      const data = await response.json();
      setMarketData(data);
    } catch (err) {
      setError(t.error);
    } finally {
      setLoading(false);
    }
  };

  return (
    <main className={`py-16 bg-gray-50 ${params.locale === 'fa' ? 'rtl' : 'ltr'}`}>
      <div className="container mx-auto px-4">
        <h1 className="text-4xl font-bold mb-4">{t.title}</h1>
        <p className="text-xl text-gray-600 mb-8">{t.subtitle}</p>

        {loading && <p>{t.loading}</p>}
        {error && <p className="text-red-600">{error}</p>}

        {marketData && (
          <div className="grid grid-cols-1 md:grid-cols-2 gap-8">
            {/* Charts will be rendered here */}
            <PriceChart
              data={marketData.gold || []}
              title="Gold Price"
              currency="USD"
            />
          </div>
        )}
      </div>
    </main>
  );
}
