<template>
  <section class="compressor-section section flex-left">
    <div class="container">
      <Ilustrasi2 />
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
import { ref, onMounted } from 'vue'
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
  padding-top: 4.5rem;
}

.compressor-title {
  font-size: 3.2rem;
  font-weight: bold;
  margin-bottom: 2.5rem;
  text-align: left;
}

.upload-container {
  border: 2.5px dashed #cfd8dc;
  border-radius: var(--radius-lg, 32px);
  width: 100%;
  max-width: 720px;
  height: 400px;
  margin-bottom: 2.5rem;
  background: transparent;
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  cursor: pointer;
  position: relative;
  transition: border-color 0.2s;
  margin-left: 0;
  margin-right: auto;
}

.upload-container:hover {
  border-color: var(--primary);
}

.file-input {
  display: none;
}

.picture-logo {
  width: 140px;
  margin-bottom: 1rem;
  opacity: 0.7;
}

.no-file {
  color: #7b8a8b;
  font-size: 1.4rem;
  font-weight: 600;
}

.slider-action-row {
  display: flex;
  align-items: center;
  gap: 2.5rem;
  margin-bottom: 2.5rem;
  justify-content: flex-start;
  width: 100%;
  max-width: 720px;
  margin-left: 0;
  margin-right: auto;
  padding-left: 0;
}

.slider-component-class {
  width: 65%;
  min-width: 200px;
  max-width: 500px;
  margin-left: 0 !important;
  margin-right: 0 !important;
}

.compress-btn {
  padding: 1rem 1rem;
  background: linear-gradient(120deg, rgba(29, 233, 182, 0.18) 0%, rgba(95, 110, 228, 0.18) 100%);
  color: #fff;
  font-size: 1.3rem;
  font-weight: bold;
  border: 1.5px solid rgba(255, 255, 255, 0.35);
  border-radius: 24px;
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
</style>
