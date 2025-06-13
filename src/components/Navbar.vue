<template>
  <nav class="main-navbar" data-aos="fade-down" data-aos-duration="1000">
    <div class="nav-glassy-group">
      <a href="#about-project" class="nav-link">About Project</a>
      <a href="#about-us" class="nav-link">About Us</a>
    </div>
  </nav>
</template>

<style scoped>
.main-navbar {
  width: 100vw;
  display: flex;
  justify-content: center;
  align-items: center;
  padding: 2rem 0 1.5rem 0;
  background: transparent;
  position: relative;
  z-index: 10;
}

.nav-glassy-group {
  display: flex;
  gap: 2.5rem;
  background: rgba(255, 255, 255, 0.03);
  border: 1.5px solid rgba(255, 255, 255, 0.13);
  border-radius: 40px;
  padding: 0.2rem 1.5rem;
  backdrop-filter: blur(8px);
  box-shadow: 0 2px 24px 0 rgba(160, 132, 232, 0.08);
}

.nav-link {
  color: #fff;
  font-size: 1.35rem;
  font-weight: 500;
  text-decoration: none;
  transition:
    color 0.2s,
    background 0.2s,
    box-shadow 0.2s;
  padding: 0.7rem 2.2rem;
  border-radius: 24px;
  position: relative;
  z-index: 1;
  overflow: hidden;
}

.nav-link::before {
  content: '';
  position: absolute;
  inset: 0;
  border-radius: 24px;
  background: linear-gradient(90deg, rgba(95, 110, 228, 0.18) 0%, rgba(30, 233, 182, 0.13) 100%);
  opacity: 0;
  transition: opacity 0.25s;
  z-index: -1;
  backdrop-filter: blur(6px);
}

.nav-link:hover,
.nav-link:focus {
  color: #f6f6f6; /* biru/ungu sesuai tema */
}

.nav-link:hover::before,
.nav-link:focus::before {
  opacity: 1;
}
</style>
