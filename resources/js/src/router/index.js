import {createRouter, createWebHistory} from 'vue-router'
import Default from "@/layouts/Default.vue";

const routes = [
    {
        path: '/',
        component: Default,
        children: [
            {
                path: '',
                name: 'home',
                component: () => import('@/pages/Home.vue')
            },
        ]
    },
]

const router = createRouter({
    history: createWebHistory(),
    routes: routes
})

export default router
