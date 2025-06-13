<template>
  <section class="result-section">
    <div class="result-illustration">
      <Ilustrasi />
    </div>
    <div class="result-content">
      <div class="container">
        <div
          class="result-row"
          data-aos="fade-up"
          data-aos-duration="1000"
          data-aos-delay="1200"
          data-aos-once="true"
        >
          <div class="result-col">
            <div class="result-title">Before</div>
            <div class="result-image-box">
              <img src="@/assets/picture_logo.svg" alt="before" class="result-img" />
            </div>
          </div>
          <div class="result-col">
            <div class="result-title">After</div>
            <div class="result-image-box">
              <img src="@/assets/picture_logo.svg" alt="after" class="result-img" />
            </div>
          </div>
        </div>
        <div class="result-info-row">
          <div class="result-info">
            <div>Image different percentage:</div>
            <div>Image compression time:</div>
          </div>
          <button class="download-btn">Download</button>
        </div>
        <router-link to="/" class="back-home-link">Back to homepage &gt;&gt;&gt;</router-link>
      </div>
    </div>
  </section>
</template>

<script setup>
import Ilustrasi from '@/components/Ilustrasi.vue'

// Tambahkan props/data sesuai kebutuhan jika ingin dynamic
</script>

<style scoped>
.result-section {
  position: relative;
  width: 100%;
}

.result-illustration {
  position: absolute;
  left: 0;
  top: -110px; /* geser ke atas */
  z-index: 1;
  width: 45vw;
  height: 100vh;
  max-width: 45vw;
  max-height: 100vh;
  overflow: hidden;
  pointer-events: none;
  box-sizing: border-box;
  display: block;
}

.container {
  max-width: 1200px;
  margin: 0 auto;
  position: relative;
  z-index: 2;
  padding-left: 40px; /* Atur sesuai kebutuhan */
}

.result-row {
  display: flex;
  justify-content: center;
  gap: 29px;
  margin-bottom: 32px;
  width: 100%;
  box-sizing: border-box;
  margin-left: 40px; /* Atur sesuai kebutuhan, misal 40px */
}

.result-col {
  display: flex;
  flex-direction: column;
  align-items: flex-start;
}

.result-title {
  color: #fff;
  font-size: 2rem;
  font-weight: bold;
  margin-bottom: 1rem;
  margin-left: 0.5rem;
}

.result-image-box {
  width: 550px;
  height: 330px;
  border: 2.5px dashed #cfd8dc;
  border-radius: 8px;
  background: transparent;
  display: flex;
  align-items: center;
  justify-content: center;
}

.result-img {
  width: 80px;
  opacity: 0.7;
}

.result-info-row {
  display: flex;
  flex-direction: column;
  align-items: flex-start;
  gap: 10px;
  margin-left: 10rem;
  margin-bottom: 2rem;
  width: 100%;
  box-sizing: border-box;

  text-align: left; /* teks rata kiri */
}

.result-info {
  color: #aebdc2;
  font-size: 1.15rem;
  display: flex;
  flex-direction: column;
  gap: 0.5rem;
  margin-right: 2rem;
}

.result-box {
  flex: 1;
  min-width: 320px;
  max-width: 48%;
  aspect-ratio: 16/9;
  border: 2px dashed #fff;
  display: flex;
  align-items: center;
  justify-content: center;
  background: rgba(255, 255, 255, 0.05);
}

.download-btn {
  padding: 0.5rem 2.2rem;
  background: transparent;
  color: #fff;
  font-size: 1.2rem;
  font-weight: bold;
  border: 2px solid #1de9b6;
  border-radius: 22px;
  cursor: pointer;
  transition:
    background 0.2s,
    color 0.2s,
    box-shadow 0.2s;
  box-shadow: 0 0 8px 0 rgba(30, 233, 182, 0.1);
  background: linear-gradient(90deg, rgba(30, 233, 182, 0.08) 0%, rgba(95, 110, 228, 0.08) 100%);
}

.download-btn:hover {
  background: linear-gradient(90deg, rgba(30, 233, 182, 0.18) 0%, rgba(95, 110, 228, 0.18) 100%);
  color: #fff;
  box-shadow: 0 0 16px 2px rgba(30, 233, 182, 0.18);
}

.back-home-link {
  position: absolute;
  right: 3rem;
  bottom: 2rem;
  color: #fff;
  font-size: 1.5rem;
  font-weight: bold;
  text-decoration: none;
  letter-spacing: 1px;
  transition: color 0.2s;
}

.back-home-link:hover {
  color: #1de9b6;
}
</style>
