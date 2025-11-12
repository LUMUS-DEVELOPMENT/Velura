<script setup>
defineProps({
  collections:{
    type: Array,
    required: true,
    default:()=>[
      {
        id: 1,
        name:"Desk and Office",
        description:"Work from home accessories",
        image: 'https://tailwindcss.com/plus-assets/img/ecommerce-images/home-page-02-edition-01.jpg',
        path:"#"
      },
      {
        id: 1,
        name:"Self-Improvement",
        description:"Journals and note-taking",
        image: 'https://tailwindcss.com/plus-assets/img/ecommerce-images/home-page-02-edition-02.jpg',
        path:"#"
      },
      {
        id: 1,
        name:"Travel",
        description:"Daily commute essentials",
        image: 'https://tailwindcss.com/plus-assets/img/ecommerce-images/home-page-02-edition-03.jpg',
        path:"#"
      }
    ]
  }
})
</script>
<template>
  <div>
    <div class="bg-gray-100">
      <div class="mx-auto max-w-7xl px-4 sm:px-6 lg:px-8">
        <div class="mx-auto max-w-2xl py-16 sm:py-24 lg:max-w-none lg:py-32">
          <h2 class="text-2xl font-bold text-gray-900">Collections</h2>
          <div class="mt-6 space-y-12 lg:grid lg:grid-cols-3 lg:space-y-0 lg:gap-x-6">
            <div v-for="collection in collections"  class="group relative">
              <img :src="collection.image"  :alt="collection.name"
                   class="w-full rounded-lg bg-white object-cover group-hover:opacity-75 max-sm:h-80 sm:aspect-2/1 lg:aspect-square" />
              <h3 class="mt-6 text-sm text-gray-500">
                <a :href="collection.path">
                  <span class="absolute inset-0"></span>
                  {{collection.name}}
                </a>
              </h3>
              <p class="text-base font-semibold text-gray-900">{{collection.description}}</p>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>