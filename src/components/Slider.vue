<template>
  <div class="slider-wrapper">
    <div class="slider-track" :style="trackStyle"></div>
    <input
      type="range"
      :min="min"
      :max="max"
      :step="step"
      :value="modelValue"
      @input="$emit('update:modelValue', +$event.target.value)"
      class="slider"
      ref="slider"
    />
    <div class="slider-value" :style="valueStyle">{{ modelValue }}%</div>
  </div>
</template>

<script setup>
import { computed, ref, onMounted } from 'vue'

const props = defineProps({
  modelValue: { type: Number, required: true },
  min: { type: Number, default: 1 },
  max: { type: Number, default: 100 },
  step: { type: Number, default: 1 },
})

const slider = ref(null)
const sliderWidth = ref(0)

const percent = computed(() => (props.modelValue - props.min) / (props.max - props.min))

const valueStyle = computed(() => {
  const thumbWidth = 32
  const width = sliderWidth.value || 370
  const offset = percent.value * (width - thumbWidth) + thumbWidth / 2
  return {
    left: `${offset}px`,
    transform: 'translateX(-50%)',
  }
})

const trackStyle = computed(() => {
  const percentValue = percent.value * 100
  return {
    background: `linear-gradient(90deg, #1de9b6 ${percentValue}%, #00bcd4 ${percentValue}%, #22313a 0%)`,
  }
})

const updateSliderWidth = () => {
  if (slider.value) {
    sliderWidth.value = slider.value.offsetWidth
  }
}

onMounted(updateSliderWidth)
window.addEventListener('resize', updateSliderWidth)
</script>

<style scoped>
.slider-wrapper {
  position: relative;
  width: 370px;
  margin: 2rem 0 3rem 0;
  margin-left: 13rem;
  height: 56px;
}

.slider-track {
  position: absolute;
  top: 50%;
  left: 0;
  width: 100%;
  height: 8px;
  border-radius: 6px;
  transform: translateY(-50%);
  z-index: 0;
  background: linear-gradient(90deg, #1de9b6 10%, #00bcd4 20%, #22313a 30%);
  transition: background 0.2s;
}

.slider {
  width: 100%;
  height: 8px;
  border-radius: 6px;
  background: transparent;
  outline: none;
  margin: 0;
  -webkit-appearance: none;
  appearance: none;
  position: relative;
  z-index: 1;
}

.slider::-webkit-slider-thumb {
  -webkit-appearance: none;
  appearance: none;
  width: 32px;
  height: 32px;
  border-radius: 50%;
  background: #1de9b6;
  border: 4px solid #0a1a24;
  box-shadow: 0 2px 8px rgba(30, 233, 182, 0.25);
  cursor: pointer;
  transition: background 0.2s;
}

.slider::-webkit-slider-thumb:hover {
  background: #00bcd4;
}

.slider::-moz-range-thumb {
  width: 32px;
  height: 32px;
  border-radius: 50%;
  background: #1de9b6;
  border: 4px solid #0a1a24;
  box-shadow: 0 2px 8px rgba(30, 233, 182, 0.25);
  cursor: pointer;
  transition: background 0.2s;
}

.slider::-moz-range-thumb:hover {
  background: #00bcd4;
}

.slider::-ms-thumb {
  width: 32px;
  height: 32px;
  border-radius: 50%;
  background: #1de9b6;
  border: 4px solid #0a1a24;
  box-shadow: 0 2px 8px rgba(30, 233, 182, 0.25);
  cursor: pointer;
  transition: background 0.2s;
}

.slider:focus {
  outline: none;
}

.slider::-webkit-slider-runnable-track {
  height: 8px;
  border-radius: 6px;
  background: transparent;
}

.slider::-ms-fill-lower {
  background: transparent;
  border-radius: 6px;
}
.slider::-ms-fill-upper {
  background: transparent;
  border-radius: 6px;
}

.slider:focus::-ms-fill-lower {
  background: transparent;
}
.slider:focus::-ms-fill-upper {
  background: transparent;
}

.slider-value {
  position: absolute;
  top: -38px;
  min-width: 48px;
  height: 38px;
  background: #1de9b6;
  color: #222;
  font-weight: bold;
  border-radius: 10px;
  padding: 0.3rem 0.8rem;
  font-size: 2rem;
  display: flex;
  align-items: center;
  justify-content: center;
  box-shadow: 0 2px 8px rgba(30, 233, 182, 0.15);
  pointer-events: none;
  transition: left 0.1s;
  z-index: 2;
}

@media (max-width: 500px) {
  .slider-wrapper {
    width: 98vw;
    max-width: 98vw;
  }
}
</style>
