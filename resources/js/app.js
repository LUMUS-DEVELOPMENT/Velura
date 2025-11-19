import "./bootstrap.js"
import '@tailwindplus/elements'

import { createApp } from 'vue'
import App from './App.vue'
import router from "@/router/index.js"
import UiPlugin from '@/plugins/ui.js'
import { createPinia } from 'pinia'
import directives from "@/directives/directives.js";

const app = createApp(App)
const pinia = createPinia()
directives.map(directive => app.directive(directive.name, directive))
app.use(pinia)
    .use(UiPlugin)
    .use(router)
    .mount('#app')

