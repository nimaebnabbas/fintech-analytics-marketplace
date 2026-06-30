'use client';

interface ProductCardProps {
  id: string;
  name: string;
  metal_type: string;
  current_price_usd: number;
  current_price_rial: number;
  purity_percentage: number;
  weight_grams: number;
  is_available: boolean;
  onAddToCart: (id: string) => void;
  language: 'en' | 'fa';
}

export default function ProductCard({
  id,
  name,
  metal_type,
  current_price_usd,
  current_price_rial,
  purity_percentage,
  weight_grams,
  is_available,
  onAddToCart,
  language,
}: ProductCardProps) {
  const metalLabels = {
    en: {
      gold: 'Gold',
      silver: 'Silver',
      platinum: 'Platinum',
      palladium: 'Palladium',
    },
    fa: {
      gold: 'طلا',
      silver: 'نقره',
      platinum: 'پلاتین',
      palladium: 'پالادیوم',
    },
  };

  return (
    <div className={`bg-white rounded-lg shadow-lg overflow-hidden hover:shadow-xl transition ${
      language === 'fa' ? 'rtl' : 'ltr'
    }`}>
      {/* Metal Type Badge */}
      <div className="bg-gradient-to-r from-yellow-400 to-yellow-500 text-white px-4 py-2">
        <span className="font-bold text-lg">
          {metalLabels[language][metal_type as keyof typeof metalLabels['en']]}
        </span>
      </div>

      {/* Content */}
      <div className="p-6">
        <h3 className="text-xl font-bold mb-2">{name}</h3>

        {/* Specs */}
        <div className="text-sm text-gray-600 mb-4 space-y-1">
          <p>{language === 'en' ? 'Purity' : 'خلوص'}: {purity_percentage}%</p>
          <p>{language === 'en' ? 'Weight' : 'وزن'}: {weight_grams}g</p>
        </div>

        {/* Pricing */}
        <div className="bg-gray-100 p-4 rounded mb-4">
          <p className="text-2xl font-bold text-blue-600">${current_price_usd.toFixed(2)}</p>
          <p className="text-gray-600">{current_price_rial.toLocaleString()} ریال</p>
        </div>

        {/* Availability */}
        <div className="mb-4">
          <span
            className={`px-3 py-1 rounded text-sm font-semibold ${
              is_available
                ? 'bg-green-100 text-green-700'
                : 'bg-red-100 text-red-700'
            }`}
          >
            {is_available
              ? language === 'en'
                ? 'In Stock'
                : 'موجود'
              : language === 'en'
              ? 'Out of Stock'
              : 'ناموجود'}
          </span>
        </div>

        {/* Button */}
        <button
          onClick={() => onAddToCart(id)}
          disabled={!is_available}
          className={`w-full py-2 rounded font-semibold transition ${
            is_available
              ? 'bg-blue-600 hover:bg-blue-700 text-white cursor-pointer'
              : 'bg-gray-300 text-gray-500 cursor-not-allowed'
          }`}
        >
          {language === 'en' ? 'Add to Cart' : 'افزودن به سبد'}
        </button>
      </div>
    </div>
  );
}
