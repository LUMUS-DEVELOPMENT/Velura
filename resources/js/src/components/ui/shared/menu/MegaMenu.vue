<script setup >
defineOptions({ name: 'MegaMenu' })
defineProps({ menuData: Object, });
</script>

<template>
  <div class="relative bg-white">
    <div class="mx-auto max-w-7xl px-4 sm:px-6 lg:px-8">
      <div class="grid grid-cols-2 gap-x-8 gap-y-10 py-16">
        <div class="col-start-2 grid grid-cols-2 gap-x-8">
          <div class="grid grid-cols-2 gap-x-4">
            <div class="group relative text-sm">
              <img src="https://tailwindcss.com/plus-assets/img/ecommerce-images/mega-menu-category-01.jpg" alt="Models sitting back to back, wearing Basic Tee in black and bone." class="aspect-square w-full rounded-lg bg-gray-100 object-cover group-hover:opacity-75" />
              <a href="#" class="mt-6 block font-medium text-gray-900">

                <span aria-hidden="true" class="absolute inset-0 z-10"></span>
                New Arrivals
              </a>
              <p aria-hidden="true" class="mt-1">Shop now</p>
            </div>
            <div class="group relative text-sm">
              <img src="https://tailwindcss.com/plus-assets/img/ecommerce-images/mega-menu-category-02.jpg" alt="Close up of Basic Tee fall bundle with off-white, ochre, olive, and black tees." class="aspect-square w-full rounded-lg bg-gray-100 object-cover group-hover:opacity-75" />
              <a href="#" class="mt-6 block font-medium text-gray-900">
                <span aria-hidden="true" class="absolute inset-0 z-10"></span>
                Basic Tees
              </a>
              <p aria-hidden="true" class="mt-1">Shop now</p>
            </div>
          </div>
        </div>
        <div class="row-start-1 grid grid-cols-3 gap-x-8 gap-y-10 text-sm">
          <div v-for="(links, category) in menuData" :key="category">
            <p :id="`${category}-heading`" class="font-medium text-gray-900">{{ category }}</p>
            <LinkList
                :id="`${category}-heading`"
                className="mt-6 space-y-6 sm:mt-4 sm:space-y-4"
                liClassName="flex hover:text-gray-800"
                :links="links" />
          </div>
        </div>
      </div>
    </div>
  </div>
</template>
