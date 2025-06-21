import { createRouter, createWebHistory } from 'vue-router'
import HomeView from '../views/HomeView.vue'
import Result from '../views/Result.vue'
import AboutProject from '../views/AboutProject.vue'
import AboutUs from '../views/AboutUs.vue'
import NotFound from '@/views/NotFound.vue'

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
      props: (route) => ({
        original_filename: route.query.original_filename,
        compressed_filename: route.query.compressed_filename,
        original_size: route.query.original_size,
        compressed_size: route.query.compressed_size,
        execution_time: route.query.execution_time,
        image_different_percentage: route.query.image_different_percentage,
      }),
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
    {
      path: '/:pathMatch(.*)*',
      name: 'NotFound',
      component: NotFound,
    },
  ],
})

export default router
