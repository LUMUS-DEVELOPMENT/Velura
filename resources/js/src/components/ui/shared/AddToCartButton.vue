<script setup>
import CartIcon from "@/components/Icons/CartIcon.vue";
import Button from "@/components/ui/base/Button.vue";

</script>

<template>
    <Button v-bind="$attrs" :override="true" class="px-3 py-1 mt-5 bg-green-600 text-white text-xs rounded hover:bg-green-700 transition cursor-pointer">
        <CartIcon />
    </Button>
</template>

<style scoped>

</style>
