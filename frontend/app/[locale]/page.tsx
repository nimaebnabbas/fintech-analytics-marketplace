'use client';

import type { Metadata } from 'next';

export const metadata: Metadata = {
  title: 'Home - FinTech Analytics Marketplace',
  description: 'Political psychology analysis and precious metals trading platform',
  openGraph: {
    title: 'FinTech Analytics Marketplace',
    description: 'Political psychology analysis and precious metals trading platform',
    type: 'website',
  },
};

interface HomePageProps {
  params: {
    locale: 'en' | 'fa';
  };
}

const translations = {
  en: {
    hero_title: 'FinTech Analytics Marketplace',
    hero_subtitle: 'Political Psychology Analysis & Precious Metals Trading',
    hero_cta: 'Get Started',
    features_title: 'Our Services',
    feature_1_title: 'Real-Time Analytics',
    feature_1_desc: 'Political psychology analysis affecting financial markets',
    feature_2_title: 'Precious Metals',
    feature_2_desc: 'Trade gold, silver, and platinum with live pricing',
    feature_3_title: 'Market Intelligence',
    feature_3_desc: 'Insights on wartime economic impacts',
  },
  fa: {
    hero_title: 'بازار تحلیل فناوری مالی',
    hero_subtitle: 'تحلیل روانشناسی سیاسی و معاملات فلزات گران‌بها',
    hero_cta: 'شروع کنید',
    features_title: 'خدمات ما',
    feature_1_title: 'تحلیل بلادرنگ',
    feature_1_desc: 'تحلیل روانشناختی سیاسی تاثیرگذار بر بازارهای مالی',
    feature_2_title: 'فلزات گران‌بها',
    feature_2_desc: 'معاملات طلا، نقره و پلاتین با قیمت زنده',
    feature_3_title: 'اطلاعات بازار',
    feature_3_desc: 'بینش‌ها درباره تاثیرات اقتصادی جنگ',
  },
};

export default function Home({ params }: HomePageProps) {
  const t = translations[params.locale];
  const isRTL = params.locale === 'fa';

  return (
    <main className={`${isRTL ? 'rtl' : 'ltr'}`}>
      {/* Hero Section */}
      <section className="bg-gradient-to-r from-gray-900 to-gray-800 text-white py-20">
        <div className="container mx-auto px-4 text-center">
          <h1 className="text-5xl font-bold mb-4">{t.hero_title}</h1>
          <p className="text-xl text-gray-300 mb-8">{t.hero_subtitle}</p>
          <button className="bg-blue-600 hover:bg-blue-700 text-white px-8 py-3 rounded-lg font-semibold transition">
            {t.hero_cta}
          </button>
        </div>
      </section>

      {/* Features Section */}
      <section className="py-16 bg-gray-50">
        <div className="container mx-auto px-4">
          <h2 className="text-4xl font-bold text-center mb-12">{t.features_title}</h2>
          <div className="grid grid-cols-1 md:grid-cols-3 gap-8">
            {/* Feature 1 */}
            <div className="bg-white p-8 rounded-lg shadow-lg text-center">
              <div className="text-4xl mb-4">📊</div>
              <h3 className="text-xl font-bold mb-2">{t.feature_1_title}</h3>
              <p className="text-gray-600">{t.feature_1_desc}</p>
            </div>

            {/* Feature 2 */}
            <div className="bg-white p-8 rounded-lg shadow-lg text-center">
              <div className="text-4xl mb-4">💎</div>
              <h3 className="text-xl font-bold mb-2">{t.feature_2_title}</h3>
              <p className="text-gray-600">{t.feature_2_desc}</p>
            </div>

            {/* Feature 3 */}
            <div className="bg-white p-8 rounded-lg shadow-lg text-center">
              <div className="text-4xl mb-4">🎯</div>
              <h3 className="text-xl font-bold mb-2">{t.feature_3_title}</h3>
              <p className="text-gray-600">{t.feature_3_desc}</p>
            </div>
          </div>
        </div>
      </section>
    </main>
  );
}
