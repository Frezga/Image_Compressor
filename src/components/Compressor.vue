<template>
  <section class="compressor-section section flex-left">
    <Ilustrasi2 />
    <div class="container">
      <h2 class="compressor-title" data-aos="fade-right" data-aos-duration="1000">
        Insert your picture
      </h2>
      <div
        class="upload-container"
        @click="triggerFileInput"
        data-aos="fade-right"
        data-aos-duration="900"
      >
        <input
          ref="fileInput"
          type="file"
          accept="image/*"
          class="file-input"
          @change="onFileChange"
        />
        <img src="@/assets/picture_logo.svg" alt="logo" class="picture-logo" />
        <span class="no-file">{{ fileName || 'No choosen file' }}</span>
      </div>
      <div class="slider-action-row" data-aos="fade-right" data-aos-duration="900">
        <Slider v-model="quality" :min="1" :max="100" class="slider-component-class" />
        <router-link to="/result" class="compress-btn">Compress &gt;&gt;&gt;</router-link>
      </div>
    </div>
  </section>
</template>

<script setup>
import { ref } from 'vue'
import Ilustrasi2 from './Ilustrasi2.vue'
import Slider from './Slider.vue'

const fileInput = ref(null)
const fileName = ref('')
const quality = ref(1)

function triggerFileInput() {
  fileInput.value.click()
}

function onFileChange(e) {
  const file = e.target.files[0]
  fileName.value = file ? file.name : ''
}
</script>

<style scoped>
.compressor-section {
  color: var(--text-main);
  position: relative;
  min-height: 100vh;
  background: transparent;
  padding-top: 4rem;
  display: flex;
  align-items: flex-start;
  justify-content: center;
}

.container {
  width: 100%;
  max-width: 700px; /* Increased from 420px */
  margin: 0 auto;
  margin-left: 5rem;
  display: flex;
  flex-direction: column;
  align-items: center;
}

.compressor-title {
  font-size: 2.8rem;
  font-weight: bold;
  margin-left: 1.3rem;
  margin-bottom: 2.5rem;
  text-align: left;
  align-self: flex-start;
}

.upload-container {
  border: 2.5px dashed #cfd8dc;
  border-radius: 32px;
  width: 100%;
  max-width: 600px; /* Increased */
  height: 340px; /* Increased */
  margin-bottom: 2.5rem;
  background: transparent;
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  cursor: pointer;
  position: relative;
  transition: border-color 0.2s;
}

.upload-container:hover {
  border-color: var(--primary);
}

.file-input {
  display: none;
}

.picture-logo {
  width: 110px; /* Increased */
  margin-bottom: 1.2rem;
  opacity: 0.7;
}

.no-file {
  color: #7b8a8b;
  font-size: 1.3rem; /* Increased */
  font-weight: 600;
}

.slider-action-row {
  display: flex;
  align-items: center;
  gap: 1rem;
  margin-bottom: 2.5rem;
  justify-content: flex-start;
  width: 100%;
  max-width: 600px;
  margin-left: 32px;
  margin-right: auto;
  padding-left: 0;
}

.slider-component-class {
  width: 60%;
  min-width: 120px;
  max-width: 260px;
  margin-left: 0 !important;
  margin-right: 0 !important;
}

.compress-btn {
  padding: 0.7rem 1.2rem;
  background: linear-gradient(120deg, rgba(29, 233, 182, 0.18) 0%, rgba(95, 110, 228, 0.18) 100%);
  color: #fff;
  font-size: 1rem;
  font-weight: bold;
  border: 1.5px solid rgba(255, 255, 255, 0.35);
  border-radius: 18px;
  backdrop-filter: blur(10px) saturate(160%);
  box-shadow: 0 2px 16px 0 rgba(30, 233, 182, 0.08);
  cursor: pointer;
  text-decoration: none;
  transition:
    box-shadow 0.25s,
    background 0.2s,
    border-color 0.2s;
  position: relative;
  overflow: hidden;
}

.compress-btn:hover {
  background: linear-gradient(120deg, rgba(29, 233, 182, 0.28) 0%, rgba(95, 110, 228, 0.28) 100%);
  border-color: var(--primary, #1de9b6);
  box-shadow:
    0 0 24px 4px var(--secondary, #5f6ee4),
    0 0 8px 2px var(--primary, #1de9b6);
}

/* Responsive adjustments */
@media (max-width: 900px) {
  .compressor-section {
    padding-top: 2rem;
  }
  .compressor-title {
    font-size: 1.6rem;
  }
  .upload-container,
  .slider-action-row {
    max-width: 98vw;
  }
}

@media (max-width: 600px) {
  .compressor-section {
    padding-top: 1rem;
  }
  .compressor-title {
    font-size: 1.2rem;
    margin-bottom: 1rem;
  }
  .upload-container {
    height: 180px;
    border-radius: 18px;
  }
  .slider-action-row {
    flex-direction: column;
    align-items: stretch;
    gap: 0.7rem;
  }
  .slider-component-class {
    width: 100%;
    min-width: 0;
    max-width: 100vw;
  }
  .compress-btn {
    width: 100%;
    font-size: 0.95rem;
    padding: 0.7rem 0;
  }
}
</style>
