import {defineStore} from "pinia";
import {useProductStore} from "@/stores/useProductStore.js";

export const useCartStore = defineStore("useCartStore", {
    state: () => ({
        items: [],
        isOpen: false
    }),
    getters: {
        count: (state) => state.items.reduce((sum, item) => Number(sum) + Number(item.qty), 0),
        total: (state) => state.items.reduce((sum, item) =>
            Number(sum) + Number(item.price) * Number(item.qty), 0),
    },
    actions: {
        toggleCart() {
            this.isOpen = !this.isOpen;
        },

        addItem(product) {
            if (!product || !product.id) {
                console.warn("Invalid product passed to addItem:", product);
                return;
            }

            const maxQty = Number(product.quantity)

            const item = this.items.find(i => i.id === product.id);

            if (item) {
                if (item.qty < maxQty) {
                    item.qty++;
                } else {
                    console.warn(`Cannot add more than ${maxQty} items for product ${product.id}`);
                }
                return;
            }

            this.items.push({
                ...product,
                qty: 1,
            });

        },
        removeItem(item) {
            this.items = this.items.filter(i => i !== item);
        },
        clear() {
            this.items = [];
        },
        setQty(item, value, blur = false) {
            if (!item) return;

            const digits = value.toString().replace(/\D/g, "");


            if (digits === "") {
                item.qty = blur ? 1 : "";
                return;
            }

            let qty = Number(digits);

            if (qty < 1) qty = 1;
            if (qty > Number(item.quantity)) qty = Number(item.quantity);


            item.qty = qty;
        },
        increaseItemQty(item) {
            if (!item) return;
            if (item && item.qty < item.quantity) item.qty++;
        },
        decreaseItemQty(item) {
            if (!item) return;
            if (item && item.qty > 1) item.qty--;
        },
    },
    persist: {
        key: 'cart',
        paths: ['items'],
        storage: localStorage,
        afterHydrate: (ctx) => {
            const store = ctx.store;

            store.items = store.items.map(item => {
                if (item.qty === "" || item.qty === null || item.qty === undefined) {
                    item.qty = 1;
                }
                return item;
            });
        },
    },
});
