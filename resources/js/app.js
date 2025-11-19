import "./bootstrap.js"
import '@tailwindplus/elements'

import { createApp } from 'vue'
import App from './App.vue'
import router from "@/router/index.js"
import UiPlugin from '@/plugins/ui.js'
import { createPinia } from 'pinia'
import directives from "@/directives/directives.js";
import piniaPluginPersistedstate from 'pinia-plugin-persistedstate'
const app = createApp(App)
directives.map(directive => app.directive(directive.name, directive))
const pinia = createPinia()

pinia.use(piniaPluginPersistedstate)

app.use(pinia)
    .use(UiPlugin)
    .use(router)
    .mount('#app')

