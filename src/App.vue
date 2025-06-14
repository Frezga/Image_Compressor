<script setup>
import Navbar from '@/components/Navbar.vue'
import { RouterView } from 'vue-router'
import AOS from 'aos'
import 'aos/dist/aos.css'
AOS.init()
</script>

<template>
  <Navbar />
  <RouterView />
</template>

<style>
#app {
  font-family:
    DM Sans,
    sans-serif;
  font-weight: 300;
  font-style: normal;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
}

body,
html {
  margin: 0;
  font-family:
    sans-serif,
    DM Sans;
}
</style>

<script>
import AOS from 'aos'

export default {
  mounted() {
    AOS.refresh() // atau AOS.init() jika pertama kali
  },
  activated() {
    AOS.refresh()
  },
}
</script>
