<script setup>
import LinkList from "@/components/ui/shared/LinkList.vue";
import MainNav from "@/components/ui/shared/MainNav.vue";

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
        <MainNav />

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
