<template>
  <section class="result-section">
    <div class="result-illustration">
      <Ilustrasi />
    </div>
    <div class="result-glass-box" data-aos="fade-up" data-aos-duration="1000" data-aos-delay="1000">
      <div class="result-row">
        <!-- Before -->
        <div class="result-col">
          <div class="result-title">Before</div>
          <div class="result-image-box">
            <img src="@/assets/picture_logo.svg" alt="before" class="result-img" />
          </div>
          <div class="result-info-area">
            <div class="result-info">
              <div>Image different percentage:</div>
              <div>Image compression time:</div>
            </div>
            <button class="result-download-btn">Download</button>
          </div>
        </div>
        <!-- After -->
        <div class="result-col">
          <div class="result-title">After</div>
          <div class="result-image-box">
            <img src="@/assets/picture_logo.svg" alt="after" class="result-img" />
          </div>
        </div>
      </div>
      <router-link to="/" class="back-home-btn">Back to homepage &gt;&gt;&gt;</router-link>
    </div>
  </section>
</template>

<script setup>
import Ilustrasi from '@/components/Ilustrasi.vue'
</script>

<style scoped>
.result-section {
  height: 80vh;
  width: 100vw;
  position: relative;
  display: flex;
  align-items: center;
  justify-content: center;
  background: transparent;
  overflow-x: clip;
}

.result-illustration {
  position: absolute;
  left: 0;
  top: 45%;
  transform: translateY(-60%);
  z-index: 1;
  width: 45vw;
  max-width: 45vw;
  height: 80vh;
  max-height: 80vh;
  pointer-events: none;
  box-sizing: border-box;
  display: block;
}

.result-glass-box {
  max-width: 1100px;
  width: 95vw;
  min-height: 450px;
  padding: 48px 50px;
  padding-top: 25px;
  background: rgba(12, 79, 121, 0.115);
  border-radius: 28px;
  box-shadow:
    0 8px 40px 0 rgba(30, 233, 182, 0.13),
    0 0 32px 4px rgba(95, 110, 228, 0.1);
  backdrop-filter: blur(25px);
  border: 2px solid rgba(255, 255, 255, 0.18);
  color: #f3f6fa;
  font-family: 'DM Sans', sans-serif;
  position: relative;
  z-index: 2;
  text-align: left;
  filter: drop-shadow(0 0 16px #b0cbdd76);
  box-sizing: border-box;
  margin: 0;
  display: flex;
  flex-direction: column;
  justify-content: space-between;
}

.result-row {
  display: flex;
  flex-direction: row;
  justify-content: center;
  gap: 35px;
  width: 100%;
}

.result-col {
  flex: 1;
  display: flex;
  flex-direction: column;
  align-items: flex-start;
  min-width: 280px;
  max-width: 440px;
  position: relative;
}

.result-title {
  color: #fff;
  font-size: 1.5rem;
  font-weight: bold;
  margin-bottom: 0.6rem;
  margin-left: 0.3rem;
}

.result-image-box {
  width: 100%;
  min-width: 120px;
  max-width: 100%;
  min-height: 280px;
  max-height: 280px;
  border: 2px dashed #fff;
  border-radius: 10px;
  display: flex;
  align-items: center;
  justify-content: center;
  background: transparent;
  margin-bottom: 0;
}

.result-img {
  width: 48px;
  opacity: 0.7;
}

.result-info-area {
  margin-top: 1.2rem;
  display: flex;
  flex-direction: column;
  align-items: flex-start;
  gap: 8px;
  width: 100%;
  padding-left: 0.3rem;
}

.result-info {
  color: #d2f6f6;
  font-size: 1rem;
  display: flex;
  font-weight: bold;
  flex-direction: column;
  gap: 5px;
  text-align: left;
}

.result-download-btn {
  margin-top: 1px;
  padding: 8px 18px;
  border-radius: 16px;
  border: 2px solid #1de9b6;
  background: transparent;
  color: #fff;
  font-weight: bold;
  font-size: 0.95rem;
  cursor: pointer;
  transition:
    background 0.2s,
    color 0.2s;
}

.result-download-btn:hover {
  background: #1de9b6;
  color: #003344;
}

.back-home-btn {
  position: absolute;
  right: 18px;
  bottom: 18px;
  font-weight: bold;
  padding: 8px 18px;
  border-radius: 16px;
  border: 2px solid #00e6e694;
  background: transparent;
  color: #fff;
  font-size: 0.95rem;
  cursor: pointer;
  transition:
    background 0.5s,
    color 0.5s;
  text-decoration: none;
  display: inline-block;
}

.back-home-btn:hover {
  background: #00e6e60b;
  color: #1ee9b6;
}

:global(html),
:global(body) {
  margin: 0;
  padding: 0;
  overflow-x: clip;
}
</style>
