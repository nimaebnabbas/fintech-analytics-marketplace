/** @type {import('next').NextConfig} */
const nextConfig = {
  reactStrictMode: true,
  i18n: {
    locales: ['en', 'fa'],
    defaultLocale: 'en',
  },
  images: {
    unoptimized: true,
  },
  // SEO Optimization
  compress: true,
  productionBrowserSourceMaps: false,
  swcMinify: true,
};

module.exports = nextConfig;