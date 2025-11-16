<template>
  <li>
    <button
        @click.prevent="$emit('select', language)"
        class="inline-flex items-center w-full p-2 rounded hover:bg-neutral-tertiary-medium hover:text-heading"
    >
      <span class="h-4 w-4 me-1.5" v-html="language.icon"></span>
      {{ language.label }}
    </button>
  </li>
</template>

<script setup>
defineProps({
  language: Object,
  isActive: Boolean
});
</script>
