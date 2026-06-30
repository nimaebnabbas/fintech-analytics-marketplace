'use client';

export default function Footer() {
  const currentYear = new Date().getFullYear();

  return (
    <footer className="bg-gray-900 text-gray-300 mt-16">
      <div className="container mx-auto px-4 py-12">
        <div className="grid grid-cols-1 md:grid-cols-4 gap-8">
          {/* About */}
          <div>
            <h3 className="text-white font-bold mb-4">FinTech Analytics</h3>
            <p className="text-sm">
              Political psychology analysis and precious metals marketplace.
            </p>
          </div>

          {/* Links */}
          <div>
            <h3 className="text-white font-bold mb-4">Quick Links</h3>
            <ul className="text-sm space-y-2">
              <li><a href="#" className="hover:text-blue-400">Home</a></li>
              <li><a href="#" className="hover:text-blue-400">Analytics</a></li>
              <li><a href="#" className="hover:text-blue-400">Shop</a></li>
            </ul>
          </div>

          {/* Legal */}
          <div>
            <h3 className="text-white font-bold mb-4">Legal</h3>
            <ul className="text-sm space-y-2">
              <li><a href="#" className="hover:text-blue-400">Terms & Conditions</a></li>
              <li><a href="#" className="hover:text-blue-400">Privacy Policy</a></li>
              <li><a href="#" className="hover:text-blue-400">Disclaimer</a></li>
            </ul>
          </div>

          {/* Contact */}
          <div>
            <h3 className="text-white font-bold mb-4">Contact</h3>
            <p className="text-sm">Email: support@fintech-analytics.com</p>
            <p className="text-sm">Phone: +1 (555) 123-4567</p>
          </div>
        </div>

        <div className="border-t border-gray-700 mt-8 pt-8 text-center text-sm">
          <p>&copy; {currentYear} FinTech Analytics Marketplace. All rights reserved.</p>
        </div>
      </div>
    </footer>
  );
}
