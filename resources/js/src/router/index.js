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
            {
                path: 'products',
                name: 'products.index',
                component: () => import('@/pages/products/Index.vue')
            },
            {
                path: 'products/:id',
                name: 'products.show',
                component: () => import('@/pages/products/Show.vue')
            },
            {
                path: 'login',
                name: 'login',
                component: () => import('@/pages/auth/Login.vue')
            },
            {
                path: 'register',
                name: 'register',
                component: () => import('@/pages/auth/Register.vue')
            },
        ]
    },
]

const router = createRouter({
    history: createWebHistory(),
    routes: routes
})

export default router
