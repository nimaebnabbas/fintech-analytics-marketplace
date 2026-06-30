import type { Metadata } from 'next';
import { i18nConfig } from '@/public/locales/i18n';

export const metadata: Metadata = {
  title: 'FinTech Analytics Marketplace',
  description: 'Political psychology analysis and precious metals marketplace',
  viewport: 'width=device-width, initial-scale=1',
  alternates: {
    languages: {
      en: 'https://fintech-analytics.com/en',
      fa: 'https://fintech-analytics.com/fa',
    },
  },
  openGraph: {
    type: 'website',
    locale: 'en_US',
    url: 'https://fintech-analytics.com',
    siteName: 'FinTech Analytics Marketplace',
  },
};

export default function RootLayout({
  children,
}: {
  children: React.ReactNode;
}) {
  return (
    <html lang="en" suppressHydrationWarning>
      <head>
        <meta charSet="utf-8" />
        <meta name="theme-color" content="#000000" />
        <link rel="canonical" href="https://fintech-analytics.com" />
      </head>
      <body>
        {children}
      </body>
    </html>
  );
}
