<script setup>
import useWomen from "@/composables/menu/useWomen.js";
import useMen from "@/composables/menu/useMen.js";
import NavItem from "@/components/ui/shared/menu/NavItem.vue";
import Logo from "@/components/Icons/Logo.vue";

defineOptions({name: "MainNav" })
const womenMenu = useWomen();
const menMenu = useMen();
</script>
<template>
  <nav aria-label="Top" class="w-1/5 ml-10 flex justify-between ">
    <div class="flex items-center gap-5">
      <!-- Logo -->
      <Logo />
      <!--Menu -->
      <NavItem id="mobile-menu" label="Women" menuId="desktop-menu-women" :menuData="womenMenu"/>
      <NavItem id="mobile-menu"  label="Men" menuId="desktop-menu-men" :menuData="menMenu"/>
    </div>
  </nav>
</template>
