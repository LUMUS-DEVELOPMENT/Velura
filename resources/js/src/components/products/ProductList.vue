<script setup>
defineProps({
  products: {
    type: Array,
    required: true,
    default:()=>[
        {
          id: 1,
          name:"Basic Tee",
          image:"https://tailwindcss.com/plus-assets/img/ecommerce-images/product-page-01-related-product-01.jpg",
          color:"black",
          price: "35",
        },
        {
          id: 2,
          name:"Basic Tee",
          image:"https://tailwindcss.com/plus-assets/img/ecommerce-images/product-page-01-related-product-02.jpg",
          color:"Aspen White",
          price: "35",
        },
        {
          id: 3,
          name:"Basic Tee",
          image:"https://tailwindcss.com/plus-assets/img/ecommerce-images/product-page-01-related-product-03.jpg",
          color:"Charcoal",
          price: "35",
        },
        {
          id: 4,
          name:"Artwork Tee",
          image:"https://tailwindcss.com/plus-assets/img/ecommerce-images/product-page-01-related-product-04.jpg",
          color:"Iso Dots",
          price: "35",
        }
      ]
  }
})

</script>

<template>
          <div v-for="product in products" class="group relative px-3 pb-3" :key="product.id">
            <img :src="product.image" alt="Front of men&#039;s Basic Tee in black." class="aspect-square w-full rounded-md bg-gray-200 object-cover group-hover:opacity-75 lg:aspect-auto lg:h-80" />
            <div class="mt-4 flex justify-between">
              <div>
                <h3 class="text-sm text-gray-700">
                  <a href="#">
                    <span aria-hidden="true" class="absolute inset-0"></span>
                    {{product.name}}
                  </a>
                </h3>
                <p class="mt-1 text-sm text-gray-500">{{product.color}}</p>
              </div>
              <p class="text-sm font-medium text-gray-900">${{ product.price }}</p>
            </div>
          </div>
</template>

<style scoped>

</style>