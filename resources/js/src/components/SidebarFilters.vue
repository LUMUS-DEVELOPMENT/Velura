<script setup>

import ProductList from "@/components/product/ProductList.vue";
import Filter from "@/components/Filters.vue";

</script>

<template>
    <div class="bg-white">
      <!-- Mobile filter dialog -->

      <el-dialog>
        <dialog id="mobile-filters" class="overflow-hidden backdrop:bg-transparent lg:hidden">
          <el-dialog-backdrop
              class="fixed inset-0 bg-black/25 transition-opacity duration-300 ease-linear data-closed:opacity-0"></el-dialog-backdrop>
          <div tabindex="0" class="fixed inset-0 flex focus:outline-none">
            <el-dialog-panel class="relative ml-auto flex size-full max-w-xs transform flex-col overflow-y-auto bg-white pt-4 pb-6 shadow-xl transition duration-300 ease-in-out data-closed:translate-x-full">
              <div class="flex items-center justify-between px-4">
                <h2 class="text-lg font-medium text-gray-900">Filters</h2>
                <button type="button" command="close" commandfor="mobile-filters"
                        class="relative -mr-2 flex size-10 items-center justify-center rounded-md bg-white p-2 text-gray-400 hover:bg-gray-50 focus:ring-2 focus:ring-indigo-500 focus:outline-hidden">
                  <span class="absolute -inset-0.5"></span>
                  <span class="sr-only">Close menu</span>
                  <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5" data-slot="icon"
                       aria-hidden="true" class="size-6">
                    <path d="M6 18 18 6M6 6l12 12" stroke-linecap="round" stroke-linejoin="round"/>
                  </svg>
                </button>
              </div>
              <!-- Filters -->
              <Filter :links="[
                      { name: 'Tops', path: '#' },
                      { name: 'Backpacks', path: '#' },
                      { name: 'Travel Bags', path: '#' },
                      { name: 'Hip Bags', path: '#' },
                      { name: 'Laptop Sleeves', path: '#' },
                  ]" :filter-check-box-params="[
                  {
                    command:'mobile-color',
                    buttonName:'Color',
                    checkboxList:[
                      { name: 'color[]', value: 'white' },
                      { name: 'color[]', value: 'beige' },
                      { name: 'color[]', value: 'blue' },
                      { name: 'color[]', value: 'brown' },
                      { name: 'color[]', value: 'green' },
                      { name: 'color[]', value: 'purple' }
                    ]
                  },
                  {
                    command:'mobile-category',
                    buttonName:'Category',
                    checkboxList:[
                      { name: 'category[]', value: 'new-arrivals' },
                      { name: 'category[]', value: 'sale' },
                      { name: 'category[]', value: 'travel' },
                      { name: 'category[]', value: 'organization' },
                      { name: 'category[]', value: 'accessories' }
                    ]
                  },
                  {
                    command:'mobile-size',
                    buttonName:'Size',
                    checkboxList:[
                      { name: 'size[]', value: '2L' },
                      { name: 'size[]', value: '6l' },
                      { name: 'size[]', value: '12l' },
                      { name: 'size[]', value: '18l' },
                      { name: 'size[]', value: '20l' },
                      { name: 'size[]', value: '40l' }
                    ]
                  }
              ]" />
            </el-dialog-panel>
          </div>
        </dialog>
      </el-dialog>

      <!-- Desktop filter dialog -->
      <main class="mx-auto max-w-7xl px-4 sm:px-6 lg:px-8">
        <div class="flex items-baseline justify-between border-b border-gray-200 pt-24 pb-6">
          <h1 class="text-4xl font-bold tracking-tight text-gray-900">New Arrivals</h1>
          <div class="flex items-center">
            <el-dropdown class="relative inline-block text-left">
              <button class="group inline-flex justify-center text-sm font-medium text-gray-700 hover:text-gray-900">
                Sort
                <svg viewBox="0 0 20 20" fill="currentColor" data-slot="icon" aria-hidden="true"
                     class="-mr-1 ml-1 size-5 shrink-0 text-gray-400 group-hover:text-gray-500">
                  <path
                      d="M5.22 8.22a.75.75 0 0 1 1.06 0L10 11.94l3.72-3.72a.75.75 0 1 1 1.06 1.06l-4.25 4.25a.75.75 0 0 1-1.06 0L5.22 9.28a.75.75 0 0 1 0-1.06Z"
                      clip-rule="evenodd" fill-rule="evenodd"/>
                </svg>
              </button>
              <el-menu anchor="bottom end" popover class="w-40 origin-top-right rounded-md bg-white shadow-2xl ring-1 ring-black/5 transition transition-discrete [--anchor-gap:--spacing(2)] focus:outline-hidden data-closed:scale-95 data-closed:transform data-closed:opacity-0 data-enter:duration-100 data-enter:ease-out data-leave:duration-75 data-leave:ease-in">
                <div class="py-1">
                  <!-- Selected: "font-medium text-gray-900", Not Selected: "text-gray-500" -->
                  <a href="#" class="block px-4 py-2 text-sm font-medium text-gray-900 focus:bg-gray-100 focus:outline-hidden">Most Popular</a>
                  <a href="#" class="block px-4 py-2 text-sm text-gray-500 focus:bg-gray-100 focus:outline-hidden">Best Rating</a>
                  <a href="#" class="block px-4 py-2 text-sm text-gray-500 focus:bg-gray-100 focus:outline-hidden">Newest</a>
                  <a href="#" class="block px-4 py-2 text-sm text-gray-500 focus:bg-gray-100 focus:outline-hidden">Price: Low to High</a>
                  <a href="#" class="block px-4 py-2 text-sm text-gray-500 focus:bg-gray-100 focus:outline-hidden">Price: High to Low</a>
                </div>
              </el-menu>
            </el-dropdown>
            <button type="button" class="-m-2 ml-5 p-2 text-gray-400 hover:text-gray-500 sm:ml-7">
              <span class="sr-only">View grid</span>
              <svg viewBox="0 0 20 20" fill="currentColor" data-slot="icon" aria-hidden="true" class="size-5">
                <path
                    d="M4.25 2A2.25 2.25 0 0 0 2 4.25v2.5A2.25 2.25 0 0 0 4.25 9h2.5A2.25 2.25 0 0 0 9 6.75v-2.5A2.25 2.25 0 0 0 6.75 2h-2.5Zm0 9A2.25 2.25 0 0 0 2 13.25v2.5A2.25 2.25 0 0 0 4.25 18h2.5A2.25 2.25 0 0 0 9 15.75v-2.5A2.25 2.25 0 0 0 6.75 11h-2.5Zm9-9A2.25 2.25 0 0 0 11 4.25v2.5A2.25 2.25 0 0 0 13.25 9h2.5A2.25 2.25 0 0 0 18 6.75v-2.5A2.25 2.25 0 0 0 15.75 2h-2.5Zm0 9A2.25 2.25 0 0 0 11 13.25v2.5A2.25 2.25 0 0 0 13.25 18h2.5A2.25 2.25 0 0 0 18 15.75v-2.5A2.25 2.25 0 0 0 15.75 11h-2.5Z"
                    clip-rule="evenodd" fill-rule="evenodd"/>
              </svg>
            </button>
            <button type="button" command="show-modal" commandfor="mobile-filters"
                    class="-m-2 ml-4 p-2 text-gray-400 hover:text-gray-500 sm:ml-6 lg:hidden">
              <span class="sr-only">Filters</span>
              <svg viewBox="0 0 20 20" fill="currentColor" data-slot="icon" aria-hidden="true" class="size-5">
                <path
                    d="M2.628 1.601C5.028 1.206 7.49 1 10 1s4.973.206 7.372.601a.75.75 0 0 1 .628.74v2.288a2.25 2.25 0 0 1-.659 1.59l-4.682 4.683a2.25 2.25 0 0 0-.659 1.59v3.037c0 .684-.31 1.33-.844 1.757l-1.937 1.55A.75.75 0 0 1 8 18.25v-5.757a2.25 2.25 0 0 0-.659-1.591L2.659 6.22A2.25 2.25 0 0 1 2 4.629V2.34a.75.75 0 0 1 .628-.74Z"
                    clip-rule="evenodd" fill-rule="evenodd"/>
              </svg>
            </button>
          </div>
        </div>
        <section aria-labelledby="products-heading" class="pt-6 pb-24">
          <h2 id="products-heading" class="sr-only">Products</h2>
          <div class="grid grid-cols-1 gap-x-8 gap-y-10">
            <!-- Filters -->
            <div class="grid grid-cols-[20%_1fr] gap-4 ">
              <Filter :links="[
                      { name: 'Tops', path: '#' },
                      { name: 'Backpacks', path: '#' },
                      { name: 'Travel Bags', path: '#' },
                      { name: 'Hip Bags', path: '#' },
                      { name: 'Laptop Sleeves', path: '#' },
                  ]" :filter-check-box-params="[
                  {
                    command:'color',
                    buttonName:'Color',
                    checkboxList:[
                      { name: 'color[]', value: 'white' },
                      { name: 'color[]', value: 'beige' },
                      { name: 'color[]', value: 'blue' },
                      { name: 'color[]', value: 'brown' },
                      { name: 'color[]', value: 'green' },
                      { name: 'color[]', value: 'purple' }
                    ]
                  },
                  {
                    command:'category',
                    buttonName:'Category',
                    checkboxList:[
                      { name: 'category[]', value: 'new-arrivals' },
                      { name: 'category[]', value: 'sale' },
                      { name: 'category[]', value: 'travel' },
                      { name: 'category[]', value: 'organization' },
                      { name: 'category[]', value: 'accessories' }
                    ]
                  },
                  {
                    command:'size',
                    buttonName:'Size',
                    checkboxList:[
                      { name: 'size[]', value: '2L' },
                      { name: 'size[]', value: '6l' },
                      { name: 'size[]', value: '12l' },
                      { name: 'size[]', value: '18l' },
                      { name: 'size[]', value: '20l' },
                      { name: 'size[]', value: '40l' }
                    ]
                  }
              ]" />
              <!-- Product grid -->
              <div class="grid grid-cols-3 w-[1fr] gap-4">
                <ProductList ></ProductList>
                <ProductList ></ProductList>
              </div>
            </div>
          </div>
        </section>
      </main>
    </div>
</template>
