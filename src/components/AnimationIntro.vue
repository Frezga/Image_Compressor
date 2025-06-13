<template>
  <div class="main-title">
    <h1 v-if="dynamicText !== ''">{{ dynamicText }}</h1>
    <h1 v-else class="invisible">|</h1>
  </div>
</template>

<script setup>
import { onMounted } from 'vue'
import { useAnimationTyping } from '@/utils/utils'
const { dynamicText, typing } = useAnimationTyping()

onMounted(() => {
  typing('Welcome to,')
})
</script>

<style scoped>
.main-title {
  font-size: 2.5rem;
  font-family: 'DM Sans', sans-serif;
  margin-top: 14rem;
  text-align: left;
  margin-bottom: 0;
  background: rgba(164, 232, 232, 0.25);
  border-radius: 30px;
  padding: 0px 10px;
  font-weight: bold;
  color: #fff;
  backdrop-filter: blur(2.2px);
  border: 1px solid rgba(204, 216, 216, 0.56);
}

.highlight {
  background: rgba(164, 232, 232, 0.25);
  border-radius: 0px;
  padding: 1px 1px;
  font-weight: bold;
  color: #fff;
  backdrop-filter: blur(2.2px);
  border: 1px solid rgba(204, 216, 216, 0.56);
}
</style>
