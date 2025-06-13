<template>
  <nav class="main-navbar" data-aos="fade-down" data-aos-duration="1000">
    <div class="nav-glassy-group">
      <router-link to="/about-project" class="nav-link">About Project</router-link>
      <router-link to="/about-us" class="nav-link">About Us</router-link>
    </div>
  </nav>
</template>

<style scoped>
.main-navbar {
  width: 100vw;
  display: flex;
  justify-content: center;
  align-items: center;
  padding: 1.5rem 0 2rem 0;
  background: transparent;
  position: relative;
  z-index: 10;
}

.nav-glassy-group {
  display: flex;
  gap: 2.5rem;
  background: rgba(30, 40, 60, 0.18);
  border-radius: 18px;
  padding: 0.5rem 2.5rem;
  box-shadow: 0 4px 32px 0 rgba(30, 233, 182, 0.08);
  backdrop-filter: blur(10px);
  border: 1.5px solid rgba(255, 255, 255, 0.1);
}

.nav-link {
  color: #fff;
  font-size: 1.18rem;
  font-weight: 600;
  text-decoration: none;
  padding: 0.5rem 0.8rem;
  border-radius: 6px;
  background: transparent;
  position: relative;
  transition: color 0.18s;
  overflow: hidden;
}

.nav-link::after {
  content: '';
  display: block;
  position: absolute;
  left: 0;
  bottom: 0.2rem;
  width: 100%;
  height: 3px;
  background: linear-gradient(90deg, #5f6ee4 0%, #1ee9b6 100%);
  border-radius: 2px;
  transform: scaleX(0);
  transition: transform 0.25s cubic-bezier(0.4, 0, 0.2, 1);
}

.nav-link:hover::after,
.nav-link.router-link-exact-active::after {
  transform: scaleX(1);
}

.nav-link:hover,
.nav-link.router-link-exact-active {
  color: #1ee9b6;
}
</style>
