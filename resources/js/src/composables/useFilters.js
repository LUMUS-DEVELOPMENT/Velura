import { ref } from "vue";

export function useFilters() {
    const products = ref([
        {
            id: 1,
            title: "Basic Tee",
            description: 'Lorem Ipsum Lorem Ipsum',
            imagePath: "https://tailwindcss.com/plus-assets/img/ecommerce-images/product-page-01-related-product-01.jpg",
            price: "35",
        },
        {
            id: 2,
            title: "Basic Tee",
            description: 'Lorem Ipsum Lorem Ipsum',
            imagePath: "https://tailwindcss.com/plus-assets/img/ecommerce-images/product-page-01-related-product-02.jpg",
            price: "35",
        },
        {
            id: 3,
            title: "Basic Tee",
            description: 'Lorem Ipsum Lorem Ipsum',
            imagePath: "https://tailwindcss.com/plus-assets/img/ecommerce-images/product-page-01-related-product-03.jpg",
            price: "35",
        },
        {
            id: 4,
            title: "Basic Tee",
            description: 'Lorem Ipsum Lorem Ipsum',
            imagePath: "https://tailwindcss.com/plus-assets/img/ecommerce-images/product-page-01-related-product-04.jpg",
            price: "35",
        }
    ]);

    return { filters};
}
