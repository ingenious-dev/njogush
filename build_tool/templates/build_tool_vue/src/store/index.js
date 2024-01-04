// import { createApp } from 'vue'
import { createStore } from 'vuex'

// Create a new store instance.
// const store = createStore({
//   state () {
//     return {
//       count: 0
//     }
//   },
//   mutations: {
//     increment (state) {
//       state.count++
//     }
//   }
// })

// const app = createApp({ /* your root component */ })

// Install the store instance as a plugin
// app.use(store)

import projects from './projects';
import assets from './assets';
import steps from './steps';
import buildSessions from './buildSessions';
import alert from './alert';

const store = createStore({
    modules: {
        // a: moduleA,
        // b: moduleB,
        projects: projects,
        assets: assets,
        steps: steps,
        buildSessions: buildSessions,
        alert: alert,
    }
})

export default store