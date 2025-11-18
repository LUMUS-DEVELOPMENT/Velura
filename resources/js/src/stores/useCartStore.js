import { defineStore } from "pinia";
import { useProducts } from "@/composables/useProducts.js";
export const useCartStore = defineStore("useCartStore", {
    state: () => ({ items: [] }),
    getters: {
        count: (state) => state.items.length,
        total: (state) =>
            state.items.reduce((sum, item) => Number(sum) + Number(item.price), 0),
    },
    actions: {
        loadFromStorage() {
            const saved = localStorage.getItem("cart");
            if (saved)  this.items = JSON.parse(saved);
        },
        saveToStorage() {
            localStorage.setItem("cart", JSON.stringify(this.items));
        },
        addItem(id) {
            const { getProduct } = useProducts();
            const product = getProduct(id);
            if (!product) {
                console.error("Product not found", id);
                return;
            }
            this.items.push({
                id: product.id,
                image: product.imagePath,
                title: product.title,
                price: product.price,
            });
            this.saveToStorage();
        },
        removeItem(id) {
            this.items = this.items.filter((item) => item.id !== id);
            this.saveToStorage();
        },
        clear() {
            this.items = [];
            this.saveToStorage();
        },
    },
});
