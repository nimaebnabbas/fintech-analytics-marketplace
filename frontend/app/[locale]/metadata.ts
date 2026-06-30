import type { Metadata } from 'next';

export const generateMetadata = (locale: 'en' | 'fa'): Metadata => {
  const isFA = locale === 'fa';
  
  return {
    title: isFA ? 'بازار تحلیل فناوری مالی' : 'FinTech Analytics Marketplace',
    description: isFA 
      ? 'تحلیل روانشناسی سیاسی و معاملات فلزات گران‌بها'
      : 'Political psychology analysis and precious metals trading platform',
    keywords: isFA
      ? ['تحلیل بازار', 'فلزات گران‌بها', 'طلا', 'نقره', 'اقتصاد']
      : ['market analysis', 'precious metals', 'gold', 'silver', 'economics'],
    canonical: `https://fintech-analytics.com/${locale}`,
    alternates: {
      languages: {
        en: 'https://fintech-analytics.com/en',
        fa: 'https://fintech-analytics.com/fa',
      },
    },
    openGraph: {
      title: isFA ? 'بازار تحلیل فناوری مالی' : 'FinTech Analytics Marketplace',
      description: isFA 
        ? 'تحلیل روانشناسی سیاسی و معاملات فلزات گران‌بها'
        : 'Political psychology analysis and precious metals trading platform',
      type: 'website',
      url: `https://fintech-analytics.com/${locale}`,
      locale: isFA ? 'fa_IR' : 'en_US',
      images: [{
        url: 'https://fintech-analytics.com/og-image.jpg',
        width: 1200,
        height: 630,
      }],
    },
    twitter: {
      card: 'summary_large_image',
      title: isFA ? 'بازار تحلیل فناوری مالی' : 'FinTech Analytics Marketplace',
      description: isFA 
        ? 'تحلیل روانشناسی سیاسی و معاملات فلزات گران‌بها'
        : 'Political psychology analysis and precious metals trading platform',
      images: ['https://fintech-analytics.com/twitter-image.jpg'],
    },
  };
};

export const generateSchemaOrg = (locale: 'en' | 'fa') => {
  return {
    '@context': 'https://schema.org',
    '@type': 'Organization',
    name: 'FinTech Analytics Marketplace',
    url: 'https://fintech-analytics.com',
    logo: 'https://fintech-analytics.com/logo.png',
    description: locale === 'fa'
      ? 'تحلیل روانشناسی سیاسی و معاملات فلزات گران‌بها'
      : 'Political psychology analysis and precious metals trading platform',
    sameAs: [
      'https://twitter.com/fintech',
      'https://linkedin.com/company/fintech',
    ],
    contactPoint: {
      '@type': 'ContactPoint',
      contactType: 'Customer Service',
      email: 'support@fintech-analytics.com',
    },
  };
};
