<script setup>
import ProductList from "@/components/product/ProductList.vue";
import Filter from "@/components/ui/features/filters/Filters.vue";

import useLinks from "@/composables/filter/useLinks.js";
import useCategory from "@/composables/filter/useCategory.js";
import useSize from "@/composables/filter/useSize.js";
import useColor from "@/composables/filter/useColor.js";

const links = useLinks();
const category = useCategory();
const size = useSize();
const color = useColor();
</script>

<template>
  <div class="bg-white">
    <!-- MOBILE FILTERS -->
    <el-dialog>
      <dialog id="mobile-filters" class="overflow-hidden backdrop:bg-transparent lg:hidden">
        <el-dialog-backdrop
            class="fixed inset-0 bg-black/25 transition-opacity duration-300 ease-linear data-closed:opacity-0">
        </el-dialog-backdrop>

        <div tabindex="0" class="fixed inset-0 flex focus:outline-none">
          <el-dialog-panel
              class="relative ml-auto flex size-full max-w-xs transform flex-col overflow-y-auto bg-white pt-4 pb-6 shadow-xl transition duration-300 ease-in-out data-closed:translate-x-full">
            <div class="flex items-center justify-between px-4">
              <h2 class="text-lg font-medium text-gray-900">Filters</h2>

              <button
                  type="button"
                  command="close"
                  commandfor="mobile-filters"
                  class="relative -mr-2 flex size-10 items-center justify-center rounded-md bg-white p-2 text-gray-400 hover:bg-gray-50">
                <span class="sr-only">Close menu</span>
                <svg viewBox="0 0 24 24" class="size-6" fill="none" stroke="currentColor" stroke-width="1.5">
                  <path d="M6 18 18 6M6 6l12 12" stroke-linecap="round" stroke-linejoin="round"/>
                </svg>
              </button>
            </div>
            <Filter
                :links="links"
                :filterCheckBoxParams="[
                  { command: 'mobile-color', buttonName:'Color', checkboxList: color },
                  { command:'mobile-category', buttonName:'Category', checkboxList: category },
                  { command:'mobile-size', buttonName:'Size', checkboxList: size }
                ]"
            />

          </el-dialog-panel>
        </div>
      </dialog>
    </el-dialog>

    <main class="mx-auto max-w-7xl px-4 sm:px-6 lg:px-8">
      <div class="flex items-baseline justify-between border-b border-gray-200 pt-24 pb-6">
        <h1 class="text-4xl font-bold tracking-tight text-gray-900">New Arrivals</h1>

        <div class="flex items-center">
          <el-dropdown class="relative inline-block text-left">
            <button class="group inline-flex justify-center text-sm font-medium text-gray-700 hover:text-gray-900">
              Sort
              <svg viewBox="0 0 20 20" class="size-5 ml-1 text-gray-400 group-hover:text-gray-500">
                <path d="M5.22 8.22a.75.75 0 0 1 1.06 0L10 11.94..."/>
              </svg>
            </button>

            <el-menu anchor="bottom end" popover class="w-40 bg-white shadow-2xl ring-1 ring-black/5">
              <div class="py-1">
                <a class="block px-4 py-2 text-sm">Most Popular</a>
                <a class="block px-4 py-2 text-sm">Best Rating</a>
                <a class="block px-4 py-2 text-sm">Newest</a>
                <a class="block px-4 py-2 text-sm">Price: Low → High</a>
                <a class="block px-4 py-2 text-sm">Price: High → Low</a>
              </div>
            </el-menu>
          </el-dropdown>

          <button class="-m-2 ml-4 p-2 text-gray-400 hover:text-gray-500 lg:hidden"
                  command="show-modal"
                  commandfor="mobile-filters">
            <svg viewBox="0 0 20 20" class="size-5">
              <path d="M2.628 1.601C5.028 1.206 7.49..."/>
            </svg>
          </button>
        </div>
      </div>
      <section aria-labelledby="products-heading" class="pt-6 pb-24">
        <h2 id="products-heading" class="sr-only">Products</h2>

        <div class="grid grid-cols-[20%_1fr] gap-8">

          <!-- DESKTOP FILTERS -->
          <Filter
              :links="links"
              :filterCheckBoxParams="[
                { command:'color', buttonName:'Color', checkboxList: color },
                { command:'category', buttonName:'Category', checkboxList: category },
                { command:'size', buttonName:'Size', checkboxList: size }
              ]"
          />
          <div class="grid grid-cols-3 gap-6">
            <ProductList/>
            <ProductList/>
          </div>
        </div>
      </section>
    </main>

  </div>
</template>
