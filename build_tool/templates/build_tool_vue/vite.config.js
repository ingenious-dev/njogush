import { defineConfig } from 'vite'
import vue from '@vitejs/plugin-vue'

// https://vitejs.dev/config/
export default defineConfig({
  plugins: [vue()],
  build: {
    assetsDir: 'static/build_tool', // TODO https://vitejs.dev/config/build-options.html#build-assetsdir
  }
})
