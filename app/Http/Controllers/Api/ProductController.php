<?php

namespace App\Http\Controllers\Api;

use App\Http\Controllers\Controller;
use App\Http\Resources\ProductResource;
use App\Models\Product;
use Illuminate\Http\Resources\Json\AnonymousResourceCollection;

class ProductController extends Controller
{
   public function index(): AnonymousResourceCollection
   {
       return ProductResource::collection(Product::where('is_active', true)
           ->latest()
           ->paginate(12)
       );
   }

   public function show($id): ProductResource
   {
       return new ProductResource(Product::where('is_active', true)->findOrFail($id));
   }
}
