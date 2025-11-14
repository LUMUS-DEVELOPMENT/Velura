<script setup>
import {useProducts} from "@/composables/useProducts.js";
import ProductCard from "@/components/product/ProductCard.vue";

const {products} = useProducts()


</script>

<template>
    <ProductCard
        v-for="product in products"
        :product="product"
        :key="product.id">
    </ProductCard>
</template>

<style scoped>

</style>
