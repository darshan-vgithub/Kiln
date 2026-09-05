/** @type {import('tailwindcss').Config} */
export default {
  content: ['./index.html', './src/**/*.{vue,js,ts,jsx,tsx}'],
  theme: {
    extend: {
      colors: {
        paper: '#F3F1EB',
        paperdim: '#EAE7DE',
        ink: '#15171B',
        inkfade: '#585A56',
        cobalt: '#2438E0',
        cobaltdeep: '#1C2BAE',
        emerald: '#0F6E5C',
        line: '#D8D4C8',
      },
      fontFamily: {
        serif: ['"Fraunces"', 'ui-serif', 'Georgia', 'serif'],
        sans: ['"Archivo"', 'ui-sans-serif', 'system-ui', 'sans-serif'],
      },
      maxWidth: {
        content: '1240px',
      },
    },
  },
  plugins: [],
}
