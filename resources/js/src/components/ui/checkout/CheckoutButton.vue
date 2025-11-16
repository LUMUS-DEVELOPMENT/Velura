<template>
  <button  class="group flex items-center p-2">
      <span class="mr-2">
      <CartIcon />
      </span>
    <span class="text-sm font-medium" > {{count.count}}</span>
  </button>
</template>
<script setup>
import CartIcon from "@/components/ui/card/CartIcon.vue";
 defineProps({
  count: Number,
})

</script>