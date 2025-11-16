<script setup>
import Card from "@/components/ui/features/card/Card.vue";
import ProductCardContent from "@/components/product/ProductCardContent.vue";

defineProps({
    product: {type: Object, required: true}
})
</script>

<template>
        <Card>
            <ProductCardContent
                :path="product.imagePath"
                :title="product.title"
                :description="product.description"
                :price="product.price"
                :link="{ name: 'products.show', params: { id: product.id} }"
            >

                <div>
                    <AddToCartButton/>
                </div>
            </ProductCardContent>
        </Card>
</template>

<style scoped>

</style>
