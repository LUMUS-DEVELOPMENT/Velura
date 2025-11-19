import {defineStore} from "pinia";

export const useCartStore = defineStore("useCartStore", {
    state: () => ({
        items: [],
    }),
    getters: {
        count: (state) => state.items.reduce((sum, item) => Number(sum) + Number(item.qty), 0),
        total: (state) => state.items.reduce((sum, item) =>
            Number(sum) + Number(item.price) * Number(item.qty), 0),
    },
    actions: {
        addItem(product) {
            if (!product) {
                console.error("Product not found", product.id);
                return;
            }

            const existingInCart = this.find(product.id);

            existingInCart ? existingInCart.qty += 1 : this.items.push({...product, qty: 1})

        },
        removeItem(id) {
            this.items = this.items.filter((item) => item.id !== id);
        },
        clear() {
            this.items = [];
        },
        increaseItemQty(id, quantity) {

            const item = this.find(id);
            if (item) item.qty++;
            if(item.qty > quantity) item.qty--;
        },
        decreaseItemQty(id) {
            const item = this.find(id);
            if (item && item.qty > 1) item.qty--;
        },
        find(id){
            return this.items.find(i => i.id === id)
        }
    },
    persist: {
        key: 'cart',
        paths: ['items'],
        storage: localStorage
    }
});
