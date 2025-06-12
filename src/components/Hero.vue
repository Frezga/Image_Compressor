<template>
  <section id="hero" class="hero">
    <div class="hero-container">
      <div class="hero-content">
        <h1 class="main-title">
          <span class="highlight">Welcome</span>
        </h1>
        <h2 class="subtitle">to</h2>
        <h3 class="subtitle2">Image Compressor</h3>
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
</script>

<style scoped>
.hero {
  width: 100%;
  height: 100vh;
  background-image: url('@/assets/abstract.png');
  background-repeat: no-repeat;
  background-position: left 3px top 10px;
  background-size: 1024px auto;
  display: flex;
  justify-content: center;
  align-items: center;
  text-align: center;
  position: relative;
  z-index: 1;
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

.main-title {
  font-size: 5rem;
  font-family: 'DM Sans', sans-serif;
  font-weight: 800;

  margin-top: 14rem;
  margin-bottom: 0;
}

.highlight {
  background: rgba(164, 232, 232, 0.25);
  border-radius: 35px;
  padding: 10px 20px;
  color: #fff;
  backdrop-filter: blur(2.2px);
  border: 1px solid rgba(204, 216, 216, 0.56);
}

.subtitle {
  font-size: 3rem;
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
  font-size: 1.5rem;
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
