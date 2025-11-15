<script setup >
defineOptions({ name: 'MegaMenu' })
defineProps({ menuData: Object, });
</script>

<template>
  <div class="relative bg-white">
    <div class="mx-auto max-w-7xl px-4 sm:px-6 lg:px-8">
      <div class="grid grid-cols-2 gap-x-8 gap-y-10 py-16">
        <div class="col-start-2 grid grid-cols-2 gap-x-8">
        </div>
        <div class="row-start-1 grid grid-cols-3 gap-x-8 gap-y-10 text-sm">
          <div v-for="(links, category) in menuData" :key="category">
            <p :id="`${category}-heading`" class="font-medium text-gray-900">{{ category }}</p>
            <LinkList
                :id="`${category}-heading`"
                className="mt-6 space-y-6 sm:mt-4 sm:space-y-4"
                liClassName="flex hover:text-gray-800"
                :links="links"
            />
          </div>
        </div>
      </div>
    </div>
  </div>
</template>
