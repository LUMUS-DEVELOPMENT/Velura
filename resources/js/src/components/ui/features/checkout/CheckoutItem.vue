<template>
  <div class="flex items-center justify-between">
    <span>{{ item.title }}</span>
    <span class="font-semibold">{{ item.price }}$</span>
  </div>
</template>
<script setup>
defineProps({
  item: { type: Object, required: true }
});
</script>