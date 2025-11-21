import {defineStore} from 'pinia'
import {useProductApi} from '@/composables/api/useProductApi'

export const useProductStore = defineStore('products', {
    state: () => ({
        products: [],
        product: null,
        meta: null,
        links: null,
        loading: false,
        error: null,
    }),

    actions: {
        async getAll(page = 1) {
            const api = useProductApi()

            this.loading = true
            this.error = null

            try {
                const result = await api.getAll(page)

                this.products = result.data
                this.meta = result.meta
                this.links = result.links
            } catch (err) {
                this.error = err?.message || 'Failed to load products'
            } finally {
                this.loading = false
            }
        },


        async getById(id) {
            const api = useProductApi()

            this.loading = true
            this.error = null

            try {
                const result = await api.getById(id)
                this.product = result.data
            } catch (err) {
                this.error = err?.message || `Failed to load product ${id}`
            } finally {
                this.loading = false
            }
        },

    },
})
