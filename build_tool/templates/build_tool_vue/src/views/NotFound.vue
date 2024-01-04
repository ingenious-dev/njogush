<template>
  <!--
    This example requires updating your template:

    ```
    <html class="h-full">
    <body class="h-full">
    ```
  -->
  <div class="flex min-h-full flex-col bg-white lg:relative">
    <div class="flex flex-grow flex-col">
      <main class="flex flex-grow flex-col bg-white">
        <div class="mx-auto flex w-full max-w-7xl flex-grow flex-col px-6 lg:px-8">
          <div class="flex-shrink-0 pt-10 sm:pt-16">
            <a href="/" class="inline-flex">
              <span class="sr-only">Your Company</span>
              <img class="h-12 w-auto" :src="image" alt="" />
            </a>
          </div>
          <div class="my-auto flex-shrink-0 py-16 sm:py-32">
            <p class="text-base font-semibold text-indigo-600">404</p>
            <h1 class="mt-2 text-4xl font-bold tracking-tight text-gray-900 sm:text-5xl">Page not found</h1>
            <p class="mt-2 text-base text-gray-500">Sorry, we couldn’t find the page you’re looking for.</p>
            <div class="mt-6">
              <router-link to="/">
              <a href="#" class="text-base font-medium text-indigo-600 hover:text-indigo-500">
                Go back home
                <span aria-hidden="true"> &rarr;</span>
              </a>
            </router-link>
            </div>
          </div>
        </div>
      </main>
      <footer class="flex-shrink-0 bg-gray-50">
        <div class="mx-auto w-full max-w-7xl py-16 px-6 lg:px-8">
          <nav class="flex space-x-4">
            <!-- <a href="#" class="text-sm font-medium text-gray-500 hover:text-gray-600">Contact Support</a>
            <span class="inline-block border-l border-gray-300" aria-hidden="true" />
            <a href="#" class="text-sm font-medium text-gray-500 hover:text-gray-600">Status</a>
            <span class="inline-block border-l border-gray-300" aria-hidden="true" />
            <a href="#" class="text-sm font-medium text-gray-500 hover:text-gray-600">Twitter</a> -->
          </nav>
        </div>
      </footer>
    </div>
    <div class="hidden lg:absolute lg:inset-y-0 lg:right-0 lg:block lg:w-1/2">
      <img class="absolute inset-0 h-full w-full object-cover" :src="njogu2" alt="" />
    </div>
  </div>
</template>

<script setup>
import image from "../assets/build.png"
import njogu2 from "../assets/IMG_0708.jpg"
</script>