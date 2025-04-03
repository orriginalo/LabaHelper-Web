import textShadow from '@designbycode/tailwindcss-text-shadow'
import typography from '@tailwindcss/typography'

/** @type {import('tailwindcss').Config} */
export default {
  content: ['./index.html', './src/**/*.{vue,js,ts,jsx,tsx}'],
  theme: {
    extend: {
      fontFamily: {
        ubuntu: ['Comfortaa', 'monospace'],
      },
      colors: {
        'green-300': '#7CBC3C',
        'green-200': '#AAE272',
        'green-400': '#98EF3E',
        'zinc-800': '#414141',
        grad: '#181818',
      },
      scale: {
        102: '1.02',
      },
    },
  },
  plugins: [
    textShadow({
      shadowColor: 'rgba(0, 0, 0, 0.5)',
      shadowBlur: '1px',
      shadowOffsetX: '1px',
      shadowOffsetY: '1px',
    }),
    typography,
  ],
}
