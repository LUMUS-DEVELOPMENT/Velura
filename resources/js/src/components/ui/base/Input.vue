<script setup>
import { computed } from 'vue'

const props = defineProps({
    modelValue: [String, Number],
    label: String,
    error: String,
    touched: Boolean,
    submitted: Boolean,
    override: Boolean
})

const emit = defineEmits(['update:modelValue', 'blur'])

const showError = computed(() =>
    props.error && (props.touched || props.submitted)
)
</script>

<template>
    <div class="flex flex-col gap-1">
        <label v-if="label" class="text-sm font-medium">{{ label }}</label>

        <input
            v-bind="$attrs"
            :value="modelValue"
            @input="emit('update:modelValue', $event.target.value)"
            @blur="emit('blur')"
            :class="props.override
    ? $attrs.class
    : [
        'px-3 py-2 mt-1 border rounded-lg text-sm transition focus:outline-none focus:ring-2',
        $attrs.class,
        showError
            ? 'border-red-500 focus:ring-red-500'
        : (props.touched && modelValue)
            ? 'border-green-500 focus:ring-green-500'
        : 'border-gray-300'
    ]"
        />

        <span
            v-if="showError"
            class="text-red-600 text-sm"
        >
            {{ error }}
        </span>
    </div>
</template>
