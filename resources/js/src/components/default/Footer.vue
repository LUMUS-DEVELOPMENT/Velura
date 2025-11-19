<template>
  <footer class="bg-neutral-primary-soft rounded-base shadow-xs  border-default m-4">
    <div class="w-full max-w-screen-xl mx-auto p-4 md:py-8">
      <div class="sm:flex sm:items-center sm:justify-between">
        <router-link to="/" class="flex items-center mb-4 sm:mb-0 space-x-3 rtl:space-x-reverse">
          <Logo />
        </router-link>
        <LinkList
            className="flex flex-wrap items-center mb-6 text-sm font-medium text-body sm:mb-0"
            linkClassName="hover:underline me-4 md:me-6"
            :links="[
                { name:'About', paths:'#' },
                { name:'Privacy Policy', paths:'#' },
                { name:'Licensing', paths:'#' },
                { name:'Contact',  paths:'#' }
            ]"
        />
      </div>
      <hr class="my-6 border-default sm:mx-auto lg:my-8" />
      <span class="block text-sm text-body sm:text-center">© 2023 <router-link to="#" class="hover:underline"> Velura™ </router-link>. All Rights Reserved.</span>
    </div>
  </footer>
</template>
<script setup>
import Logo from "@/components/Icons/Logo.vue";
import LinkList from "@/components/ui/shared/LinkList.vue";
</script>
