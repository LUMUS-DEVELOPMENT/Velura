<script setup>
import useWomen from "@/composables/menu/useWomen.js";
import useMen from "@/composables/menu/useMen.js";

defineOptions({name: "MainNav" })
const womenMenu = useWomen();
const menMenu = useMen();
</script>
<template>
  <nav aria-label="Top" class="w-1/5 ml-10 flex justify-between ">
    <div class="flex items-center gap-5">
      <button type="button" command="show-modal" commandfor="mobile-menu" class="relative rounded-md bg-white p-2 text-gray-400 lg:hidden">
        <span class="absolute -inset-0.5"></span>
        <span class="sr-only">Open menu</span>
        <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5" data-slot="icon" aria-hidden="true" class="size-6">
          <path d="M3.75 6.75h16.5M3.75 12h16.5m-16.5 5.25h16.5" stroke-linecap="round" stroke-linejoin="round" />
        </svg>
      </button>
      <!-- Logo -->
      <div class=" flex lg:ml-0">
        <router-link :to="{name: 'home'}">
          <span class="sr-only">Your Company</span>
          <img src="https://tailwindcss.com/plus-assets/img/logos/mark.svg?color=indigo&shade=600" alt="" class="h-8 w-auto" />
        </router-link>
      </div>
      <NavItem label="Women" menuId="desktop-menu-women" :menuData="womenMenu"/>
      <NavItem label="Men" menuId="desktop-menu-men" :menuData="menMenu"/>

    </div>
  </nav>
</template>
