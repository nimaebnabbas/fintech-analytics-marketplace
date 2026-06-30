'use client';

import { Check } from 'lucide-react';

interface SubscriptionPackage {
  id: string;
  name_en: string;
  name_fa: string;
  price_usd: number;
  price_rial: number;
  tier_level: number;
  features_en: string[];
  features_fa: string[];
}

interface SubscriptionCardProps {
  package: SubscriptionPackage;
  language: 'en' | 'fa';
  onSubscribe: (packageId: string) => void;
}

export default function SubscriptionCard({
  package: pkg,
  language,
  onSubscribe,
}: SubscriptionCardProps) {
  const isPopular = pkg.tier_level === 3; // Middle package is popular
  const name = language === 'en' ? pkg.name_en : pkg.name_fa;
  const features = language === 'en' ? pkg.features_en : pkg.features_fa;
  const price = language === 'en' ? `$${pkg.price_usd}` : `${pkg.price_rial.toLocaleString()} ریال`;
  const period = language === 'en' ? '/month' : '/ماهانه';

  return (
    <div
      className={`rounded-lg shadow-lg overflow-hidden transition transform hover:scale-105 ${
        isPopular ? 'ring-2 ring-blue-600 scale-105' : ''
      } ${language === 'fa' ? 'rtl' : 'ltr'}`}
    >
      {/* Header */}
      <div className={`p-6 ${
        isPopular ? 'bg-gradient-to-r from-blue-600 to-blue-700' : 'bg-gray-100'
      }`}>
        {isPopular && (
          <span className="inline-block bg-yellow-400 text-gray-900 px-3 py-1 rounded-full text-xs font-bold mb-2">
            {language === 'en' ? 'Most Popular' : 'محبوب‌ترین'}
          </span>
        )}
        <h3 className={`text-2xl font-bold ${isPopular ? 'text-white' : 'text-gray-900'}`}>
          {name}
        </h3>
      </div>

      {/* Price */}
      <div className="p-6 bg-white">
        <div className="text-center mb-6">
          <p className={`text-4xl font-bold ${
            isPopular ? 'text-blue-600' : 'text-gray-900'
          }`}>
            {price}
          </p>
          <p className="text-gray-600 text-sm">{period}</p>
        </div>

        {/* Features */}
        <ul className="space-y-3 mb-6">
          {features.map((feature, idx) => (
            <li key={idx} className="flex items-start">
              <Check className="w-5 h-5 text-green-600 mr-3 flex-shrink-0 mt-0.5" />
              <span className="text-gray-700">{feature}</span>
            </li>
          ))}
        </ul>

        {/* Button */}
        <button
          onClick={() => onSubscribe(pkg.id)}
          className={`w-full py-3 rounded font-semibold transition ${
            isPopular
              ? 'bg-blue-600 hover:bg-blue-700 text-white'
              : 'bg-gray-200 hover:bg-gray-300 text-gray-900'
          }`}
        >
          {language === 'en' ? 'Subscribe Now' : 'اشتراک‌گذاری الان'}
        </button>
      </div>
    </div>
  );
}
