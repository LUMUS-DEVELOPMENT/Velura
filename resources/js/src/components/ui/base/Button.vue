<script setup>
const props = defineProps({
    override: Boolean
})
</script>

<template>
    <button
        v-bind="$attrs"
        :class="props.override
      ? $attrs.class
      : ['w-full bg-indigo-600 text-white font-medium py-2.5 rounded-lg hover:bg-indigo-700 transition cursor-pointer', $attrs.class]
    "
    >
        <slot />
    </button>
</template>
