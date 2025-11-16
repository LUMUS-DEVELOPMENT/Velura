<script setup>
import Header from "@/components/default/Header.vue";
import Footer from "@/components/default/Footer.vue";
import Navbar from "@/components/default/Navbar.vue";
</script>

<template>
  <Header>
    <Navbar />
  </Header>
    <router-view></router-view>
  <Footer>

  </Footer>
</template>

<style scoped>

</style>
