<script setup>


</script>

<template>
  <el-dialog>
    <dialog id="mobile-menu" class="backdrop:bg-transparent lg:hidden">
      <el-dialog-backdrop class="fixed inset-0 bg-black/25 transition-opacity duration-300 ease-linear data-closed:opacity-0"></el-dialog-backdrop>
      <div tabindex="0" class="fixed inset-0 flex focus:outline-none">
        <el-dialog-panel class="relative flex w-full max-w-xs transform flex-col overflow-y-auto bg-white pb-12 shadow-xl transition duration-300 ease-in-out data-closed:-translate-x-full">
          <div class="flex px-4 pt-5 pb-2">
            <button type="button" command="close" commandfor="mobile-menu" class="relative -m-2 inline-flex items-center justify-center rounded-md p-2 text-gray-400">
              <span class="absolute -inset-0.5"></span>
              <span class="sr-only">Close menu</span>
              <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5" data-slot="icon" aria-hidden="true" class="size-6">
                <path d="M6 18 18 6M6 6l12 12" stroke-linecap="round" stroke-linejoin="round" />
              </svg>
            </button>
          </div>
          <!-- Links -->
          <el-tab-group class="mt-2 block">
            <div class="border-b border-gray-200">
              <el-tab-list class="-mb-px flex space-x-8 px-4">
                <button class="flex-1 border-b-2 border-transparent px-1 py-4 text-base font-medium whitespace-nowrap text-gray-900 aria-selected:border-indigo-600 aria-selected:text-indigo-600">Women</button>
                <button class="flex-1 border-b-2 border-transparent px-1 py-4 text-base font-medium whitespace-nowrap text-gray-900 aria-selected:border-indigo-600 aria-selected:text-indigo-600">Men</button>
              </el-tab-list>
            </div>
            <el-tab-panels>
              <div class="space-y-10 px-4 pt-10 pb-8">
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
                <div>
                  <p id="women-clothing-heading-mobile" class="font-medium text-gray-900">Clothing</p>
<!--                  <UlComponent id="women-clothing-heading-mobile" ariaLabelledby="women-clothing-heading-mobile" className="mt-6 flex flex-col space-y-6">-->
<!--                    <LiComponent className="-m-2 block p-2 text-gray-500" liClassName="flow-root" :links="[-->
<!--                        { name:'Tops', path:'#' },-->
<!--                        { name:'Dresses', path:'#' },-->
<!--                        { name:'Pants', path:'#' },-->
<!--                        { name:'Denim', path:'#' },-->
<!--                        { name:'Sweaters', path:'#' },-->
<!--                        { name:'T-Shirts', path:'#' },-->
<!--                        { name:'Jackets', path:'#' },-->
<!--                        { name:'Browse All', path:'#' }-->
<!--                    ]" />-->
<!--                  </UlComponent>-->
                </div>
                <div>
                  <p id="women-accessories-heading-mobile" class="font-medium text-gray-900">Accessories</p>
<!--                  <UlComponent id="women-accessories-heading-mobile" ariaLabelledby="women-accessories-heading-mobile" className="mt-6 flex flex-col space-y-6">-->
<!--                    <LiComponent className="-m-2 block p-2 text-gray-500" liClassName="flow-root" :links="[-->
<!--                        { name:'Watches', path:'#' },-->
<!--                        { name:'Wallets', path:'#' },-->
<!--                        { name:'Bags', path:'#'},-->
<!--                        { name:'Sunglasses', path:'#' },-->
<!--                        { name:'Hats', path:'#'},-->
<!--                        { name:'Belts', path:'#'}-->
<!--                    ]" />-->
<!--                  </UlComponent>-->
                </div>
                <div>
                  <p id="women-brands-heading-mobile" class="font-medium text-gray-900">Brands</p>
