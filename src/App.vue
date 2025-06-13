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
  background: linear-gradient(
    138deg,
    #021420 19%,
    #052f3a 43%,
    #042a49 59%,
    #0b3d5f 86%,
    #176b87 99%,
    #229799 99%,
    #021420 100%
  );
}
</style>
