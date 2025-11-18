<script setup>
import CartIcon from "@/components/Icons/CartIcon.vue";
import Button from "@/components/ui/base/Button.vue";
import {useCartStore} from "@/stores/useCartStore.js";
defineProps({
  id:{
    type: Number,
    required: true,
  }
})
const  cart = useCartStore()
</script>

<template>
    <Button :override="true" @click.prevent="cart.addItem(id)" class="px-3 py-1 mt-5 bg-green-600 text-white text-xs rounded hover:bg-green-700 transition cursor-pointer">
        <CartIcon />
    </Button>
</template>

<style scoped>

</style>
