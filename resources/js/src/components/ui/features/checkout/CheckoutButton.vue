<template>
  <Button class="group flex items-center p-2" :override="true">
      <span class="mr-2">
      <CartIcon />
      </span>
    <span class="text-sm font-medium" > {{count}}</span>
  </Button>
</template>
<script setup>
import CartIcon from "@/components/Icons/CartIcon.vue";
import Button from "@/components/ui/base/Button.vue";
defineProps({ count: Number });
</script>