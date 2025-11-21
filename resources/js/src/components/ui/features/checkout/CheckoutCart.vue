<script setup>
import {RouterLink} from "vue-router";
import CheckoutItem from "@/components/ui/features/checkout/CheckoutItem.vue";
import CheckoutButton from "@/components/ui/features/checkout/CheckoutButton.vue";
import {useCartStore} from "@/stores/useCartStore.js";

const cart = useCartStore();

</script>
<template>
    <div class="relative">
        <CheckoutButton :count="cart.count" @click="cart.toggleCart"/>

        <transition name="fade">
            <div v-if="cart.isOpen"
                 class="absolute right-0 mt-2 w-112 bg-white shadow-xl rounded-lg border p-3 z-50">
                <h3 class="font-semibold text-gray-800 mb-2">Your Cart</h3>
                <div v-if="cart.count === 0" class="text-sm text-gray-500 py-2 text-center">
                    Your cart is empty.
                </div>

                <div v-else class="space-y-2">
                    <CheckoutItem v-for="item in cart.items"
                                  :key="item.id"
                                  :item="item"
                    >

                        <div class="flex items-center gap-1 sm:gap-2">
                            <Button @click="cart.decreaseItemQty(item)" class="px-2 py-1 bg-gray-200 rounded">
                                -
                            </Button>
                            <Input
                                v-model.number="item.qty"
                                @update:modelValue="value => cart.setQty(item, value)"
                                @blur="() => cart.setQty(item, item.qty, true)"
                                class="w-12 text-center"
                            />
                            <Button @click="cart.increaseItemQty(item)" class="px-2 py-1 bg-gray-200 rounded">
                                +
                            </Button>

                            <Button type="button" @click="cart.removeItem(item)" :override="true">
                                <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24"
                                     stroke-width="1.5" stroke="currentColor" class="size-6">
                                    <path stroke-linecap="round" stroke-linejoin="round"
                                          d="M12 9.75 14.25 12m0 0 2.25 2.25M14.25 12l2.25-2.25M14.25 12 12 14.25m-2.58 4.92-6.374-6.375a1.125 1.125 0 0 1 0-1.59L9.42 4.83c.21-.211.497-.33.795-.33H19.5a2.25 2.25 0 0 1 2.25 2.25v10.5a2.25 2.25 0 0 1-2.25 2.25h-9.284c-.298 0-.585-.119-.795-.33Z"/>
                                </svg>
                            </Button>
                        </div>

                    </CheckoutItem>
                    <span class="font-bold text-lg text-gray-800">Total: {{new Intl.NumberFormat('en-US', {style: 'currency', currency: 'USD'}).format(cart.total) }}</span>
                    <div class="flex justify-between">
                        <RouterLink
                            to="/checkout"
                            class="block mt-3 text-center bg-black text-white py-2 rounded-md hover:bg-gray-900 transition p-4">
                            Checkout
                        </RouterLink>
                        <Button type="button" :override="true" @click="cart.clear()">
                            <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke-width="1.5"
                                 stroke="currentColor" class="size-6">
                                <path stroke-linecap="round" stroke-linejoin="round"
                                      d="m14.74 9-.346 9m-4.788 0L9.26 9m9.968-3.21c.342.052.682.107 1.022.166m-1.022-.165L18.16 19.673a2.25 2.25 0 0 1-2.244 2.077H8.084a2.25 2.25 0 0 1-2.244-2.077L4.772 5.79m14.456 0a48.108 48.108 0 0 0-3.478-.397m-12 .562c.34-.059.68-.114 1.022-.165m0 0a48.11 48.11 0 0 1 3.478-.397m7.5 0v-.916c0-1.18-.91-2.164-2.09-2.201a51.964 51.964 0 0 0-3.32 0c-1.18.037-2.09 1.022-2.09 2.201v.916m7.5 0a48.667 48.667 0 0 0-7.5 0"/>
                            </svg>
                        </Button>
                    </div>
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
