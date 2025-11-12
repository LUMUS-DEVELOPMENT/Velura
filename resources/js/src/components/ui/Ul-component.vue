<script setup>
defineProps({
  role:"list",
  id:null,
  ariaLabelledby:null,
  className:null,
})
</script>

<template>
  <ul
      :role="role"
      :class="className"
      :id="id"
      :aria-labelledby="ariaLabelledby"
  >
    <slot />
  </ul>
</template>
