<template>
  <div class="flex lg:ml-6 " >
    <el-disclosure   id="search-form" hidden class="w-[calc(100vh/2)]">
      <form class="flex items-center max-w-lg mx-auto space-x-2">
        <label for="voice-search" class="sr-only">Search</label>
        <div class="relative w-full ">
          <input type="text" id="input-search" class="block w-full ps-9 pe-3 py-2.5 bg-neutral-secondary-medium border border-default-medium text-heading text-sm rounded-base focus:ring-brand focus:border-brand shadow-xs placeholder:text-body" placeholder="Search" required />
        </div>
      </form>
    </el-disclosure>
    <SearchButton />
  </div>
</template>
<script setup>
import SearchButton from "@/components/ui/features/search/SearchButton.vue";
</script>
