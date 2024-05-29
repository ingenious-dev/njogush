<template>
  <main>
    <main class="py-10">
      <!-- Page header -->
      <div class="mx-auto max-w-3xl px-4 sm:px-6 md:flex md:items-center md:justify-between md:space-x-5 lg:max-w-7xl lg:px-8">
        <div class="flex items-center space-x-5">
          <!-- <div class="flex-shrink-0">
            <div class="relative">
              <img class="h-16 w-16 rounded-full" :src="currentProject?.profile?.image" alt="" />
              <span class="absolute inset-0 rounded-full shadow-inner" aria-hidden="true" />
            </div>
          </div> -->
          <div>
            <h1 class="text-2xl font-bold text-gray-900">#{{ currentBuildSession?.id }}: {{ currentProject?.name }}</h1>
            <p class="text-sm font-medium text-gray-500">
              <!-- Applied for <a href="#" class="text-gray-900">Front End Developer</a> on <time datetime="2020-08-25">August 25, 2020</time> -->
              Created <time datetime="2020-08-25">{{ $moment(currentBuildSession?.date_posted).format('MMMM D, YYYY, h:mm:ss a') }}</time>
              <!-- Last modified <time datetime="2020-08-25">{{ $moment(currentProject?.date_modified).format('MMMM D, YYYY') }}</time> -->
            </p>
          </div>
        </div>
        <div v-if="is_running" class="justify-stretch mt-6 flex flex-col-reverse space-y-4 space-y-reverse sm:flex-row-reverse sm:justify-end sm:space-y-0 sm:space-x-3 sm:space-x-reverse md:mt-0 md:flex-row md:space-x-3">
          <button
            type="button"
            class="inline-flex items-center justify-center rounded-md border border-transparent bg-red-600 px-4 py-2 text-sm font-medium text-white shadow-sm hover:bg-red-700 focus:outline-none focus:ring-2 focus:ring-red-500 focus:ring-offset-2 focus:ring-offset-gray-100"
            @click="stop()">
            <svg class="animate-spin -ml-1 mr-3 h-5 w-5 text-white" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24">
              <circle class="opacity-25" cx="12" cy="12" r="10" stroke="currentColor" stroke-width="4"></circle>
              <path class="opacity-75" fill="currentColor" d="M4 12a8 8 0 018-8V0C5.373 0 0 5.373 0 12h4zm2 5.291A7.962 7.962 0 014 12H0c0 3.042 1.135 5.824 3 7.938l3-2.647z"></path>
            </svg>
            Stop</button>
        </div>
        <div v-else class="justify-stretch mt-6 flex flex-col-reverse space-y-4 space-y-reverse sm:flex-row-reverse sm:justify-end sm:space-y-0 sm:space-x-3 sm:space-x-reverse md:mt-0 md:flex-row md:space-x-3">
          <button
            type="button"
            class="inline-flex items-center justify-center rounded-md border border-transparent bg-green-600 px-4 py-2 text-sm font-medium text-white shadow-sm hover:bg-green-700 focus:outline-none focus:ring-2 focus:ring-green-500 focus:ring-offset-2 focus:ring-offset-gray-100"
            @click="run()">
            Continue</button>
          <button
            type="button"
            class="inline-flex items-center justify-center rounded-md border border-transparent bg-blue-600 px-4 py-2 text-sm font-medium text-white shadow-sm hover:bg-blue-700 focus:outline-none focus:ring-2 focus:ring-blue-500 focus:ring-offset-2 focus:ring-offset-gray-100"
            @click="rerun()">
            Run again</button>
        </div>
        
      </div>

      <div class="mx-auto mt-8 grid max-w-3xl grid-cols-1 gap-6 sm:px-6 lg:max-w-7xl lg:grid-flow-col-dense lg:grid-cols-3">
        <div class="space-y-6 lg:col-span-2 lg:col-start-1">

            <div>
              <label for="chat-log" class="block text-sm font-medium text-gray-700">Live Logs</label>
              <div class="mt-1">
                <textarea id="chat-log" name="chat-log" rows="20" class="mt-1 block w-full rounded-md border-gray-300 shadow-sm focus:border-indigo-500 focus:ring-indigo-500 sm:text-sm" placeholder="" ref="chat_log" disabled />
              </div>
            </div>

            </div>

            <div>
              <section aria-labelledby="timeline-title" class="lg:col-span-1 lg:col-start-3">
                <div class="bg-white px-4 py-5 shadow sm:rounded-lg sm:px-6">
                  <h2 id="timeline-title" class="text-lg font-medium text-gray-900">Timeline</h2>

                  <!-- Activity Feed -->
                  <div class="mt-6 flow-root">
                    <ul role="list" class="-mb-8 h-96 overflow-auto">
                      <li v-for="(item, itemIdx) in step_progress" :key="item.id">
                        <div class="relative pb-8">
                          <span v-if="itemIdx !== step_progress.length - 1" class="absolute top-4 left-4 -ml-px h-full w-0.5 bg-gray-200" aria-hidden="true" />
                          <div class="relative flex space-x-3">
                            <div>
                              <span :class="[getClass(item) , 'h-8 w-8 rounded-full flex items-center justify-center ring-8 ring-white']">
                                <component :is="getIcon(item)" class="h-5 w-5 text-white" aria-hidden="true" />
                              </span>
                            </div>
                            <div class="flex min-w-0 flex-1 justify-between space-x-4 pt-1.5">
                              <div>
                                <p class="text-sm text-gray-500">
                                  <!-- {{ item.content }} <a href="#" class="font-medium text-gray-900">{{ item.target }}</a> -->
                                  STEP #{{ item.step.id }}: {{ item.step.name }}
                                </p>
                              </div>
                              <!-- <div class="whitespace-nowrap text-right text-sm text-gray-500">
                                <time :datetime="item.date_posted">{{ $moment(item.date_posted).format('MMM D') }}</time>
                              </div> -->
                            </div>
                          </div>
                        </div>
                      </li>
                    </ul>
                  </div>
                  <!-- <div class="justify-stretch mt-6 flex flex-col">
                    <button
                      type="button"
                      class="inline-flex items-center justify-center rounded-md border border-transparent bg-blue-600 px-4 py-2 text-sm font-medium text-white shadow-sm hover:bg-blue-700 focus:outline-none focus:ring-2 focus:ring-blue-500 focus:ring-offset-2"
                    >Advance to offer</button>
                  </div> -->
                </div>
              </section>
              
            </div>
      </div>

      <div class="mx-auto mt-8 grid max-w-3xl grid-cols-1 gap-6 sm:px-6 lg:max-w-7xl lg:grid-flow-col-dense lg:grid-cols-1">
        <div class="space-y-6 lg:col-span-2 lg:col-start-1">

          <div>
            <label for="previous-chat-log" class="block text-sm font-medium text-gray-700">Previous Logs ({{ $moment(currentBuildSession?.date_modified).format('MMMM D, YYYY, h:mm:ss a') }})</label>
            <div class="mt-1">
              <textarea id="previous-chat-log" name="previous-chat-log" rows="20" class="mt-1 block w-full rounded-md border-gray-300 shadow-sm focus:border-indigo-500 focus:ring-indigo-500 sm:text-sm" placeholder="" disabled :value="currentBuildSession?.logs" />
            </div>
          </div>

        </div>
      </div>

    </main>
    
    <TransitionRoot as="template" :show="open">
      <Dialog as="div" class="relative z-10" @close="open = false">
        <div class="fixed inset-0" />

        <div class="fixed inset-0 overflow-hidden">
          <div class="absolute inset-0 overflow-hidden">
            <div class="pointer-events-none fixed inset-y-0 right-0 flex max-w-full pl-10 sm:pl-16">
              <TransitionChild as="template" enter="transform transition ease-in-out duration-500 sm:duration-700" enter-from="translate-x-full" enter-to="translate-x-0" leave="transform transition ease-in-out duration-500 sm:duration-700" leave-from="translate-x-0" leave-to="translate-x-full">
                <DialogPanel class="pointer-events-auto w-screen max-w-md">
                  <form class="flex h-full flex-col divide-y divide-gray-200 bg-white shadow-xl">
                    <div class="h-0 flex-1 overflow-y-auto">
                      <div class="bg-indigo-700 py-6 px-4 sm:px-6">
                        <div class="flex items-center justify-between">
                          <DialogTitle class="text-lg font-medium text-white">{{ newOrEdit }} Project</DialogTitle>
                          <div class="ml-3 flex h-7 items-center">
                            <button type="button" class="rounded-md bg-indigo-700 text-indigo-200 hover:text-white focus:outline-none focus:ring-2 focus:ring-white" @click="open = false">
                              <span class="sr-only">Close panel</span>
                              <XMarkIcon class="h-6 w-6" aria-hidden="true" />
                            </button>
                          </div>
                        </div>
                        <div class="mt-1">
                          <p class="text-sm text-indigo-300">Fill in the information below to {{ newOrEdit }} your new project.</p>
                        </div>
                      </div>
                      <div class="flex flex-1 flex-col justify-between">
                        <div class="divide-y divide-gray-200 px-4 sm:px-6">
                          <div class="space-y-6 pt-6 pb-5">
                            <div>
                              <label for="project-name" class="block text-sm font-medium text-gray-900">Project name</label>
                              <div class="mt-1">
                                <input
                                type="text"
                                name="project-name"
                                id="project-name"
                                class="block w-full rounded-md border-gray-300 shadow-sm focus:border-indigo-500 focus:ring-indigo-500 sm:text-sm"
                                v-model="name" />
                              </div>
                            </div>
                            <div>
                              <label for="description" class="block text-sm font-medium text-gray-900">Description</label>
                              <div class="mt-1">
                                <textarea id="description" name="description" rows="4" class="block w-full rounded-md border-gray-300 shadow-sm focus:border-indigo-500 focus:ring-indigo-500 sm:text-sm" />
                              </div>
                            </div>
                            <div>
                              <SwitchGroup as="div" class="flex items-center justify-between">
                                <span class="flex flex-grow flex-col">
                                  <SwitchLabel as="span" class="text-sm font-medium text-gray-900" passive>Listed</SwitchLabel>
                                  <SwitchDescription as="span" class="text-sm text-gray-500">Will appear in searches.</SwitchDescription>
                                </span>
                                <Switch v-model="is_listed" :class="[is_listed ? 'bg-indigo-600' : 'bg-gray-200', 'relative inline-flex h-6 w-11 flex-shrink-0 cursor-pointer rounded-full border-2 border-transparent transition-colors duration-200 ease-in-out focus:outline-none focus:ring-2 focus:ring-indigo-500 focus:ring-offset-2']">
                                  <span aria-hidden="true" :class="[is_listed ? 'translate-x-5' : 'translate-x-0', 'pointer-events-none inline-block h-5 w-5 transform rounded-full bg-white shadow ring-0 transition duration-200 ease-in-out']" />
                                </Switch>
                              </SwitchGroup>
                            </div>
                            <div>
                              <SwitchGroup as="div" class="flex items-center justify-between">
                                <span class="flex flex-grow flex-col">
                                  <SwitchLabel as="span" class="text-sm font-medium text-gray-900" passive>Available</SwitchLabel>
                                  <SwitchDescription as="span" class="text-sm text-gray-500">Will be available for use.</SwitchDescription>
                                </span>
                                <Switch v-model="is_available" :class="[is_available ? 'bg-indigo-600' : 'bg-gray-200', 'relative inline-flex h-6 w-11 flex-shrink-0 cursor-pointer rounded-full border-2 border-transparent transition-colors duration-200 ease-in-out focus:outline-none focus:ring-2 focus:ring-indigo-500 focus:ring-offset-2']">
                                  <span aria-hidden="true" :class="[is_available ? 'translate-x-5' : 'translate-x-0', 'pointer-events-none inline-block h-5 w-5 transform rounded-full bg-white shadow ring-0 transition duration-200 ease-in-out']" />
                                </Switch>
                              </SwitchGroup>
                            </div>
                          </div>
                        </div>
                      </div>
                    </div>
                    <div class="flex flex-shrink-0 justify-between px-4 py-4">
                      <button
                        type="button"
                        class="ml-4 inline-flex justify-center rounded-md border border-transparent bg-red-600 py-2 px-4 text-sm font-medium text-white shadow-sm hover:bg-red-700 focus:outline-none focus:ring-2 focus:ring-red-500 focus:ring-offset-2"
                        @click="openModal = true">Delete</button>
                      <div class="flex flex-shrink-0 justify-end">
                        <button type="button" class="rounded-md border border-gray-300 bg-white py-2 px-4 text-sm font-medium text-gray-700 shadow-sm hover:bg-gray-50 focus:outline-none focus:ring-2 focus:ring-indigo-500 focus:ring-offset-2" @click="open = false">Cancel</button>
                        <button
                          type="button"
                          class="ml-4 inline-flex justify-center rounded-md border border-transparent bg-indigo-600 py-2 px-4 text-sm font-medium text-white shadow-sm hover:bg-indigo-700 focus:outline-none focus:ring-2 focus:ring-indigo-500 focus:ring-offset-2"
                          @click="save()">Save</button>
                      </div>
                    </div>
                  </form>
                </DialogPanel>
              </TransitionChild>
            </div>
          </div>
        </div>
      </Dialog>
    </TransitionRoot>

    <TransitionRoot as="template" :show="openModal">
      <Dialog as="div" class="relative z-10" @close="openModal = false">
        <TransitionChild as="template" enter="ease-out duration-300" enter-from="opacity-0" enter-to="opacity-100" leave="ease-in duration-200" leave-from="opacity-100" leave-to="opacity-0">
          <div class="fixed inset-0 bg-gray-500 bg-opacity-75 transition-opacity" />
        </TransitionChild>

        <div class="fixed inset-0 z-10 overflow-y-auto">
          <div class="flex min-h-full items-end justify-center p-4 text-center sm:items-center sm:p-0">
            <TransitionChild as="template" enter="ease-out duration-300" enter-from="opacity-0 translate-y-4 sm:translate-y-0 sm:scale-95" enter-to="opacity-100 translate-y-0 sm:scale-100" leave="ease-in duration-200" leave-from="opacity-100 translate-y-0 sm:scale-100" leave-to="opacity-0 translate-y-4 sm:translate-y-0 sm:scale-95">
              <DialogPanel class="relative transform overflow-hidden rounded-lg bg-white px-4 pt-5 pb-4 text-left shadow-xl transition-all sm:my-8 sm:w-full sm:max-w-lg sm:p-6">
                <div class="absolute top-0 right-0 hidden pt-4 pr-4 sm:block">
                  <button type="button" class="rounded-md bg-white text-gray-400 hover:text-gray-500 focus:outline-none focus:ring-2 focus:ring-indigo-500 focus:ring-offset-2" @click="openModal = false">
                    <span class="sr-only">Close</span>
                    <XMarkIcon class="h-6 w-6" aria-hidden="true" />
                  </button>
                </div>
                <div class="sm:flex sm:items-start">
                  <div class="mx-auto flex h-12 w-12 flex-shrink-0 items-center justify-center rounded-full bg-red-100 sm:mx-0 sm:h-10 sm:w-10">
                    <ExclamationTriangleIcon class="h-6 w-6 text-red-600" aria-hidden="true" />
                  </div>
                  <div class="mt-3 text-center sm:mt-0 sm:ml-4 sm:text-left">
                    <DialogTitle as="h3" class="text-lg font-medium leading-6 text-gray-900">Run project</DialogTitle>
                    <div class="mt-2">
                      <p class="text-sm text-gray-500">Are you sure you want to run the project? This project steps will be executed.</p>
                    </div>
                  </div>
                </div>
                <div class="mt-5 sm:mt-4 sm:flex sm:flex-row-reverse">
                  <button type="button" class="inline-flex w-full justify-center rounded-md border border-transparent bg-red-600 px-4 py-2 text-base font-medium text-white shadow-sm hover:bg-red-700 focus:outline-none focus:ring-2 focus:ring-red-500 focus:ring-offset-2 sm:ml-3 sm:w-auto sm:text-sm" @click="setStatus()">Proceed</button>
                  <button type="button" class="mt-3 inline-flex w-full justify-center rounded-md border border-gray-300 bg-white px-4 py-2 text-base font-medium text-gray-700 shadow-sm hover:text-gray-500 focus:outline-none focus:ring-2 focus:ring-indigo-500 focus:ring-offset-2 sm:mt-0 sm:w-auto sm:text-sm" @click="openModal = false">Cancel</button>
                </div>
              </DialogPanel>
            </TransitionChild>
          </div>
        </div>
      </Dialog>
    </TransitionRoot>

    <TransitionRoot as="template" :show="openModalSocket">
      <Dialog as="div" class="relative z-10" @close="openModalSocket = false">
        <TransitionChild as="template" enter="ease-out duration-300" enter-from="opacity-0" enter-to="opacity-100" leave="ease-in duration-200" leave-from="opacity-100" leave-to="opacity-0">
          <div class="fixed inset-0 bg-gray-500 bg-opacity-75 transition-opacity" />
        </TransitionChild>

        <div class="fixed inset-0 z-10 overflow-y-auto">
          <div class="flex min-h-full items-end justify-center p-4 text-center sm:items-center sm:p-0">
            <TransitionChild as="template" enter="ease-out duration-300" enter-from="opacity-0 translate-y-4 sm:translate-y-0 sm:scale-95" enter-to="opacity-100 translate-y-0 sm:scale-100" leave="ease-in duration-200" leave-from="opacity-100 translate-y-0 sm:scale-100" leave-to="opacity-0 translate-y-4 sm:translate-y-0 sm:scale-95">
              <DialogPanel class="relative transform overflow-hidden rounded-lg bg-white px-4 pt-5 pb-4 text-left shadow-xl transition-all sm:my-8 sm:w-full sm:max-w-lg sm:p-6">
                <div class="absolute top-0 right-0 hidden pt-4 pr-4 sm:block">
                  <button type="button" class="rounded-md bg-white text-gray-400 hover:text-gray-500 focus:outline-none focus:ring-2 focus:ring-indigo-500 focus:ring-offset-2" @click="openModal = false">
                    <span class="sr-only">Close</span>
                    <XMarkIcon class="h-6 w-6" aria-hidden="true" />
                  </button>
                </div>
                <div class="sm:flex sm:items-start">
                  <div class="mx-auto flex h-12 w-12 flex-shrink-0 items-center justify-center rounded-full bg-red-100 sm:mx-0 sm:h-10 sm:w-10">
                    <ExclamationTriangleIcon class="h-6 w-6 text-red-600" aria-hidden="true" />
                  </div>
                  <div class="mt-3 text-center sm:mt-0 sm:ml-4 sm:text-left">
                    <DialogTitle as="h3" class="text-lg font-medium leading-6 text-gray-900">Info</DialogTitle>
                    <div class="mt-2">
                      <p class="text-sm text-gray-500">{{ modalSocketMessage }}</p>
                    </div>
                  </div>
                </div>
                <div class="mt-5 sm:mt-4 sm:flex sm:flex-row-reverse">
                  <!-- <button type="button" class="inline-flex w-full justify-center rounded-md border border-transparent bg-red-600 px-4 py-2 text-base font-medium text-white shadow-sm hover:bg-red-700 focus:outline-none focus:ring-2 focus:ring-red-500 focus:ring-offset-2 sm:ml-3 sm:w-auto sm:text-sm" @click="setStatus()">Try Again</button> -->
                  <button type="button" class="mt-3 inline-flex w-full justify-center rounded-md border border-gray-300 bg-white px-4 py-2 text-base font-medium text-gray-700 shadow-sm hover:text-gray-500 focus:outline-none focus:ring-2 focus:ring-indigo-500 focus:ring-offset-2 sm:mt-0 sm:w-auto sm:text-sm" @click="() => this.$router.push({ path: `/projects/${this.selectedProjectId}`, replace: true })">Ok</button>
                </div>
              </DialogPanel>
            </TransitionChild>
          </div>
        </div>
      </Dialog>
    </TransitionRoot>
  </main>
