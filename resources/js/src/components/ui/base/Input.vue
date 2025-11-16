<script setup>
const props = defineProps({
    modelValue: [String, Number],
    label: String,
    error: String,
    type: { type: String, default: 'text' },
    override: Boolean
})

const emit = defineEmits(['update:modelValue'])
</script>

<template>
    <div class="flex flex-col gap-1">
        <label v-if="label" class="text-sm font-medium">{{ label }}</label>

        <input
            v-bind="$attrs"
            :type="type"
            :value="modelValue"
            @input="$emit('update:modelValue', $event.target.value)"
            :class="props.override
        ? $attrs.class
        : [
            'px-3 py-2 mt-2 border rounded-lg text-sm transition focus:outline-none focus:ring-2 focus:ring-blue-500',
            $attrs.class,
            error
              ? 'border-red-500 focus:ring-red-500'
              : modelValue
              ? 'border-green-500 focus:ring-green-500'
              : 'border-gray-300'
          ]"
        />

        <span v-if="error" class="text-red-600 text-sm">{{ error }}</span>
    </div>
</template>
