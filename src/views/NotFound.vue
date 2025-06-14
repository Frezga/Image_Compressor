<template>
  <div class="not-found">
    <div class="notfound-glass">
      <div class="notfound-title">404</div>
      <div class="notfound-error">ERROR</div>
      <div class="notfound-desc">Page Not Found</div>
      <div class="notfound-subdesc">The page you are looking for does not exist.</div>
      <router-link to="/" class="notfound-home-link">Go Back to Home</router-link>
    </div>
  </div>
</template>

<style scoped>
.not-found {
  position: fixed;
  inset: 0;
  width: 100vw;
  height: 100vh;
  display: flex;
  align-items: center;
  justify-content: center;
  background: transparent;
  overflow: hidden;
  z-index: 9999;
}

.notfound-glass {
  background: rgba(30, 40, 60, 0.28);
  border-radius: 32px;
  box-shadow:
    0 8px 40px 0 rgba(30, 233, 182, 0.13),
    0 0 32px 4px rgba(95, 110, 228, 0.1);
  backdrop-filter: blur(16px);
  border: 2px solid rgba(255, 255, 255, 0.18);
  padding: 3.5rem 4.5rem 2.5rem 4.5rem;
  color: #f3f6fa;
  font-family: 'DM Sans', sans-serif;
  text-align: center;
  position: relative;
  z-index: 2;
  filter: drop-shadow(0 0 16px #1de9b6aa);
  display: flex;
  flex-direction: column;
  align-items: center;
  max-width: 98vw;
  box-sizing: border-box;
  overflow: hidden;
  margin-top: 0;
}

.notfound-title {
  font-size: 10rem;
  font-weight: bold;
  color: #1de9b6;
  letter-spacing: 8px;

  margin-bottom: 0.5rem;
  margin-top: -1rem;
  line-height: 1;
}

.notfound-error {
  font-size: 2.2rem;
  font-weight: 700;
  color: #ff5252;
  letter-spacing: 2px;
  margin-bottom: 0.5rem;
}

.notfound-desc {
  font-size: 2rem;
  font-weight: 600;
  color: #fff;
  margin-bottom: 0.5rem;
  text-shadow: 0 0 8px #1de9b6cc;
}

.notfound-subdesc {
  font-size: 1.1rem;
  color: #b2f7ef;
  margin-bottom: 2rem;
  text-shadow: 0 0 4px #1de9b633;
}

.notfound-home-link {
  display: inline-block;
  padding: 0.7rem 2.2rem;
  background: linear-gradient(90deg, rgba(30, 233, 182, 0.18) 0%, rgba(95, 110, 228, 0.18) 100%);
  color: #fff;
  font-size: 1.2rem;
  font-weight: bold;
  letter-spacing: 1px;
  border: 1.5px solid rgba(255, 255, 255, 0.35);
  border-radius: 16px;
  backdrop-filter: blur(8px);
  box-shadow: 0 0 12px 0 rgba(30, 233, 182, 0.1);
  cursor: pointer;
  text-decoration: none;
  transition:
    box-shadow 0.25s,
    background 0.2s,
    border-color 0.2s,
    color 0.2s;
}

.notfound-home-link:hover {
  box-shadow:
    0 0 24px 4px rgba(95, 110, 228, 0.25),
    0 0 8px 2px rgba(30, 233, 182, 0.18);
  border-color: #5f6ee4;
  background: linear-gradient(90deg, rgba(95, 110, 228, 0.28) 0%, rgba(30, 233, 182, 0.28) 100%);
  color: #1de9b6;
}
</style>
