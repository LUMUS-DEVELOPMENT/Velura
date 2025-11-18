<script setup>
const emit = defineEmits(['click', 'focus', 'blur', 'keydown', 'keyup']);

const props = defineProps({
    disabled: Boolean,
    loading: Boolean,
    override: Boolean,
    type: { type: String, default: 'button' }
})
</script>

<template>
    <button
        v-bind="$attrs"
        :type="type"
        :disabled="disabled || loading"
        :class="props.override
      ? [$attrs.class]
      : [
          'px-4 py-2 rounded-lg text-sm font-medium transition flex items-center justify-center gap-2',
          disabled || loading
            ? 'bg-gray-400 text-white cursor-not-allowed'
            : ($attrs.class ? $attrs.class : 'bg-indigo-600 hover:bg-indigo-700 text-white cursor-pointer')
        ]"
        @click="emit('click', $event)"
        @blur="emit('blur')"
    >
        <template v-if="loading">
            <svg class="w-5 h-5 animate-spin text-white" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24">
                <circle class="opacity-25" cx="12" cy="12" r="10" stroke="currentColor" stroke-width="4"></circle>
                <path class="opacity-75" fill="currentColor" d="M4 12a8 8 0 018-8v4l3-3-3-3v4a8 8 0 00-8 8h4l-3 3 3 3H4z"></path>
            </svg>
            <span>Loading...</span>
        </template>
        <template v-else>
            <slot />
        </template>
    </button>
</template>