<!--                  <UlComponent id="women-brands-heading-mobile" ariaLabelledby="women-brands-heading-mobile" className="mt-6 flex flex-col space-y-6">-->
<!--                    <LiComponent className="-m-2 block p-2 text-gray-500" liClassName="flow-root" :links="[-->
<!--                        { name:'Full Nelson', path:'#' },-->
<!--                        { name:'My Way', path:'#' },-->
<!--                        { name:'Re-Arranged', path:'#'},-->
<!--                        { name:'Counterfeit', path:'#' },-->
<!--                        { name:'Significant Other', path:'#'}-->
<!--                    ]" />-->
<!--                  </UlComponent>-->
                </div>
              </div>
              <div hidden class="space-y-10 px-4 pt-10 pb-8">
                <div class="grid grid-cols-2 gap-x-4">
                  <div class="group relative text-sm">
                    <img src="https://tailwindcss.com/plus-assets/img/ecommerce-images/product-page-04-detail-product-shot-01.jpg" alt="Drawstring top with elastic loop closure and textured interior padding." class="aspect-square w-full rounded-lg bg-gray-100 object-cover group-hover:opacity-75" />
                    <a href="#" class="mt-6 block font-medium text-gray-900">
                      <span aria-hidden="true" class="absolute inset-0 z-10"></span>
                      New Arrivals
                    </a>
                    <p aria-hidden="true" class="mt-1">Shop now</p>
                  </div>
                  <div class="group relative text-sm">
                    <img src="https://tailwindcss.com/plus-assets/img/ecommerce-images/category-page-02-image-card-06.jpg" alt="Three shirts in gray, white, and blue arranged on table with same line drawing of hands and shapes overlapping on front of shirt." class="aspect-square w-full rounded-lg bg-gray-100 object-cover group-hover:opacity-75" />
                    <a href="#" class="mt-6 block font-medium text-gray-900">
                      <span aria-hidden="true" class="absolute inset-0 z-10"></span>
                      Artwork Tees
                    </a>
                    <p aria-hidden="true" class="mt-1">Shop now</p>
                  </div>
                </div>
                <div>
                  <p id="men-clothing-heading-mobile" class="mt-6 flex flex-col space-y-6">Clothing</p>
<!--                  <UlComponent id="heading" ariaLabelledby="men-clothing-heading-mobile" className="mt-6 flex flex-col space-y-6">-->
<!--                    <LiComponent className="-m-2 block p-2 text-gray-500" liClassName="flow-root" :links="[-->
<!--                        { name:'Tops', path:'#' },-->
<!--                        { name:'Pants', path:'#' },-->
<!--                        { name:'Sweaters', path:'#'},-->
<!--                        { name:'T-Shirts', path:'#' },-->
<!--                        { name:'Jackets', path:'#'},-->
<!--                        { name:'Activewear', path:'#' },-->
<!--                        { name:'Browse All', path:'#' },-->
<!--                    ]" />-->
<!--                  </UlComponent>-->
                </div>
                <div>
                  <p id="men-accessories-heading-mobile" class="font-medium text-gray-900">Accessories</p>
<!--                  <UlComponent id="heading" ariaLabelledby="Accessories-heading" className="mt-6 flex flex-col space-y-6">-->
<!--                    <LiComponent className="-m-2 block p-2 text-gray-500" liClassName="flow-root" :links="[-->
<!--                        { name:'Watches', path:'#' },-->
<!--                        { name:'Wallets', path:'#' },-->
<!--                        { name:'Bags', path:'#'},-->
<!--                        { name:'Sunglasses', path:'#' },-->
<!--                        { name:'Hats', path:'#'},-->
<!--                        { name:'Belts', path:'#' }-->
<!--                    ]" />-->
<!--                  </UlComponent>-->
                </div>
                <div>
                  <p id="men-brands-heading-mobile" class="font-medium text-gray-900">Brands</p>
<!--                  <UlComponent id="heading" ariaLabelledby="men-brands-heading-mobile" className="mt-6 flex flex-col space-y-6">-->
<!--                    <LiComponent className="-m-2 block p-2 text-gray-500" liClassName="flow-root" :links="[-->
<!--                        { name:'Re-Arranged', path:'#' },-->
<!--                        { name:'Counterfeit', path:'#' },-->
<!--                        { name:'Full Nelson', path:'#'},-->
<!--                        { name:'My Way', path:'#' }-->
<!--                    ]" />-->
<!--                  </UlComponent>-->
                </div>
              </div>
            </el-tab-panels>
          </el-tab-group>
          <div class="space-y-6 border-t border-gray-200 px-4 py-6">
            <div class="flow-root">
              <a href="#" class="-m-2 block p-2 font-medium text-gray-900">Company</a>
            </div>
            <div class="flow-root">
              <a href="#" class="-m-2 block p-2 font-medium text-gray-900">Stores</a>
            </div>
          </div>

          <div class="space-y-6 border-t border-gray-200 px-4 py-6">
            <div class="flow-root">
              <router-link to="/login" class="-m-2 block p-2 font-medium text-gray-900">Sign in</router-link>
            </div>
            <div class="flow-root">
              <router-link to="/register" class="-m-2 block p-2 font-medium text-gray-900">Register</router-link>
            </div>
          </div>

          <div class="border-t border-gray-200 px-4 py-6">
            <a href="#" class="-m-2 flex items-center p-2">
              <img src="https://tailwindcss.com/plus-assets/img/flags/flag-canada.svg" alt="" class="block h-auto w-5 shrink-0" />
              <span class="ml-3 block text-base font-medium text-gray-900">CAD</span>
              <span class="sr-only">, change currency</span>
            </a>
          </div>
        </el-dialog-panel>
      </div>
    </dialog>
  </el-dialog>
</template>

<style scoped>

</style>