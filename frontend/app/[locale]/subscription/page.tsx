'use client';

import { useEffect, useState } from 'react';
import SubscriptionCard from '@/components/SubscriptionCard';

interface SubscriptionPageProps {
  params: {
    locale: 'en' | 'fa';
  };
}

const translations = {
  en: {
    title: 'Subscription Plans',
    subtitle: 'Choose the perfect plan for your needs',
    loading: 'Loading plans...',
    error: 'Failed to load subscription plans',
  },
  fa: {
    title: 'طرح‌های اشتراک',
    subtitle: 'طرح مناسب برای نیازهای خود را انتخاب کنید',
    loading: 'در حال بارگذاری...',
    error: 'بارگذاری طرح‌ها ناموفق',
  },
};

export default function Subscription({ params }: SubscriptionPageProps) {
  const t = translations[params.locale];
  const [packages, setPackages] = useState<any[]>([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState('');

  useEffect(() => {
    fetchPackages();
  }, []);

  const fetchPackages = async () => {
    try {
      const response = await fetch(
        `${process.env.NEXT_PUBLIC_API_URL}/subscriptions/packages?language=${params.locale}`
      );
      if (!response.ok) throw new Error('Failed to fetch');
      const data = await response.json();
      setPackages(data.packages || []);
    } catch (err) {
      setError(t.error);
    } finally {
      setLoading(false);
    }
  };

  const handleSubscribe = (packageId: string) => {
    console.log('Subscribing to:', packageId);
    // TODO: Implement subscription logic
  };

  return (
    <main className={`py-16 bg-gray-50 ${params.locale === 'fa' ? 'rtl' : 'ltr'}`}>
      <div className="container mx-auto px-4">
        <h1 className="text-4xl font-bold mb-4 text-center">{t.title}</h1>
        <p className="text-xl text-gray-600 mb-12 text-center">{t.subtitle}</p>

        {loading && <p className="text-center">{t.loading}</p>}
        {error && <p className="text-center text-red-600">{error}</p>}

        {packages.length > 0 && (
          <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-5 gap-6">
            {packages.map((pkg) => (
              <SubscriptionCard
                key={pkg.id}
                package={pkg}
                language={params.locale}
                onSubscribe={handleSubscribe}
              />
            ))}
          </div>
        )}
      </div>
    </main>
  );
}
