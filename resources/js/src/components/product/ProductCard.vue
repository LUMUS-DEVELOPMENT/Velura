<script setup>
import Card from "@/components/ui/features/card/Card.vue";
import ProductCardContent from "@/components/product/ProductCardContent.vue";
import {useCartStore} from "@/stores/useCartStore.js";

defineProps({
    product: {type: Object, required: true}
})

const  cart = useCartStore()
</script>

<template>
        <Card>
            <ProductCardContent
                :path="product.imagePath"
                :title="product.title"
                :description="product.description"
                :price="product.price"
                :link="{ name: 'products.show', params: { id: product.id} }">
                <div>
                    <AddToCartButton @click="cart.addItem(product)"/>
                </div>
            </ProductCardContent>
        </Card>
</template>

<style scoped>

</style>
