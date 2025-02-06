/** @type {import('tailwindcss').Config} */
module.exports = {
  content: [
    "./templates/**/*.html",
  ],
  theme: {
    extend: {
      colors: {
        'kerala': {
          'gold': '#FFD700',
          'red': '#8B0000',
          'green': '#006400',
          'cream': '#FFF5E1',
          'spice': '#8B4513',
        },
        'dark': {
          'bg': '#121212',
          'surface': '#1E1E1E',
          'border': '#2D2D2D',
          'hover': '#2A2A2A',
        }
      },
      fontFamily: {
        'malayalam': ['Manjari', 'sans-serif'],
        'display': ['Poppins', 'sans-serif'],
        'body': ['Inter', 'sans-serif'],
      },
      backgroundImage: {
        'kerala-pattern': "url('/static/images/kerala-pattern.svg')",
      }
    },
  },
  plugins: [],
}
