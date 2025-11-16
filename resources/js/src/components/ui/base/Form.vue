<script setup>
const props = defineProps({
    title: String,
    override: Boolean
})
const emit = defineEmits(['submit'])

const handleSubmit = (e) => {
    e.preventDefault()
    emit('submit', e)
}
</script>

<template>
    <form
        v-bind="$attrs"
        :class="props.override
      ? ($attrs.class || '')
      : ['flex flex-col gap-4 bg-white p-8 rounded-2xl shadow-lg w-full max-w-sm', $attrs.class || '']"
        @submit="handleSubmit"
    >
        <h1 v-if="title" class="text-2xl font-semibold text-gray-800 text-center mb-6">{{ title }}</h1>
        <slot />
    </form>
</template>
