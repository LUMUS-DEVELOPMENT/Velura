<template>
  <div class="flex items-center justify-between">
    <img :src="item.image" alt="image" class="w-10 h-10">
    <span>{{ item.title }}</span>
    <span class="font-semibold">{{ item.price }}$</span>
    <Button type="button" @click="cart.removeItem(item.id)" :override="true">
      <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke-width="1.5" stroke="currentColor" class="size-6">
        <path stroke-linecap="round" stroke-linejoin="round" d="M12 9.75 14.25 12m0 0 2.25 2.25M14.25 12l2.25-2.25M14.25 12 12 14.25m-2.58 4.92-6.374-6.375a1.125 1.125 0 0 1 0-1.59L9.42 4.83c.21-.211.497-.33.795-.33H19.5a2.25 2.25 0 0 1 2.25 2.25v10.5a2.25 2.25 0 0 1-2.25 2.25h-9.284c-.298 0-.585-.119-.795-.33Z" />
      </svg>
    </Button>
  </div>
</template>
<script setup>
import {useCartStore} from "@/stores/useCartStore.js";
import Button from "@/components/ui/base/Button.vue";

defineProps({
  item: { type: Object, required: true }
});
const cart = useCartStore()
</script>