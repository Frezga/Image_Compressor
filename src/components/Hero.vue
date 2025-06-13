<template>
  <section id="home" class="hero">
    <ilustrasi />
    <div class="hero-container">
      <div class="welcome" data-aos="fade-in" data-aos-duration="600" data-aos-delay="1000">
        <AnimationIntro />
      </div>
      <div class="hero-content" data-aos="fade-down" data-aos-duration="900" data-aos-delay="1200">
        <h2 class="subtitle">Image Compressor</h2>
        <p class="description">
          Project ini bertujuan untuk mengompresi gambar sesuai dengan keinginan user. User bisa
          membaca panduan cara menjalankan fungsi ini dengan melihat
          <RouterLink to="/about-project" class="link">about project</RouterLink> terlebih dahulu
          atau cukup ikuti semua alur yang sudah disediakan. Selain itu, User juga bisa melihat
          developer pada <RouterLink to="/about-us" class="link">about us</RouterLink> di atas.
        </p>
        <p class="scroll-text">scroll down to continue</p>
      </div>
    </div>
  </section>
</template>

<script setup>
import { RouterLink } from 'vue-router'
import Ilustrasi from './Ilustrasi.vue'
import AnimationIntro from './AnimationIntro.vue'
</script>

<style scoped>
.hero {
  width: 100%;
  display: flex;
  padding-bottom: 20rem; /* kasih ruang buat transisi */
  background: transparent;
  justify-content: center;
  align-items: center;
  text-align: center;
  position: relative;
  z-index: 1;
}

.welcome {
  display: flex;
  padding-top: 0;
  flex-direction: row;
  align-items: center;
  margin-left: 24rem;
  text-align: center;
}
.hero-content {
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  text-align: center;
  z-index: 2;
  margin: auto;
}

.subtitle {
  font-size: 6rem;
  font-family: 'DM Sans', sans-serif;
  font-weight: bold;
  margin-top: 0rem;

  margin-bottom: 0rem;
  color: #fff;
}

.subtitle2 {
  font-size: 3rem;
  font-family: 'DM Sans', sans-serif;
  font-weight: bold;
  margin-top: -1.5rem;
  margin-bottom: 2rem;
  color: #fff;
}

.description {
  font-size: 1.3rem;
  text-align: left;
  padding-top: 0px;
  padding-left: 100px;
  color: #eaeaea;
  max-width: 80%;
  margin-bottom: 5rem;
  margin-top: 1rem;
  margin-left: 7rem;
  line-height: 1.6;
}

.link {
  color: #2bb6b6;
  text-decoration: underline;
  cursor: pointer;
}

.scroll-text {
  font-size: 1rem;
  color: #aaa;
  margin-top: 2rem;
  animation: bounce 1s infinite alternate;
}

@keyframes bounce {
  0% {
    transform: translateY(0);
  }
  100% {
    transform: translateY(10px);
  }
}

@keyframes slideInLeft {
  0% {
    opacity: 0;
    transform: translateX(-200px);
  }
  100% {
    opacity: 1;
    transform: translateX(0);
  }
}

@keyframes bounce {
  0% {
    transform: translateY(0);
  }
  100% {
    transform: translateY(10px);
  }
}
</style>
