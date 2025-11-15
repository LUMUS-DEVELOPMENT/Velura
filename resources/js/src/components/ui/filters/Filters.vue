<script setup>
import FilterSection from "@/components/ui/filters/FilterSection.vue";

defineProps({
  links: Array,
  filterCheckBoxParams: Array
});
</script>

<template>
  <aside class="space-y-8">

    <!-- LINKS -->
    <nav v-if="links?.length">
      <ul class="space-y-2">
        <li v-for="link in links" :key="link.name">
          <RouterLink :to="link.path" class="text-gray-700 hover:text-black">
            {{ link.name }}
          </RouterLink>
        </li>
      </ul>
    </nav>

    <!-- FILTER SECTIONS -->
    <div class="space-y-6">
      <FilterSection
          v-for="filter in filterCheckBoxParams"
          :key="filter.command"
          :command="filter.command"
          :buttonName="filter.buttonName"
          :checkboxList="filter.checkboxList"
      />
    </div>

  </aside>
</template>
