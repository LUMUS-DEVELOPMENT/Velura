<script setup>
import {useRoute} from "vue-router";
import {useProducts} from "@/composables/useProducts.js";
import ProductCardContent from "@/components/product/ProductCardContent.vue";
import AddToCartButton from "@/components/ui/AddToCartButton.vue";

const route = useRoute()
const { getProduct } = useProducts()

const product = getProduct(route.params.id)

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
                <div>
                    <AddToCartButton />
                </div>
            </ProductCardContent>

            <p v-else>Product not found.</p>
        </div>
    </div>
</template>

<style scoped>

</style>
