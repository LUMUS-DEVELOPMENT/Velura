<template>
    <div class="flex flex-col sm:flex-row sm:items-center gap-2 sm:gap-4">
        <img :src="item.imagePath" alt="image" class="w-16 h-16 sm:w-10 sm:h-10 object-cover rounded">

        <div class="flex-1 flex flex-col sm:flex-row sm:items-center sm:justify-between gap-2 sm:gap-4">
            <div class="flex flex-col sm:flex-row sm:items-center gap-1 sm:gap-2">
                <span class="font-medium">{{ item.title }}</span>
                <span class="font-semibold">
                    {{ new Intl.NumberFormat('en-US', { style: 'currency', currency: 'USD' })
                    .format(item.price * item.qty) }}
                </span>
            </div>

            <div class="flex items-center gap-1 sm:gap-2">
                <slot />
            </div>
        </div>
    </div>
</template>

<script setup>
defineProps({
    item: { type: Object, required: true }
});
</script>
