<template>
  <div id="home" class="hero"></div>
  <Ilustrasi />
  <div class="hero-section">
    <div class="hero-content-container">
      <div
        class="welcome"
        data-aos="fade-up"
        data-aos-duration="1200"
        data-aos-delay="1000"
        data-aos-once="true"
      >
        <AnimationIntro />
        <div class="subtitle">Image Compressor</div>
      </div>
    </div>
  </div>
</template>

<script setup>
import Ilustrasi from './Ilustrasi.vue'
import AnimationIntro from './AnimationIntro.vue'
</script>

<style scoped>
.hero-section {
  position: relative;
  width: 100vw;
  height: 100vh;
}

.hero-content-container {
  position: absolute;
  padding-left: 10rem;
  top: 40%;
  left: 50%;
  transform: translate(-50%, -60%);
  display: flex;
  flex-direction: column;
  align-items: flex-start;
  z-index: 2;
}

.welcome {
  display: flex;
  flex-direction: column;
  align-items: flex-start;
  text-align: left;
}

.subtitle {
  font-size: 7rem;
  font-family: 'DM Sans', sans-serif;
  font-weight: bold;
  margin-top: 0rem;
  margin-bottom: 0rem;
  color: #fff;
  text-align: left;
  white-space: nowrap; /* agar tidak pindah baris */
}
</style>
