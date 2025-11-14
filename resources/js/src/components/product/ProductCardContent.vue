<script setup>
import ProductCardImage from "@/components/product/ProductCardImage.vue";

defineProps({
    path: {type: String, required: true},
    title: {type: String, required: true},
    description: {type: String, required: true},
    price: {type: [String, Number], required: true},
    link: {type:[String, Object] , required: true}
})
</script>

<template>
    <div>
        <router-link :to="link">
                <ProductCardImage :path="path"/>
                <div class="flex justify-between mt-2">
                   <div>
                       <h3 class="text-sm text-gray-700">
                           <div>
                               {{ title }}
                           </div>
                       </h3>
                       <p class="mt-1 text-sm text-gray-500">{{ description }}</p>
                   </div>
                   <div class="p-2">
                       <p class="text-sm font-medium text-gray-900">${{ price }}</p>
                   </div>
                </div>
        </router-link>

        <slot />
    </div>

</template>

<style scoped>

</style>
