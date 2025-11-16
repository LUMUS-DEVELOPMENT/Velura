<script setup>
import SearchIcon from "@/components/ui/features/search/searchIcon.vue";
</script>
<template>
  <button type="button" class="p-2 text-gray-400 hover:text-gray-500" command="--toggle" commandfor="search-form">
    <span class="sr-only">Search</span>
    <SearchIcon />
  </button>
</template>
