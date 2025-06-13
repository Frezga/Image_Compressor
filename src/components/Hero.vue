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
    <!-- Tombol scroll ke compressor -->
    <button
      class="scroll-btn"
      data-aos="fade-down"
      data-aos-delay="1000"
      @click="scrollToCompressor"
      aria-label="Scroll to compressor"
    >
      <svg width="54" height="54" viewBox="0 0 54 54" fill="none">
        <circle
          cx="27"
          cy="27"
          r="25"
          stroke="#fff"
          stroke-width="2"
          fill="rgba(255,255,255,0.08)"
        />
        <path
          d="M18 25L27 34L36 25"
          stroke="#fff"
          stroke-width="2.5"
          stroke-linecap="round"
          stroke-linejoin="round"
        />
      </svg>
    </button>
  </div>
</template>

<script setup>
import Ilustrasi from './Ilustrasi.vue'
import AnimationIntro from './AnimationIntro.vue'

function scrollToCompressor() {
  const el = document.querySelector('.compressor-section')
  if (el) {
    el.scrollIntoView({ behavior: 'smooth', block: 'start' })
  }
}
</script>

<style scoped>
.hero-section {
  min-height: 100vh;
  height: 100vh;
  width: 100vw;
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
}

.welcome {
  display: flex;
  flex-direction: column;
  align-items: flex-start;
  pointer-events: none;
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

.scroll-btn {
  position: absolute;
  left: 50%;
  bottom: 40px;
  transform: translateX(-50%);
  background: rgba(30, 233, 182, 0.1);
  border: none;
  border-radius: 50%;
  padding: 1.1rem;
  cursor: pointer;
  box-shadow: 0 2px 16px 0 rgba(30, 233, 182, 0.1);
  transition:
    background 0.2s,
    box-shadow 0.2s,
    transform 0.2s;
  z-index: 20;
  display: flex;
  align-items: center;
  justify-content: center;
  animation: scroll-bounce 1.9s infinite;
}

@keyframes scroll-bounce {
  0%,
  100% {
    transform: translateX(-50%) translateY(0);
  }
  50% {
    transform: translateX(-50%) translateY(18px);
  }
}

.scroll-btn:hover {
  background: rgba(95, 110, 228, 0.18);
  box-shadow: 0 4px 24px 0 rgba(95, 110, 228, 0.18);
}

.scroll-btn svg {
  display: block;
}
</style>
