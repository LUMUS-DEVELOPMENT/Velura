<script setup>

import UlComponent from "@/components/ui/Ul-component.vue";
import LiComponent from "@/components/ui/Li-component.vue";

</script>
<template>
  <nav aria-label="Top" class="mx-auto max-w-7xl px-4 sm:px-6 lg:px-8">
    <div class="border-b border-gray-200">
      <div class="flex h-16 items-center">
        <button type="button" command="show-modal" commandfor="mobile-menu" class="relative rounded-md bg-white p-2 text-gray-400 lg:hidden">
          <span class="absolute -inset-0.5"></span>
          <span class="sr-only">Open menu</span>
          <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5" data-slot="icon" aria-hidden="true" class="size-6">
            <path d="M3.75 6.75h16.5M3.75 12h16.5m-16.5 5.25h16.5" stroke-linecap="round" stroke-linejoin="round" />
          </svg>
        </button>
        <!-- Logo -->
        <div class="ml-4 flex lg:ml-0">
          <router-link :to="{name: 'home'}">
            <span class="sr-only">Your Company</span>
            <img src="https://tailwindcss.com/plus-assets/img/logos/mark.svg?color=indigo&shade=600" alt="" class="h-8 w-auto" />
          </router-link>
        </div>
        <!-- Flyout menus -->
        <el-popover-group class="group/popover-group hidden lg:ml-8 lg:block lg:self-stretch">
          <div class="flex h-full space-x-8">
            <div class="group/popover flex">
              <div class="relative flex">
                <button popovertarget="desktop-menu-women" class="relative flex items-center justify-center text-sm font-medium transition-colors duration-200 ease-out group-not-has-open/popover:text-gray-700 group-has-open/popover:text-indigo-600 group-not-has-open/popover:hover:text-gray-800">
                  Women
                  <span aria-hidden="true" class="absolute inset-x-0 -bottom-px z-30 h-0.5 bg-transparent duration-200 ease-in group-has-open/popover:bg-indigo-600 group-has-open/popover-group:duration-150 group-has-open/popover-group:ease-out"></span>
                </button>
              </div>
              <el-popover id="desktop-menu-women" anchor="bottom" popover class="w-full overflow-visible bg-white text-sm text-gray-500 transition transition-discrete [--anchor-gap:1px] backdrop:bg-transparent open:block data-closed:opacity-0 data-enter:duration-200 data-enter:ease-out data-leave:duration-150 data-leave:ease-in">
                <!-- Presentational element used to render the bottom shadow, if we put the shadow on the actual panel it pokes out the top, so we use this shorter element to hide the top of the shadow -->
                <div aria-hidden="true" class="absolute inset-0 top-1/2 bg-white shadow-sm"></div>
                <div class="relative bg-white">
                  <div class="mx-auto max-w-7xl px-4 sm:px-6 lg:px-8">
                    <div class="grid grid-cols-2 gap-x-8 gap-y-10 py-16">
                      <div class="col-start-2 grid grid-cols-2 gap-x-8">
                        <div class="group relative text-base sm:text-sm">
                          <img src="https://tailwindcss.com/plus-assets/img/ecommerce-images/mega-menu-category-01.jpg" alt="Models sitting back to back, wearing Basic Tee in black and bone." class="aspect-square w-full rounded-lg bg-gray-100 object-cover group-hover:opacity-75" />
                          <a href="#" class="mt-6 block font-medium text-gray-900">
                            <span aria-hidden="true" class="absolute inset-0 z-10"></span>
                            New Arrivals
                          </a>
                          <p aria-hidden="true" class="mt-1">Shop now</p>
                        </div>
                        <div class="group relative text-base sm:text-sm">
                          <img src="https://tailwindcss.com/plus-assets/img/ecommerce-images/mega-menu-category-02.jpg" alt="Close up of Basic Tee fall bundle with off-white, ochre, olive, and black tees." class="aspect-square w-full rounded-lg bg-gray-100 object-cover group-hover:opacity-75" />
                          <a href="#" class="mt-6 block font-medium text-gray-900">
                            <span aria-hidden="true" class="absolute inset-0 z-10"></span>
                            Basic Tees
                          </a>
                          <p aria-hidden="true" class="mt-1">Shop now</p>
                        </div>
                      </div>
                      <div class="row-start-1 grid grid-cols-3 gap-x-8 gap-y-10 text-sm">
                        <div>
                          <p id="Clothing-heading" class="font-medium text-gray-900">Clothing</p>
                          <UlComponent id="Clothing-heading" class="mt-6 space-y-6 sm:mt-4 sm:space-y-4"
                                       ariaLabelledby="Clothing-heading">
                            <li-component className="hover:text-gray-800" liClassName="flex"
                                          :links="[
                                                        { name: 'Tops', path: '/tops' },
                                                        { name: 'Dresses', path: '/dresses' },
                                                        { name: 'Pants', path: '/pants'},
                                                        { name: 'Denim', path: '/denim'},
                                                        { name: 'Sweaters', path: '/sweaters'},
                                                        { name: 'T-Shirts', path: '/tshirts'},
                                                        { name: 'Jackets', path: '/jackets'},
                                                        { name: 'Activewear', path: '/activewear' },
                                                        { name: 'Browse All', path: '/all' }
                                                    ]"/>
                          </UlComponent>
                        </div>
                        <div>
                          <p id="Accessories-heading" class="font-medium text-gray-900">Accessories</p>
                          <UlComponent id="Accessories-heading" class="mt-6 space-y-6 sm:mt-4 sm:space-y-4"
                                       ariaLabelledby="Accessories-heading">
                            <li-component className="hover:text-gray-800" liClassName="flex"
                                          :links="[
                                                        { name: 'Watches', path: '/Watches' },
                                                        { name: 'Wallets', path: '/Wallets' },
                                                        { name: 'Bags', path: '/Bags', },
                                                        { name: 'Sunglasses', path: '/Sunglasses' },
                                                        { name: 'Hats', path: '/Hats' },
                                                        { name: 'Belts', path: '/Belts' }
                                                    ]"/>
                          </UlComponent>
                        </div>
                        <div>
                          <p id="Brands-heading" class="font-medium text-gray-900">Brands</p>
                          <UlComponent id="Brands-heading" class="mt-6 space-y-6 sm:mt-4 sm:space-y-4"
                                       ariaLabelledby="Brands-heading">
                            <li-component className="hover:text-gray-800" liClassName="flex"
                                          :links="[
                                                        { name: 'Full Nelson', path: '/Watches'},
                                                        { name: 'My Way', path: '/Wallets' },
                                                        { name: 'Re-Arranged', path: '/Bags' },
                                                        { name: 'Counterfeit', path: '/Sunglasses' },
                                                        { name: 'Significant Other', path: '/Hats'}
                                                    ]"/>
                          </UlComponent>
                        </div>
                      </div>
                    </div>
                  </div>
                </div>
              </el-popover>
            </div>
            <div class="group/popover flex">
              <div class="relative flex">
                <button popovertarget="desktop-menu-men" class="relative flex items-center justify-center text-sm font-medium transition-colors duration-200 ease-out group-not-has-open/popover:text-gray-700 group-has-open/popover:text-indigo-600 group-not-has-open/popover:hover:text-gray-800">
                  Men
                  <span aria-hidden="true" class="absolute inset-x-0 -bottom-px z-30 h-0.5 bg-transparent duration-200 ease-in group-has-open/popover:bg-indigo-600 group-has-open/popover-group:duration-150 group-has-open/popover-group:ease-out"></span>
                </button>
              </div>
              <el-popover id="desktop-menu-men" anchor="bottom" popover class="w-full overflow-visible bg-white text-sm text-gray-500 transition transition-discrete [--anchor-gap:1px] backdrop:bg-transparent open:block data-closed:opacity-0 data-enter:duration-200 data-enter:ease-out data-leave:duration-150 data-leave:ease-in">
                <!-- Presentational element used to render the bottom shadow, if we put the shadow on the actual panel it pokes out the top, so we use this shorter element to hide the top of the shadow -->
                <div aria-hidden="true" class="absolute inset-0 top-1/2 bg-white shadow-sm"></div>
                <div class="relative bg-white">
                  <div class="mx-auto max-w-7xl px-4 sm:px-6 lg:px-8">
                    <div class="grid grid-cols-2 gap-x-8 gap-y-10 py-16">
                      <div class="col-start-2 grid grid-cols-2 gap-x-8">
                        <div class="group relative text-base sm:text-sm">
                          <img src="https://tailwindcss.com/plus-assets/img/ecommerce-images/product-page-04-detail-product-shot-01.jpg" alt="Drawstring top with elastic loop closure and textured interior padding." class="aspect-square w-full rounded-lg bg-gray-100 object-cover group-hover:opacity-75" />
                          <a href="#" class="mt-6 block font-medium text-gray-900">
                            <span aria-hidden="true" class="absolute inset-0 z-10"></span>
                            New Arrivals
                          </a>
                          <p aria-hidden="true" class="mt-1">Shop now</p>
                        </div>
                        <div class="group relative text-base sm:text-sm">
                          <img src="https://tailwindcss.com/plus-assets/img/ecommerce-images/category-page-02-image-card-06.jpg" alt="Three shirts in gray, white, and blue arranged on table with same line drawing of hands and shapes overlapping on front of shirt." class="aspect-square w-full rounded-lg bg-gray-100 object-cover group-hover:opacity-75" />
                          <a href="#" class="mt-6 block font-medium text-gray-900">
                            <span aria-hidden="true" class="absolute inset-0 z-10"></span>
                            Artwork Tees
                          </a>
                          <p aria-hidden="true" class="mt-1">Shop now</p>
                        </div>
                      </div>
                      <div class="row-start-1 grid grid-cols-3 gap-x-8 gap-y-10 text-sm">
                        <div>
                          <p id="Clothing-heading" class="font-medium text-gray-900">Clothing</p>
                          <UlComponent id="Brands-heading" class="mt-6 space-y-6 sm:mt-4 sm:space-y-4"
                                       ariaLabelledby="Brands-heading">
                            <li-component className="hover:text-gray-800" liClassName="flex"
                                          :links="[
                                                        { name: 'Tops', path: '/Watches'},
                                                        { name: 'Pants', path: '/Wallets' },
                                                        { name: 'Sweaters', path: '/Bags' },
                                                        { name: 'T-Shirts', path: '/Sunglasses' },
                                                        { name: 'Jackets', path: '/Hats'},
                                                        { name: 'Activewear', path: '/Hats'},
                                                        { name: 'Browse All', path: '/Hats'}
                                                    ]"/>
                          </UlComponent>
                        </div>
                        <div>
                          <p id="Accessories-heading" class="font-medium text-gray-900">Accessories</p>
                          <UlComponent  id="Accessories-heading" class="mt-6 space-y-6 sm:mt-4 sm:space-y-4"
                                        ariaLabelledby="Accessories-heading">
                            <li-component className="hover:text-gray-800" liClassName="flex"
                                          :links="[
                                                        { name: 'Watches', path: '/Watches'},
                                                        { name: 'Wallets', path: '/Wallets' },
                                                        { name: 'Bags', path: '/Bags' },
                                                        { name: 'Sunglasses', path: '/Sunglasses' },
                                                        { name: 'Hats', path: '/Hats'},
                                                        { name: 'Activewear', path: '/Hats'},
                                                        { name: 'Belts', path: '/Hats'}
                                                    ]"/>
                          </UlComponent>
                        </div>
                        <div>
                          <p id="Brands-heading" class="font-medium text-gray-900">Brands</p>
                          <UlComponent id="Brands-heading" class="mt-6 space-y-6 sm:mt-4 sm:space-y-4"
                                       ariaLabelledby="Brands-heading">
                            <li-component className="hover:text-gray-800" liClassName="flex"
                                          :links="[
                                                        { name: 'Re-Arranged', path: '/Watches'},
                                                        { name: 'Counterfeit', path: '/Wallets' },
                                                        { name: 'Full Nelson', path: '/Bags' },
                                                        { name: 'My Way', path: '/Sunglasses' },
                                                    ]"/>
                          </UlComponent>
                        </div>
                      </div>
                    </div>
                  </div>
                </div>
              </el-popover>
            </div>
            <router-link :to="{ name: 'products.index'}" class="flex items-center text-sm font-medium text-gray-700 hover:text-gray-800">Products</router-link>
            <router-link to="#" class="flex items-center text-sm font-medium text-gray-700 hover:text-gray-800">Stores</router-link>
          </div>
        </el-popover-group>

        <div class="ml-auto flex items-center">
          <div class="hidden lg:flex lg:flex-1 lg:items-center lg:justify-end lg:space-x-6">
            <router-link to="/login"   class="text-sm font-medium text-gray-700 hover:text-gray-800">Sign in</router-link>
              <span aria-hidden="true" class="h-6 w-px bg-gray-200"></span>
            <router-link to="/register" class="text-sm font-medium text-gray-700 hover:text-gray-800" >Sign up</router-link>
          </div>

          <div class="hidden lg:ml-8 lg:flex">
            <a href="#" class="flex items-center text-gray-700 hover:text-gray-800">
              <img src="https://tailwindcss.com/plus-assets/img/flags/flag-canada.svg" alt="" class="block h-auto w-5 shrink-0" />
              <span class="ml-3 block text-sm font-medium">CAD</span>
              <span class="sr-only">, change currency</span>
            </a>
          </div>
          <!-- Search -->
          <div class="flex lg:ml-6">
            <a href="#" class="p-2 text-gray-400 hover:text-gray-500">
              <span class="sr-only">Search</span>
              <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5" data-slot="icon" aria-hidden="true" class="size-6">
                <path d="m21 21-5.197-5.197m0 0A7.5 7.5 0 1 0 5.196 5.196a7.5 7.5 0 0 0 10.607 10.607Z" stroke-linecap="round" stroke-linejoin="round" />
              </svg>
            </a>
          </div>
          <!-- Cart -->
          <div class="ml-4 flow-root lg:ml-6">
            <a href="#" class="group -m-2 flex items-center p-2">
              <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5" data-slot="icon" aria-hidden="true" class="size-6 shrink-0 text-gray-400 group-hover:text-gray-500">
                <path d="M15.75 10.5V6a3.75 3.75 0 1 0-7.5 0v4.5m11.356-1.993 1.263 12c.07.665-.45 1.243-1.119 1.243H4.25a1.125 1.125 0 0 1-1.12-1.243l1.264-12A1.125 1.125 0 0 1 5.513 7.5h12.974c.576 0 1.059.435 1.119 1.007ZM8.625 10.5a.375.375 0 1 1-.75 0 .375.375 0 0 1 .75 0Zm7.5 0a.375.375 0 1 1-.75 0 .375.375 0 0 1 .75 0Z" stroke-linecap="round" stroke-linejoin="round" />
              </svg>
              <span class="ml-2 text-sm font-medium text-gray-700 group-hover:text-gray-800">0</span>
              <span class="sr-only">items in cart, view bag</span>
            </a>
          </div>
        </div>
      </div>
    </div>
  </nav>
</template>
