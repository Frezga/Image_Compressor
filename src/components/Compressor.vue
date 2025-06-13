<template>
  <section class="compressor-section">
    <Ilustrasi2 />
    <h2 class="compressor-title">Insert Your Pict</h2>
    <div class="upload-container" @click="triggerFileInput">
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
    <div class="slider-section">
      <div class="slider-label">{{ quality }}%</div>
      <input type="range" min="1" max="100" v-model="quality" class="slider" />
    </div>
    <button class="result-btn">Result &gt;&gt;&gt;</button>
    <slot />
  </section>
</template>

<script setup>
import { ref } from 'vue'
import Ilustrasi2 from './Ilustrasi2.vue'

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

.slider-section {
  display: flex;
  padding-left: 11rem;
  align-items: center;
  margin: 2rem 0 3rem 0;
}

.slider-label {
  background: #1de9b6;
  color: #222;
  font-weight: bold;
  border-radius: 6px;
  padding: 0.3rem 0.8rem;
  margin-right: 1rem;
  font-size: 1.1rem;
  position: relative;
  top: -10px;
}

.slider {
  width: 350px;
  accent-color: #1de9b6;
  height: 6px;
  border-radius: 4px;
}

.result-btn {
  margin-top: 1.5rem;
  background: none;
  border: none;
  color: #fff;
  font-size: 1.5rem;
  font-weight: bold;
  letter-spacing: 2px;
  cursor: pointer;
  transition: color 0.2s;
}

.result-btn:hover {
  color: #1de9b6;
}
</style>
