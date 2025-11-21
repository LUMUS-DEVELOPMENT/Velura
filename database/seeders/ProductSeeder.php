<?php

namespace Database\Seeders;

use App\Models\Product;
use Illuminate\Database\Seeder;

class ProductSeeder extends Seeder
{
    /**
     * Run the database seeds.
     */
    public function run(): void
    {
        $products = [
            [
                'title' => 'Basic Tee',
                'description' => 'Lorem Ipsum Lorem Ipsum',
                'image_path' => 'https://tailwindcss.com/plus-assets/img/ecommerce-images/product-page-01-related-product-01.jpg',
                'price' => 35,
                'quantity' => 3,
                'is_active' => true,
            ],
            [
                'title' => 'Basic Tee',
                'description' => 'Lorem Ipsum Lorem Ipsum',
                'image_path' => 'https://tailwindcss.com/plus-assets/img/ecommerce-images/product-page-01-related-product-02.jpg',
                'price' => 35,
                'quantity' => 6,
                'is_active' => true,
            ],
            [
                'title' => 'Basic Tee',
                'description' => 'Lorem Ipsum Lorem Ipsum',
                'image_path' => 'https://tailwindcss.com/plus-assets/img/ecommerce-images/product-page-01-related-product-03.jpg',
                'price' => 35,
                'quantity' => 15,
                'is_active' => true,
            ],
            [
                'title' => 'Basic Tee',
                'description' => 'Lorem Ipsum Lorem Ipsum',
                'image_path' => 'https://tailwindcss.com/plus-assets/img/ecommerce-images/product-page-01-related-product-04.jpg',
                'price' => 35,
                'quantity' => 5,
                'is_active' => true,
            ],
        ];

        foreach ($products as $p) {
            Product::create($p);
        }
    }
}
