import { fileURLToPath, URL } from 'node:url'

import { defineConfig } from 'vite'
import vue from '@vitejs/plugin-vue'
import vueDevTools from 'vite-plugin-vue-devtools'

// https://vite.dev/config/
export default defineConfig({
  server: {
    proxy: {
      "/backend-api": {
        target: 'https://manflix-bruno-f5aedufgd4hphse5.westus3-01.azurewebsites.net',
        secure: false,
        changeOrigin: true,
        rewrite: (path)=> path.replace(/^\/backend-api/,"")
      }
    }
  },
  plugins: [
    vue(),
    vueDevTools(),
  ],
  resolve: {
    alias: {
      '@': fileURLToPath(new URL('./src', import.meta.url))
    },
  },
})
