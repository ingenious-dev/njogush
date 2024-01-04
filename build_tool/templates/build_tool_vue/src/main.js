import { createApp } from 'vue'
import './style.css'
import App from './App.vue'
import router from './router'
import store from './store'
import moment from 'moment';

// createApp(App).mount('#app')

const app = createApp(App)

app.use(router)

app.use(store)

app.config.globalProperties.$moment = moment

app.mount('#app')
