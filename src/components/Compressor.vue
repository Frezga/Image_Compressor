<template>
  <section class="compressor-section">
    <Ilustrasi2 />
    <h2 class="compressor-title" data-aos="fade-right" data-aos-duration="900">
      Insert your picture
    </h2>
    <div class="upload-container" @click="triggerFileInput" data-aos="fade-right">
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
    <div class="slider-action-row">
      <Slider v-model="quality" :min="1" :max="100" />
      <button class="result-btn">Compress &gt;&gt;&gt;</button>
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
  min-height: 100vh;
  width: 100vw;
  color: #fff;
  padding: 1rem 1rem;
  position: relative;
}

.compressor-title {
  font-size: 4.5rem;
  margin-left: 11rem;
  font-weight: bold;
  margin-bottom: 2rem;
  text-align: left;
}

.upload-container {
  border: 2px dashed #cfd8dc;
  margin-left: 11rem;
  border-radius: 8px;
  width: 800px;
  height: 440px;
  margin-bottom: 2rem;
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
  border-color: #64ffda;
}

.file-input {
  display: none;
}

.picture-logo {
  width: 150px;
  margin-bottom: 0.5rem;
  opacity: 0.7;
}

.no-file {
  color: #7b8a8b;
  font-size: 1.3rem;
  font-weight: 600;
}

.slider-action-row {
  display: flex;
  align-items: center;
  gap: 2rem; /* jarak antara slider dan tombol */
  margin-bottom: 2rem;
}

.result-btn {
  margin-top: 0;
  padding: 0.7rem 2.2rem;
  background: linear-gradient(90deg, rgba(30, 233, 182, 0.18) 0%, rgba(95, 110, 228, 0.18) 100%);
  color: #fff;
  font-size: 1.3rem;
  font-weight: bold;
  letter-spacing: 1px;
  border: 1.5px solid rgba(255, 255, 255, 0.35);
  border-radius: 16px;
  backdrop-filter: blur(8px);
  box-shadow: 0 0 12px 0 rgba(30, 233, 182, 0.1);
  cursor: pointer;
  transition:
    box-shadow 0.25s,
    background 0.2s,
    border-color 0.2s;
}

.result-btn:hover {
  box-shadow:
    0 0 24px 4px rgba(95, 110, 228, 0.25),
    0 0 8px 2px rgba(30, 233, 182, 0.18);
  border-color: #5f6ee4;
  background: linear-gradient(90deg, rgba(95, 110, 228, 0.28) 0%, rgba(30, 233, 182, 0.28) 100%);
}
</style>
