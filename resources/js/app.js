import "./bootstrap.js"
import '@tailwindplus/elements'

import { createApp } from 'vue'
import App from './App.vue'
import router from "@/router/index.js"
import UiPlugin from '@/plugins/ui.js'

createApp(App)
    .use(UiPlugin)
    .use(router)
    .mount('#app')

