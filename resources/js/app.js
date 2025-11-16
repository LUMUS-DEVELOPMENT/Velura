import "./bootstrap.js"
import '@tailwindplus/elements'

import { createApp } from 'vue'
import App from './App.vue'
import router from "@/router/index.js";
import components from "@/components/ui/index.js"

const app = createApp(App);
components.map(component => app.component(component.name, component));

app.use(router).mount('#app')
