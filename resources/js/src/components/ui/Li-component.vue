<script setup>

import {RouterLink} from "vue-router";

defineProps({
  links: {
    type: Array,
    required: true
  },
  liClassName: null,
  className: null
})
</script>

<template>
  <li v-for="link in links" :key="link.name" :class="liClassName">
    <RouterLink :to="link.path" :class="liClassName">
      {{ link.name }}
    </RouterLink>
  </li>
</template>
