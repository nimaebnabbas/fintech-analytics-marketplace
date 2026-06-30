'use client';

import { usePathname, useRouter } from 'next/navigation';
import Link from 'next/link';
import { useEffect, useState } from 'react';

export default function Header() {
  const pathname = usePathname();
  const router = useRouter();
  const [isOpen, setIsOpen] = useState(false);
  const [currentLang, setCurrentLang] = useState<'en' | 'fa'>('en');
  const [isLoggedIn, setIsLoggedIn] = useState(false);

  useEffect(() => {
    // Extract language from pathname
    const lang = pathname.startsWith('/fa') ? 'fa' : 'en';
    setCurrentLang(lang);
    
    // Check if user is logged in
    const token = localStorage.getItem('token');
    setIsLoggedIn(!!token);
  }, [pathname]);

  const toggleLanguage = () => {
    const newLang = currentLang === 'en' ? 'fa' : 'en';
    const newPath = pathname.replace(/^\/[a-z]{2}/, `/${newLang}`);
    router.push(newPath);
  };

  const toggleMenu = () => {
    setIsOpen(!isOpen);
  };

  const isRTL = currentLang === 'fa';

  return (
    <header className={`bg-gray-900 text-white shadow-lg ${isRTL ? 'rtl' : 'ltr'}`}>
      <nav className="container mx-auto px-4 py-4 flex justify-between items-center">
        {/* Logo */}
        <Link href={`/${currentLang}`} className="text-2xl font-bold text-blue-400">
          FinTech
        </Link>

        {/* Desktop Menu */}
        <div className="hidden md:flex space-x-6">
          <Link href={`/${currentLang}`} className="hover:text-blue-400 transition">
            {currentLang === 'en' ? 'Home' : 'صفحه اصلی'}
          </Link>
          <Link href={`/${currentLang}/analytics`} className="hover:text-blue-400 transition">
            {currentLang === 'en' ? 'Analytics' : 'تحلیل'}
          </Link>
          <Link href={`/${currentLang}/shop`} className="hover:text-blue-400 transition">
            {currentLang === 'en' ? 'Shop' : 'فروشگاه'}
          </Link>
          <Link href={`/${currentLang}/subscription`} className="hover:text-blue-400 transition">
            {currentLang === 'en' ? 'Subscription' : 'اشتراک'}
          </Link>
        </div>

        {/* Right side */}
        <div className="flex items-center space-x-4">
          <button
            onClick={toggleLanguage}
            className="bg-blue-600 hover:bg-blue-700 px-4 py-2 rounded transition"
          >
            {currentLang === 'en' ? 'فارسی' : 'English'}
          </button>

          {isLoggedIn ? (
            <Link href={`/${currentLang}/account`} className="hover:text-blue-400">
              {currentLang === 'en' ? 'Account' : 'حساب'}
            </Link>
          ) : (
            <Link href={`/${currentLang}/login`} className="bg-green-600 hover:bg-green-700 px-4 py-2 rounded transition">
              {currentLang === 'en' ? 'Login' : 'ورود'}
            </Link>
          )}

          {/* Mobile menu button */}
          <button onClick={toggleMenu} className="md:hidden">
            <svg className="w-6 h-6" fill="none" stroke="currentColor" viewBox="0 0 24 24">
              <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M4 6h16M4 12h16M4 18h16" />
            </svg>
          </button>
        </div>
      </nav>

      {/* Mobile Menu */}
      {isOpen && (
        <div className="md:hidden bg-gray-800 px-4 py-2">
          <Link href={`/${currentLang}`} className="block py-2 hover:text-blue-400">
            {currentLang === 'en' ? 'Home' : 'صفحه اصلی'}
          </Link>
          <Link href={`/${currentLang}/analytics`} className="block py-2 hover:text-blue-400">
            {currentLang === 'en' ? 'Analytics' : 'تحلیل'}
          </Link>
          <Link href={`/${currentLang}/shop`} className="block py-2 hover:text-blue-400">
            {currentLang === 'en' ? 'Shop' : 'فروشگاه'}
          </Link>
          <Link href={`/${currentLang}/subscription`} className="block py-2 hover:text-blue-400">
            {currentLang === 'en' ? 'Subscription' : 'اشتراک'}
          </Link>
        </div>
      )}
    </header>
  );
}
