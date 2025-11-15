<script setup >
import { RouterLink } from "vue-router";
defineOptions({name: "LinkList"})
 defineProps({
    id: String,
    className: String,
    liClassName: String,
    linkClassName: String,
    ariaLabelledby: String,
    links: {
      type: Array,
      default: () => [],
    },
    role: {
      type: String,
      default: "list",
    },
    required: true
});
</script>

<template>
  <ul :role="role"  :class="className"  :id="id"  :aria-labelledby="ariaLabelledby" >
    <li  v-for="link in links"  :key="link.name"  :class="liClassName">
      <RouterLink :to="link.path"  :class="linkClassName">
        {{ link.name }}
      </RouterLink>
    </li>
  </ul>
</template>

