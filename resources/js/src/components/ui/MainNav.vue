<script setup>
import useWomen from "@/composables/menu/useWomen.js";
import useMen from "@/composables/menu/useMen.js";

defineOptions({name: "MainNav" })
const womenMenu = useWomen();
const menMenu = useMen();
</script>
<template>
  <nav aria-label="Top" class="ml-10">
    <div class="flex items-center gap-5">
      <NavItem label="Women" menuId="desktop-menu-women" :menuData="womenMenu"/>
      <NavItem label="Men" menuId="desktop-menu-men" :menuData="menMenu"/>
    </div>
  </nav>
</template>
