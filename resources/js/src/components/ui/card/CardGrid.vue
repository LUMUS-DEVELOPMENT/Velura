<script setup>
defineProps({
    gap: {type: String, default: 'gap-5'}
})
</script>

<template>
    <div :class="['grid grid-cols-2 sm:grid-cols-3 lg:grid-cols-4', gap]">
        <slot />
    </div>
</template>

<style scoped>

</style>
