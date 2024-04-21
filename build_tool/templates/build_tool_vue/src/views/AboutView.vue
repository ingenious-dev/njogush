<!-- <template>
  <div class="about">
    <h1>This is an about page</h1>
  </div>
</template> -->
<template>
  <div>
    <div class="relative bg-indigo-800">
      <div class="absolute inset-0">
        <img class="h-full w-full object-cover" :src="njogu" alt="" />
        <div class="absolute inset-0 bg-indigo-800 mix-blend-multiply" aria-hidden="true" />
      </div>
      <div class="relative mx-auto max-w-7xl py-24 px-6 sm:py-32 lg:px-8">
        <h1 class="text-4xl font-bold tracking-tight text-white sm:text-5xl lg:text-6xl">njogush</h1>
        <p class="mt-6 max-w-3xl text-xl text-indigo-100">Njogush is a tool that helps developers work smarter. It provides a set of frequently used actions. It simplifies tasks to their basic parts. Complex tasks are designed as collection of simpler ones</p>
      </div>
    </div>

    <div class="bg-indigo-200 bg-opacity-25">
      <div class="mx-auto max-w-7xl py-16 px-6 sm:py-24 lg:px-8">
        <div class="lg:grid lg:grid-cols-2 lg:gap-8">
          <h2 class="mx-auto max-w-md text-center text-3xl font-bold tracking-tight text-indigo-900 lg:max-w-xl lg:text-left">Learn more about njogush</h2>
          <div class="mt-8 flow-root self-center lg:mt-0">
            <div class="-mt-4 -ml-8 flex flex-wrap justify-between lg:-ml-4">
              <a href="https://njogush.ingenious.or.ke" target="_blank" class="mt-4 ml-8 flex flex-shrink-0 flex-grow justify-center lg:ml-4 lg:flex-grow-0 lg:w-1/4">
                <img class="h-12 object-contain" :src="image" alt="njogush" />
              </a>
              <a href="https://github.com/ingenious-dev/njogush" target="_blank" class="mt-4 ml-8 flex flex-shrink-0 flex-grow justify-center lg:ml-4 lg:flex-grow-0 lg:w-1/4">
                <img class="h-12 object-contain" src="https://github.githubassets.com/assets/GitHub-Logo-ee398b662d42.png" alt="github" />
              </a>
              <a href="https://ingenious.or.ke" target="_blank" class="mt-4 ml-8 flex flex-shrink-0 flex-grow justify-center lg:ml-4 lg:flex-grow-0 lg:w-1/4">
                <img class="h-12 object-contain" src="https://ingenious.or.ke/static//img/ingenious%20logo%20-%20cropped.png" alt="ingenious" />
              </a>
            </div>
          </div>
        </div>
      </div>
    </div>

    <div class="bg-white">
      <div class="mx-auto max-w-7xl py-12 px-6 lg:py-16 lg:px-8">
        <p class="text-center text-lg font-semibold text-gray-600">Library & Frameworks used</p>
        <div class="mt-6 grid grid-cols-2 gap-0.5 md:grid-cols-3 lg:mt-8">
          <div class="col-span-1 flex justify-center bg-gray-50 py-8 px-8">
            <img class="max-h-12 object-contain" :src="django" alt="Workcation" />
          </div>
          <div class="col-span-1 flex justify-center bg-gray-50 py-8 px-8">
            <img class="max-h-12 object-contain" :src="vuejs" alt="Mirage" />
          </div>
          <div class="col-span-1 flex justify-center bg-gray-50 py-8 px-8">
            <img class="max-h-12 object-contain" :src="tailwind" alt="Tuple" />
          </div>
          <!-- <div class="col-span-1 flex justify-center bg-gray-50 py-8 px-8">
            <img class="max-h-12" src="https://tailwindui.com/img/logos/laravel-logo-gray-400.svg" alt="Laravel" />
          </div>
          <div class="col-span-1 flex justify-center bg-gray-50 py-8 px-8">
            <img class="max-h-12" src="https://tailwindui.com/img/logos/statickit-logo-gray-400.svg" alt="StaticKit" />
          </div>
          <div class="col-span-1 flex justify-center bg-gray-50 py-8 px-8">
            <img class="max-h-12" src="https://tailwindui.com/img/logos/statamic-logo-gray-400.svg" alt="Statamic" />
          </div> -->
        </div>
      </div>
    </div>

  </div>
</template>

<script setup>
import image from "../assets/build.png"
import njogu from "../assets/IMG_0709.jpg"

import django from "../assets/Django_logo.svg.png"
import vuejs from "../assets/pngegg (1).png"
import tailwind from "../assets/Tailwind_CSS_logo.svg.png"

</script>
<style>
@media (min-width: 1024px) {
  .about {
    min-height: 100vh;
    display: flex;
    align-items: center;
  }
}
</style>
