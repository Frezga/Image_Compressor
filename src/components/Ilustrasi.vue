<template>
  <img
    src="@/assets/abstract.png"
    alt="Abstract"
    class="abstract-img"
    data-aos="slide-right"
    data-aos-duration="1000"
    data-aos-delay="500"
    data-aos-once="true"
  />
</template>

<script setup></script>

<style scoped>
img,
svg {
  width: 100%;
  height: 100%;
  object-fit: contain;
  display: block;
}

.abstract-img {
  position: absolute;
  left: 3px;
  top: 10px;
  width: 650px;
  height: auto;
  z-index: 1;
  pointer-events: none;
  overflow: hidden;
  user-select: none;
}
</style>
