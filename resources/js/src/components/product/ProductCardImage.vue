<script setup>
defineProps({
    path: {type: String, required: true},
})
</script>

<template>
    <img :src="path" alt="Front of men&#039;s Basic Tee in black."
         class="aspect-square w-full rounded-md bg-gray-200 object-cover group-hover:opacity-75 lg:aspect-auto lg:h-80"/>

</template>

<style scoped>

</style>