</template>

<!-- TODO https://tailwind-ui-two.vercel.app/components/application-ui/lists/tables#component-822ab4bf111e9a34063e651275b381e6 -->
<!-- <script setup>
  const people = [
    {
      name: 'Lindsay Walton',
      title: 'Front-end Developer',
      department: 'Optimization',
      email: 'lindsay.walton@example.com',
      role: 'Member',
      image:
        'https://images.unsplash.com/photo-1517841905240-472988babdf9?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=facearea&facepad=2&w=256&h=256&q=80',
    },
    // More people...
  ]
</script> -->

<!-- TODO https://tailwind-ui-two.vercel.app/components/application-ui/overlays/slide-overs#component-b76ed25b74c40b7f3a181393e2b7742f -->
<!-- <script setup>
  import { ref } from 'vue'
  import { Dialog, DialogPanel, DialogTitle, TransitionChild, TransitionRoot } from '@headlessui/vue'
  import { XMarkIcon } from '@heroicons/vue/24/outline'
  import { LinkIcon, PlusIcon, QuestionMarkCircleIcon } from '@heroicons/vue/20/solid'

  const team = [
    {
      name: 'Tom Cook',
      email: 'tom.cook@example.com',
      href: '#',
      imageUrl:
        'https://images.unsplash.com/photo-1472099645785-5658abf4ff4e?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=facearea&facepad=2&w=256&h=256&q=80',
    },
    {
      name: 'Whitney Francis',
      email: 'whitney.francis@example.com',
      href: '#',
      imageUrl:
        'https://images.unsplash.com/photo-1517365830460-955ce3ccd263?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=facearea&facepad=2&w=256&h=256&q=80',
    },
    {
      name: 'Leonard Krasner',
      email: 'leonard.krasner@example.com',
      href: '#',
      imageUrl:
        'https://images.unsplash.com/photo-1519345182560-3f2917c472ef?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=facearea&facepad=2&w=256&h=256&q=80',
    },
    {
      name: 'Floyd Miles',
      email: 'floyd.miles@example.com',
      href: '#',
      imageUrl:
        'https://images.unsplash.com/photo-1463453091185-61582044d556?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=facearea&facepad=2&w=256&h=256&q=80',
    },
    {
      name: 'Emily Selman',
      email: 'emily.selman@example.com',
      href: '#',
      imageUrl:
        'https://images.unsplash.com/photo-1502685104226-ee32379fefbe?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=facearea&facepad=2&w=256&h=256&q=80',
    },
  ]

  const open = ref(true)
