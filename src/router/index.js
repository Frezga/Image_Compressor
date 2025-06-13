import { createRouter, createWebHistory } from 'vue-router'
import HomeView from '../views/HomeView.vue'
import Result from '../views/Result.vue'
import AboutProject from '../views/AboutProject.vue'
import AboutUs from '../views/AboutUs.vue'

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/',
      name: 'home',
      component: HomeView,
    },
    {
      path: '/result',
      name: 'result',
      component: Result,
    },
    {
      path: '/about-project',
      name: 'aboutProject',
      component: AboutProject,
    },
    {
      path: '/about-us',
      name: 'aboutUs',
      component: AboutUs,
    },
  ],
})

export default router
