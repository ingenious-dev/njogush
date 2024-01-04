<!-- <script setup>
import TheWelcome from '../components/TheWelcome.vue'
const stats = [
  { name: 'Total Subscribers', stat: '71,897' },
  { name: 'Avg. Open Rate', stat: '58.16%' },
  { name: 'Avg. Click Rate', stat: '24.57%' },
]
</script> -->

<script>
import { fetchDashboard } from '../services/dashboard';

export default {
  components: {

  },
  // Properties returned from data() become reactive state
  // and will be exposed on `this`.
  data() {
    return {
      stats: [
        // { name: 'Total Subscribers', stat: '71,897' },
        // { name: 'Avg. Open Rate', stat: '58.16%' },
        // { name: 'Avg. Click Rate', stat: '24.57%' },
      ],
      buildSessions: []
    }
  },
  // Methods are functions that mutate state and trigger updates.
  // They can be bound as event handlers in templates.
  methods: {
    navigate(project, build) {
      // object with path
      this.$router.push({ path: `/projects/${project}/build/${build}` })
    }
  },
  // Lifecycle hooks are called at different stages
  // of a component's lifecycle.
  // This function will be called when the component is mounted.
  mounted() {
    // console.log(`The initial count is ${this.count}.`)
    fetchDashboard()
      .then(function (data) {
        // handle success
        this.stats = [
          { name: 'Projects', stat: data['projects_count'] },
          { name: 'Assets', stat: data['assets_count'] },
          { name: 'Build Sessions', stat: data['build_sessions_count'] },
        ]
        this.buildSessions = data['last_build_sessions']
      }.bind(this))
      .catch(function (error) {
        // handle error
        console.log(error);
      })
      .finally(function () {
        // always executed
      });
  }
}
</script>

<template>
  <main>
    <div class="py-6">
      <div class="mx-auto max-w-7xl px-4 sm:px-6 md:px-8">
        <h1 class="text-2xl font-semibold text-gray-900">Dashboard</h1>
      </div>
      <div class="mx-auto max-w-7xl px-4 sm:px-6 md:px-8">
        <!-- Replace with your content -->
        <!-- <div class="py-4">
          <div class="h-96 rounded-lg border-4 border-dashed border-gray-200" />
        </div> -->
        <!-- /End replace -->
        <div>
          <!-- <h3 class="text-lg font-medium leading-6 text-gray-900">Last 30 days</h3> -->
          <dl class="mt-5 grid grid-cols-1 gap-5 sm:grid-cols-3">
            <div v-for="item in stats" :key="item.name" class="overflow-hidden rounded-lg bg-white px-4 py-5 shadow sm:p-6">
              <dt class="truncate text-sm font-medium text-gray-500">{{ item.name }}</dt>
              <dd class="mt-1 text-3xl font-semibold tracking-tight text-gray-900">{{ item.stat }}</dd>
            </div>
          </dl>
        </div>
      </div>

      <div class="mx-auto max-w-7xl px-4 sm:px-6 md:px-8 mt-5">
        <h3 class="text-lg font-medium leading-6 text-gray-900">Your recent builds</h3>
        <div class="overflow-hidden shadow ring-1 ring-black ring-opacity-5 md:rounded-lg mt-5">
          <table class="min-w-full divide-y divide-gray-300">
            <thead class="bg-gray-50">
              <tr>
                <th scope="col" class="whitespace-nowrap py-3.5 pl-4 pr-3 text-left text-sm font-semibold text-gray-900 sm:pl-6">Build ID</th>
                <th scope="col" class="whitespace-nowrap px-2 py-3.5 text-left text-sm font-semibold text-gray-900">Date</th>
              </tr>
            </thead>
            <tbody class="divide-y divide-gray-200 bg-white">
              <tr v-for="item in buildSessions" :key="item.id">
                <td class="whitespace-nowrap py-2 pl-4 pr-3 text-sm text-gray-500 sm:pl-6" @click=" navigate(item.project, item.id) ">{{ item.id }}</td>
                <td class="whitespace-nowrap px-2 py-2 text-sm font-medium text-gray-900" @click=" navigate(item.project, item.id) ">{{ $moment(item.date_posted).format() }}</td>
              </tr>
            </tbody>
          </table>
        </div>
      </div>

    </div>
  </main>
</template>