</script> -->

<script>
import { Dialog, DialogPanel, DialogTitle, TransitionChild, TransitionRoot } from '@headlessui/vue'
import { XMarkIcon } from '@heroicons/vue/24/outline'
import { LinkIcon, PlusIcon, QuestionMarkCircleIcon, CheckIcon, ArrowPathIcon } from '@heroicons/vue/20/solid'
import { Switch, SwitchDescription, SwitchGroup, SwitchLabel } from '@headlessui/vue'
import { ExclamationTriangleIcon } from '@heroicons/vue/24/outline'
import AssetsView from './AssetsView.vue'
import StepsView from './StepsView.vue'
import { NJOGUSH_WEBSOCKET_URL, getBaseUrl } from '../network/network_info'

export default {
  components: {
    Dialog,
    DialogPanel,
    DialogTitle,
    TransitionChild,
    TransitionRoot,
    XMarkIcon,
    LinkIcon,
    PlusIcon,
    QuestionMarkCircleIcon,

    Switch,
    SwitchDescription,
    SwitchGroup,
    SwitchLabel,

    ExclamationTriangleIcon,
    CheckIcon,
    ArrowPathIcon,

    StepsView,
    AssetsView,

  },
  // Properties returned from data() become reactive state
  // and will be exposed on `this`.
  data() {
    return {
      count: 0,
      people: [
        {
          name: 'Lindsay Walton',
          title: 'Front-end Developer',
          department: 'Optimization',
          email: 'lindsay.walton@example.com',
          role: 'Member',
          image:
            'https://images.unsplash.com/photo-1517841905240-472988babdf9?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=facearea&facepad=2&w=256&h=256&q=80',
        },
        // More people...
      ],
      open: false,
      name: '',
      is_listed: true,
      is_available: true,
      openModal: false,
      openModalSocket: false,
      modalSocketMessage: '',
      action: null,
      chatSocket: null,
      step_progress: [],
      eventTypes: {
        applied: { icon: ArrowPathIcon, bgColorClass: 'bg-gray-400' },
        failure: { icon: XMarkIcon, bgColorClass: 'bg-red-500' },
        success: { icon: CheckIcon, bgColorClass: 'bg-green-500' },
      },
      is_running: false,
    }
  },
  computed: {
    selectedId() {
      return parseInt(this.$route.params.id);
    },
    buildSessions() {
      // `this` points to the component instance
      // return this.$store.state.buildSessions;
      return this.$store.getters.buildSessions;
    },
    currentBuildSession() {
      console.log(this.buildSessions.find(element => element.id === this.selectedId))
      return this.buildSessions.find(element => element.id === this.selectedId);
    },
    // <<<<>>>>>
    // PROJECT
    selectedProjectId() {
      return parseInt(this.$route.params.project_id);
    },
    projects() {
      // `this` points to the component instance
      // return this.$store.state.projects;
      return this.$store.getters.projects;
    },
    currentProject() {
      console.log(this.projects.find(element => element.id === this.selectedProjectId))
      return this.projects.find(element => element.id === this.selectedProjectId);
    },
    // ! <<<<>>>>>

    newOrEdit() {
      return this.selectedId ? 'Edit' : 'New';
    },
  },

  watch: {
    // whenever currentBuildSession changes, this function will run
    currentBuildSession(newValue, oldValue) {
      if(!this.currentProject) {
        this.$store.dispatch('getProject', {id: newValue.project});
      }
    }
  },

  // Methods are functions that mutate state and trigger updates.
  // They can be bound as event handlers in templates.
  methods: {
    openSideBar(id) {
      // this.selectedId = id;
      if(id) {
        this.setForm(this.currentProject)
      } else {
        this.setForm({})
      }
      this.open = true
    },
    closeSideBar(id) {
      this.open = false
    },
    setForm(item) {
      this.name = item.name;
      this.is_listed = item.is_listed ?? true;
      this.is_available = item.is_available ?? true;
    },
    async save() {
      const data = {
        name: this.name,
        is_listed: this.is_listed,
        is_available: this.is_available,
      }
      
      if(this.selectedId) {
        await this.$store.dispatch('updateProject', {id: this.selectedId, data: data});
      } else {
        await this.$store.dispatch('createProject', data);
        this.closeSideBar();
      }
    },
    async showModal(status) {
      this.action = status;
      this.openModal = true;
    },
    // WEBSOCKET
    async initSocket() {
      // const roomName = JSON.parse(document.getElementById('room-name').textContent);
      const roomName = `${this.selectedId}`;

      // OPTION 1 - infer host
      // when using 'npm run dev' the SPA will be served on port '5173'
      // which is not the location of the server (see OPTION 2 below)
      // this.chatSocket = new WebSocket(
      //     'ws://'
      //     + window.location.host
      //     + '/ws/build/'
      //     + roomName
      //     + '/'
      // );

      // OPTION 2
      // this.chatSocket = new WebSocket(
      //     'ws://'
      //     + getBaseUrl()
      //     + '/ws/build/'
      //     + roomName
      //     + '/'
      // );

      // OPTION 3 - infer protocol
      this.chatSocket = new WebSocket(
          NJOGUSH_WEBSOCKET_URL
          + '/ws/build/'
          + roomName
          + '/'
      );

      this.chatSocket.onmessage = function(e) {
          const data = JSON.parse(e.data);
          // document.querySelector('#chat-log').value += (data.message + '\n');
          if(data.signal) {
            if(data.signal == 'start') {
              this.is_running = true;
            } else if (data.signal == 'finish') {
              this.is_running = false;

              this.openModalSocket = true;
              this.modalSocketMessage = 'Project steps finished'
            } else if (data.signal == 'stop') {
              this.is_running = false;

              this.openModalSocket = true;
              this.modalSocketMessage = 'Project stopped'
            }
          }
          if(data.logs) {
            this.$refs.chat_log.value += data.logs;
          }
          if(data.report) {
            this.step_progress.push(data.report);
            console.log(this.step_progress)
          }
          
      }.bind(this);

      this.chatSocket.onclose = function(e) {
          // console.error('Chat socket closed unexpectedly');
          this.openModalSocket = true;
          this.modalSocketMessage = 'Chat socket closed unexpectedly'
      }.bind(this);

    },
    async run() {
      this.$refs.chat_log.value = '';

      if (this.chatSocket.readyState == 3) {
        await this.initSocket();
      }

      this.step_progress = [];

      this.chatSocket.send(JSON.stringify({
        'message': 'run'
      }));
    },
    async rerun() {
      this.$refs.chat_log.value = '';

      if (this.chatSocket.readyState == 3) {
        await this.initSocket();
      }

      this.step_progress = [];

      this.chatSocket.send(JSON.stringify({
        'message': 'rerun'
      }));
    },
    async stop() {
      if (this.chatSocket.readyState == 3) {
        await this.initSocket();
      }

      this.chatSocket.send(JSON.stringify({
        'message': 'stop'
      }));
    },
    getClass(item) {
      if(item.status.includes("success")){
        return this.eventTypes.success.bgColorClass
      }

      if(item.status.includes("failure")){
        return this.eventTypes.failure.bgColorClass
      }

      return this.eventTypes.applied.bgColorClass
    },
    getIcon(item) {
      if(item.status.includes("success")){
        return this.eventTypes.success.icon
      }

      if(item.status.includes("failure")){
        return this.eventTypes.failure.icon
      }

      return this.eventTypes.applied.icon
    }
  },

  // Lifecycle hooks are called at different stages
  // of a component's lifecycle.
  // This function will be called when the component is mounted.
  async mounted() {
    // console.log(`The initial count is ${this.count}.`)

    this.initSocket();
    if(!this.currentBuildSession) {
      this.$store.dispatch('getBuildSession', {id: this.selectedId});
    }
  }
}
</script>
