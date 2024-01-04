import { createRouter, createWebHistory } from 'vue-router'
import HomeView from '../views/HomeView.vue'
import DashboardView from '../views/DashboardView.vue'

import ProjectsView from '../views/ProjectsView.vue'
import ProjectItemView from '../views/ProjectItemView.vue'
import BuildSessionItemView from '../views/BuildSessionItemView.vue'
import NotFound from '../views/NotFound.vue'

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/',
      name: 'dashboard',
      // component: HomeView
      component: DashboardView
    },
    {
      path: '/about',
      name: 'about',
      // route level code-splitting
      // this generates a separate chunk (About.[hash].js) for this route
      // which is lazy-loaded when the route is visited.
      component: () => import('../views/AboutView.vue')
    },

    {
      path: '/projects',
      name: 'projects',
      component: ProjectsView
    },
    // dynamic segments start with a colon
    { 
      path: '/projects/:id',
      component: ProjectItemView
    },
    { 
      path: '/projects/:project_id/build/:id',
      component: BuildSessionItemView
    },
    // will match everything and put it under `$route.params.pathMatch`
    { path: '/:pathMatch(.*)*', name: 'NotFound', component: NotFound },
  ]
})

export default router
