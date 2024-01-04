<template>
  <div>
    <!-- Comments-->
    <section aria-labelledby="notes-title">
      <div class="bg-white shadow sm:overflow-hidden sm:rounded-lg">
        <div class="divide-y divide-gray-200">
          <div class="px-4 py-5 sm:px-6 flex">
            <div class="flex-auto">
              <h2 id="notes-title" class="text-lg font-medium text-gray-900">Steps</h2>
            </div>
            <button
              type="button"
              class="inline-flex items-center justify-center rounded-md border border-transparent bg-indigo-600 px-4 py-2 text-sm font-medium text-white shadow-sm hover:bg-indigo-700 focus:outline-none focus:ring-2 focus:ring-indigo-500 focus:ring-offset-2 sm:w-auto"
              @click="openSideBar()">Add</button>
          </div>
          <div class="px-4 py-6 sm:px-6">
            <ul role="list" class="space-y-8">
              <li v-for="item in steps" :key="item.id">
                <a href="#" class="block hover:bg-gray-50" @click="openSideBar(item.id)">
                  <div class="px-4 py-4 sm:px-6">
                    <div class="flex items-center justify-between">
                      <p class="truncate text-sm font-medium text-indigo-600">{{ item.name }}</p>
                      <div class="ml-2 flex flex-shrink-0">
                        <!-- <p class="inline-flex rounded-full bg-green-100 px-2 text-xs font-semibold leading-5 text-green-800">Full-time</p> -->
                      </div>
                    </div>
                    <div class="mt-2 sm:flex sm:justify-between">
                      <div class="sm:flex">
                        <p class="mt-2 flex items-center text-sm text-gray-500 sm:mt-0">
                          <TagIcon class="mr-1.5 h-5 w-5 flex-shrink-0 text-gray-400" aria-hidden="true" />
                          {{ item.category.toUpperCase() }}
                        </p>
                      </div>
                      <div class="mt-2 flex items-center text-sm text-gray-500 sm:mt-0">
                        <!-- Heroicon name: mini/calendar -->
                        <svg class="mr-1.5 h-5 w-5 flex-shrink-0 text-gray-400" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 20 20" fill="currentColor" aria-hidden="true">
                          <path fill-rule="evenodd" d="M5.75 2a.75.75 0 01.75.75V4h7V2.75a.75.75 0 011.5 0V4h.25A2.75 2.75 0 0118 6.75v8.5A2.75 2.75 0 0115.25 18H4.75A2.75 2.75 0 012 15.25v-8.5A2.75 2.75 0 014.75 4H5V2.75A.75.75 0 015.75 2zm-1 5.5c-.69 0-1.25.56-1.25 1.25v6.5c0 .69.56 1.25 1.25 1.25h10.5c.69 0 1.25-.56 1.25-1.25v-6.5c0-.69-.56-1.25-1.25-1.25H4.75z" clip-rule="evenodd" />
                        </svg>
                        <p>
                          <!-- Closing on -->
                          <time datetime="2020-01-07">{{ $moment(item.date_posted).format("MMMM Do YYYY, h:mm:ss a") }}</time>
                        </p>
                      </div>
                    </div>
                  </div>
                </a>
              </li>
            </ul>
          </div>
        </div>
      </div>
    </section>
    
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
                          <DialogTitle class="text-lg font-medium text-white">{{ newOrEdit }} Step</DialogTitle>
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
                              <label for="project-name" class="block text-sm font-medium text-gray-900">Step name</label>
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
                                <textarea id="description" name="description" rows="4" class="block w-full rounded-md border-gray-300 shadow-sm focus:border-indigo-500 focus:ring-indigo-500 sm:text-sm" v-model="description" />
                              </div>
                            </div>
                            <div>
                              <label for="project-rank" class="block text-sm font-medium text-gray-900">Rank</label>
                              <div class="mt-1">
                                <input
                                type="number"
                                name="project-rank"
                                id="project-rank"
                                class="block w-full rounded-md border-gray-300 shadow-sm focus:border-indigo-500 focus:ring-indigo-500 sm:text-sm"
                                v-model="rank" />
                              </div>
                            </div>

                            <div>
                              <label for="category" class="block text-sm font-medium text-gray-700">Category</label>
                              <div class="mt-1">
                                <select id="category" name="category" autocomplete="category-name" class="block w-full rounded-md border-gray-300 shadow-sm focus:border-indigo-500 focus:ring-indigo-500 sm:text-sm" v-model="category">
                                  <option value="folder">Folder</option>
                                  <option value="file">File</option>
                                  <option value="excerpt">Excerpt</option>
                                  <option value="command">Command</option>
                                </select>
                              </div>
                            </div>
                            <div v-if="category === 'folder'">
                              <div>
                                <label for="project-folder" class="block text-sm font-medium text-gray-900">Folder</label>
                                <div class="mt-1">
                                  <input
                                  type="text"
                                  name="project-folder"
                                  id="project-folder"
                                  class="block w-full rounded-md border-gray-300 shadow-sm focus:border-indigo-500 focus:ring-indigo-500 sm:text-sm"
                                  v-model="folder" />
                                </div>
                              </div>
                            </div>
                            <div v-if="category === 'file'">
                              <div>
                                <label for="project-file_path" class="block text-sm font-medium text-gray-900">File Path</label>
                                <div class="mt-1">
                                  <input
                                  type="text"
                                  name="project-file_path"
                                  id="project-file_path"
                                  class="block w-full rounded-md border-gray-300 shadow-sm focus:border-indigo-500 focus:ring-indigo-500 sm:text-sm"
                                  v-model="file_path" />
                                </div>
                              </div>
                              <div>
                                  <label for="asset" class="block text-sm font-medium text-gray-700">Asset</label>
                                  <div class="mt-1">
                                    <select id="asset" name="asset" autocomplete="asset-name" class="block w-full rounded-md border-gray-300 shadow-sm focus:border-indigo-500 focus:ring-indigo-500 sm:text-sm" v-model="asset">
                                      <option v-for="item in assets" :key="item.id" :value="item.id">{{ item.name }}</option>
                                    </select>
                                  </div>
                                </div>
                            </div>
                            <div v-if="category === 'excerpt'">
                              <div>
                                <label for="project-file_path" class="block text-sm font-medium text-gray-900">File Path</label>
                                <div class="mt-1">
                                  <input
                                  type="text"
                                  name="project-file_path"
                                  id="project-file_path"
                                  class="block w-full rounded-md border-gray-300 shadow-sm focus:border-indigo-500 focus:ring-indigo-500 sm:text-sm"
                                  v-model="file_path" />
                                </div>
                              </div>
                              <div>
                                <label for="excerpt" class="block text-sm font-medium text-gray-900">Excerpt</label>
                                <div class="mt-1">
                                  <textarea id="excerpt" name="excerpt" rows="4" class="block w-full rounded-md border-gray-300 shadow-sm focus:border-indigo-500 focus:ring-indigo-500 sm:text-sm" v-model="excerpt" />
                                </div>
                              </div>
                              <div>
                                <label for="project-excerpt_start" class="block text-sm font-medium text-gray-900">Start Marker</label>
                                <div class="mt-1">
                                  <input
                                  type="text"
                                  name="project-excerpt_start"
                                  id="project-excerpt_start"
                                  class="block w-full rounded-md border-gray-300 shadow-sm focus:border-indigo-500 focus:ring-indigo-500 sm:text-sm"
                                  v-model="excerpt_start" />
                                </div>
                              </div>
                              <div>
                                <label for="project-excerpt_end" class="block text-sm font-medium text-gray-900">End Marker</label>
                                <div class="mt-1">
                                  <input
                                  type="text"
                                  name="project-excerpt_end"
                                  id="project-excerpt_end"
                                  class="block w-full rounded-md border-gray-300 shadow-sm focus:border-indigo-500 focus:ring-indigo-500 sm:text-sm"
                                  v-model="excerpt_end" />
                                </div>
                              </div>
                            </div>
                            <div v-if="category === 'command'">
                              <div>
                                <label for="command" class="block text-sm font-medium text-gray-900">command</label>
                                <div class="mt-1">
                                  <textarea id="command" name="command" rows="4" class="block w-full rounded-md border-gray-300 shadow-sm focus:border-indigo-500 focus:ring-indigo-500 sm:text-sm" v-model="command" />
                                </div>
                              </div>
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
                          @click="checkForm()">Save</button>
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
                    <DialogTitle as="h3" class="text-lg font-medium leading-6 text-gray-900">Delete step</DialogTitle>
                    <div class="mt-2">
                      <p class="text-sm text-gray-500">Are you sure you want to delete the step? All of your data will be permanently removed from our servers forever. This action cannot be undone.</p>
                    </div>
                  </div>
                </div>
                <div class="mt-5 sm:mt-4 sm:flex sm:flex-row-reverse">
                  <button type="button" class="inline-flex w-full justify-center rounded-md border border-transparent bg-red-600 px-4 py-2 text-base font-medium text-white shadow-sm hover:bg-red-700 focus:outline-none focus:ring-2 focus:ring-red-500 focus:ring-offset-2 sm:ml-3 sm:w-auto sm:text-sm" @click="deleteStep()">Delete</button>
                  <button type="button" class="mt-3 inline-flex w-full justify-center rounded-md border border-gray-300 bg-white px-4 py-2 text-base font-medium text-gray-700 shadow-sm hover:text-gray-500 focus:outline-none focus:ring-2 focus:ring-indigo-500 focus:ring-offset-2 sm:mt-0 sm:w-auto sm:text-sm" @click="openModal = false">Cancel</button>
                </div>
              </DialogPanel>
            </TransitionChild>
          </div>
        </div>
      </Dialog>
    </TransitionRoot>

    <TransitionRoot as="template" :show="openModalError">
      <Dialog as="div" class="relative z-10" @close="openModalError = false">
        <TransitionChild as="template" enter="ease-out duration-300" enter-from="opacity-0" enter-to="opacity-100" leave="ease-in duration-200" leave-from="opacity-100" leave-to="opacity-0">
          <div class="fixed inset-0 bg-gray-500 bg-opacity-75 transition-opacity" />
        </TransitionChild>

        <div class="fixed inset-0 z-10 overflow-y-auto">
          <div class="flex min-h-full items-end justify-center p-4 text-center sm:items-center sm:p-0">
            <TransitionChild as="template" enter="ease-out duration-300" enter-from="opacity-0 translate-y-4 sm:translate-y-0 sm:scale-95" enter-to="opacity-100 translate-y-0 sm:scale-100" leave="ease-in duration-200" leave-from="opacity-100 translate-y-0 sm:scale-100" leave-to="opacity-0 translate-y-4 sm:translate-y-0 sm:scale-95">
              <DialogPanel class="relative transform overflow-hidden rounded-lg bg-white px-4 pt-5 pb-4 text-left shadow-xl transition-all sm:my-8 sm:w-full sm:max-w-lg sm:p-6">
                <div class="absolute top-0 right-0 hidden pt-4 pr-4 sm:block">
                  <button type="button" class="rounded-md bg-white text-gray-400 hover:text-gray-500 focus:outline-none focus:ring-2 focus:ring-indigo-500 focus:ring-offset-2" @click="openModalError = false">
                    <span class="sr-only">Close</span>
                    <XMarkIcon class="h-6 w-6" aria-hidden="true" />
                  </button>
                </div>
                <div class="sm:flex sm:items-start">
                  <div class="mx-auto flex h-12 w-12 flex-shrink-0 items-center justify-center rounded-full bg-red-100 sm:mx-0 sm:h-10 sm:w-10">
                    <ExclamationTriangleIcon class="h-6 w-6 text-red-600" aria-hidden="true" />
                  </div>
                  <div class="mt-3 text-center sm:mt-0 sm:ml-4 sm:text-left">
                    <DialogTitle as="h3" class="text-lg font-medium leading-6 text-gray-900">Error</DialogTitle>
                    <div class="mt-2">
                      <!-- <p class="text-sm text-gray-500">{{ modalErrorMessage }}</p> -->

                      <p v-if="errors.length">
                        <b>Please correct the following error(s):</b>
                        <ul>
                          <li v-for="error in errors" :key="error">{{ error }}</li>
                        </ul>
                      </p>
                    </div>
                  </div>
                </div>
                <div class="mt-5 sm:mt-4 sm:flex sm:flex-row-reverse">
                  <!-- <button type="button" class="inline-flex w-full justify-center rounded-md border border-transparent bg-red-600 px-4 py-2 text-base font-medium text-white shadow-sm hover:bg-red-700 focus:outline-none focus:ring-2 focus:ring-red-500 focus:ring-offset-2 sm:ml-3 sm:w-auto sm:text-sm" @click="setStatus()">Try Again</button> -->
                  <button type="button" class="mt-3 inline-flex w-full justify-center rounded-md border border-gray-300 bg-white px-4 py-2 text-base font-medium text-gray-700 shadow-sm hover:text-gray-500 focus:outline-none focus:ring-2 focus:ring-indigo-500 focus:ring-offset-2 sm:mt-0 sm:w-auto sm:text-sm" @click="openModalError = false">Ok</button>
                </div>
              </DialogPanel>
            </TransitionChild>
          </div>
        </div>
      </Dialog>
    </TransitionRoot>
  </div>
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
import { LinkIcon, PlusIcon, QuestionMarkCircleIcon } from '@heroicons/vue/20/solid'
import { Switch, SwitchDescription, SwitchGroup, SwitchLabel } from '@headlessui/vue'
import { ExclamationTriangleIcon, TagIcon } from '@heroicons/vue/24/outline'

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
    TagIcon
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
      errors: [],
      name: '',
      description: '',
      rank: 0,
      category: '',
      folder: '',
      file_path: '',
      asset: '',
      excerpt: '',
      excerpt_start: '',
      excerpt_end: '',
      command: '',
      openModal: false,
      openModalError: false,
      modalErrorMessage: '',
      selectedId: null,
    }
  },
  computed: {
    projectId() {
      return this.$route.params.id;
    },
    steps() {
      // `this` points to the component instance
      // return this.$store.state.steps;
      return this.$store.getters.steps;
    },
    currentStep() {
      return this.steps.find(element => element.id === this.selectedId);
    },
    newOrEdit() {
      return this.selectedId ? 'Edit' : 'New';
    },

    assets() {
      // `this` points to the component instance
      // return this.$store.state.assets;
      return this.$store.getters.assets;
    },
  },

  // Methods are functions that mutate state and trigger updates.
  // They can be bound as event handlers in templates.
  methods: {
    openSideBar(id) {
      this.selectedId = id;
      if(id) {
        this.setForm(this.currentStep)
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
      this.description = item.description;
      this.rank = item.rank ?? 0;
      this.category = item.category;
      this.folder = item.folder;
      this.file_path = item.file_path;
      this.asset = item.asset;
      this.excerpt = item.excerpt;
      this.excerpt_start = item.excerpt_start;
      this.excerpt_end = item.excerpt_end;
      this.command = item.command;
    },
    async save() {
      const data = {
        project: this.projectId,
        name: this.name,
        description: this.description,
        rank: this.rank,
        category: this.category,
        folder: this.folder,
        file_path: this.file_path,
        asset: this.asset,
        excerpt: this.excerpt,
        excerpt_start: this.excerpt_start,
        excerpt_end: this.excerpt_end,
        command: this.command,
      }
      
      if(this.selectedId) {
        await this.$store.dispatch('updateStep', {id: this.selectedId, data: data});
      } else {
        await this.$store.dispatch('createStep', data);
        this.closeSideBar();
        this.setForm({})
      }
    },
    async deleteStep() {
      await this.$store.dispatch('deleteStep', {id: this.selectedId});
      this.openModal = false;
    },
    // TODO https://v2.vuejs.org/v2/cookbook/form-validation#Base-Example
    checkForm (e) {
      this.errors = [];

      if (!this.name) {
        this.errors.push('Name required.');
      }

      if (this.rank == null) {
        this.errors.push('Rank required.');
      }

      switch (this.category) {
        case 'folder':
          if (!this.folder) {
            this.errors.push('Folder required.');
          }
          break;
        
        case 'file':
          if (!this.file_path) {
            this.errors.push('File path required.');
          }
          if (!this.asset) {
            this.errors.push('Asset required.');
          }
          break;

        case 'excerpt':
          if (!this.excerpt) {
            this.errors.push('Excerpt required.');
          }
          if (!this.excerpt_start) {
            this.errors.push('Start marker required.');
          }
          if (!this.excerpt_end) {
            this.errors.push('End marker required.');
          }
          break;

        case 'command':
          if (!this.command) {
            this.errors.push('Command required.');
          }
          break;
      
        default:
          break;
      }

      if(this.errors.length == 0) {
        this.save()
        return true;
      }

      // e.preventDefault();

      this.openModalError = true;
      // this.modalErrorMessage = 'Chat socket closed unexpectedly'
    },
    // https://masteringjs.io/tutorials/vue/file-upload
    uploadFile() {
      this.file = this.$refs.file.files[0];
    }
  },

  // Lifecycle hooks are called at different stages
  // of a component's lifecycle.
  // This function will be called when the component is mounted.
  mounted() {
    // console.log(`The initial count is ${this.count}.`)
    this.$store.dispatch('fetchSteps', {project: this.projectId});
  }
}
</script>
