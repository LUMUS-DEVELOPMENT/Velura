<script setup>
import { useRoute } from "vue-router";
import { onMounted, computed } from "vue";
import { useProductStore } from "@/stores/useProductStore.js";
import ProductCardContent from "@/components/product/ProductCardContent.vue";
import { useCartStore } from "@/stores/useCartStore.js";

const route = useRoute()
const store = useProductStore()
const cart = useCartStore()

onMounted(() => {
    store.getById(route.params.id)
})

const product = computed(() => store.product)
</script>


<template>
    <div class="w-full">
        <div class="w-1/4  p-5 mt-10">
            <ProductCardContent
                v-if="product"
                :path="product.imagePath"
                :title="product.title"
                :description="product.description"
                :price="product.price"
                :link="{ name: 'products.show', params: { id: product.id } }"
            >
                <div class="flex justify-between">
                  <span class="p-2">Quantity: <b>{{product.quantity}}</b></span>
                    <AddToCartButton @click="cart.addItem(product)" />
                </div>
            </ProductCardContent>

            <p v-else>Product not found.</p>
        </div>
    </div>
</template>

<style scoped>

</style>
