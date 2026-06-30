'use client';

import { LineChart, Line, XAxis, YAxis, CartesianGrid, Tooltip, Legend, ResponsiveContainer } from 'recharts';

interface PriceChartProps {
  data: Array<{
    timestamp: string;
    price: number;
  }>;
  title: string;
  currency: string;
}

export default function PriceChart({ data, title, currency }: PriceChartProps) {
  return (
    <div className="bg-white p-6 rounded-lg shadow-lg">
      <h3 className="text-xl font-bold mb-4">{title}</h3>
      <ResponsiveContainer width="100%" height={300}>
        <LineChart data={data}>
          <CartesianGrid strokeDasharray="3 3" />
          <XAxis dataKey="timestamp" />
          <YAxis />
          <Tooltip />
          <Legend />
          <Line
            type="monotone"
            dataKey="price"
            stroke="#3b82f6"
            dot={false}
            name={`Price (${currency})`}
          />
        </LineChart>
      </ResponsiveContainer>
    </div>
  );
}
