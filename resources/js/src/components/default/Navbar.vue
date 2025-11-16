<template>
    <MainNav />
  <div class="ml-auto flex items-center gap-4">
    <!-- Search -->
    <SearchForm />
    <!-- Language -->
    <Lang />
    <!-- Cart -->
    <CheckoutCart />
    <!-- Auth -->
    <div class="w-full flex items-center gap-2">
      <router-link to="/login"   class="text-sm font-medium text-gray-700 hover:text-gray-800">Sign in</router-link>
      <router-link to="/register" class="text-sm font-medium text-gray-700 hover:text-gray-800" >Sign up</router-link>
    </div>
  </div>
</template>
<script setup>
import SearchForm from "@/components/ui/search/SearchForm.vue";
import MainNav from "@/components/ui/shared//MainNav.vue";
import Lang from "@/components/ui/lang/Lang.vue";
import CheckoutCart from "@/components/ui/checkout/CheckoutCart.vue";
</script>