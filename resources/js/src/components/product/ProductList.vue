<script setup>
import ProductCard from "@/components/product/ProductCard.vue";
import {useProductStore} from "@/stores/useProductStore.js";
import {onMounted} from "vue";


const store = useProductStore();

onMounted( () => {
     store.getAll()
})

</script>

<template>
    <ProductCard
        v-for="product in store.products"
        :product="product"
        :key="product.id">
    </ProductCard>
</template>

<style scoped>

</style>
