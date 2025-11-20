<script setup>
import {computed} from "vue";

const props = defineProps({
    modelValue: Boolean,
    label: String,
    error: String,
    touched: Boolean,
    submitted: Boolean,
    override: Boolean
})

const emit = defineEmits(["update:modelValue", "blur"])

const showError = computed(() =>
    props.error && (props.touched || props.submitted)
)
</script>

<template>
    <div class="flex flex-col gap-1">
        <label class="flex items-center gap-2 cursor-pointer select-none">
            <input
                type="checkbox"
                :checked="modelValue"
                @change="emit('update:modelValue', $event.target.checked)"
                @blur="emit('blur')"
                v-bind="$attrs"
                :class="props.override ? $attrs.class : [
                    'h-4 w-4 rounded border transition cursor-pointer',
                    showError
                        ? 'border-red-500 ring-1 ring-red-500'
                        : modelValue
                                ? 'border-green-500 ring-1 ring-green-500'
                                : 'border-gray-300'
                ]"
            >
            <span v-if="label" class="text-sm font-medium text-gray-800">
                {{ label }}
            </span>

            <span
                v-if="showError"
                class="text-red-600 text-sm"
            >
                {{ error }}
             </span>
        </label>
    </div>
</template>

<style scoped>

</style>
