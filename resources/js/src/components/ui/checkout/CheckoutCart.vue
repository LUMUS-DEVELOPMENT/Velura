<script setup>
import { ref, computed } from "vue";
import { RouterLink } from "vue-router";
import CheckoutItem from "@/components/ui/checkout/CheckoutItem.vue";
import CheckoutButton from "@/components/ui/checkout/CheckoutButton.vue";

const open = ref(false);

const items = ref([
  { id: 1, title: "Product 1", price: 35 },
  { id: 2, title: "Product 2", price: 29 },
  { id: 3, title: "Product 3", price: 25 },
]);

const count = computed(() => items.value.length);
function toggleCart() {
  open.value = !open.value;
}
</script>
<template>
  <div class="relative">
 <CheckoutButton :count={count} @click="toggleCart" />
    <transition name="fade">
      <div v-if="open" class="absolute right-0 mt-2 w-64 bg-white shadow-xl rounded-lg border p-3 z-50">
        <h3 class="font-semibold text-gray-800 mb-2">Your Cart</h3>
        <div v-if="count === 0" class="text-sm text-gray-500 py-2 text-center">
          Your cart is empty.
        </div>
        <div v-else class="space-y-2">
          <CheckoutItem
              v-for="item in items"
              :key="item.id"
              :item="item"
          />
          <RouterLink to="/checkout"
              class="block mt-3 text-center bg-black text-white py-2 rounded-md hover:bg-gray-900 transition">
            Checkout
          </RouterLink>
        </div>
      </div>
    </transition>
  </div>
</template>

<style scoped>
.fade-enter-active,
.fade-leave-active {
  transition: opacity 0.15s ease, transform 0.15s ease;
}
.fade-enter-from,
.fade-leave-to {
  opacity: 0;
  transform: translateY(-5px);
}
</style>
