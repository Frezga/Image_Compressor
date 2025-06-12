<template>
  <nav class="navbar">
    <RouterLink to="/about-project" class="nav-link">About Project</RouterLink>
    <RouterLink to="/about-us" class="nav-link">About Us</RouterLink>
  </nav>
</template>
<style scoped>
/* Pastikan properti .navbar tetap seperti sebelumnya */
.navbar {
  width: 100%;
  position: fixed;
  top: 0;
  left: 0;
  z-index: 100; /* Pastikan navbar di atas konten lain */
  text-align: center;
  padding: 1rem 0;
  margin-top: 0;

  /* Glassy Effect */
  background-color: rgba(34, 151, 153, 0.08); /* Dasar biru kehijauan yang sangat transparan */
  backdrop-filter: blur(15px); /* Efek buram yang lebih kuat untuk kesan kaca */

  /* Box-shadow untuk kesan "terbang" dan blue glow */
  box-shadow:
    0 4px 20px rgba(0, 0, 0, 0.1),
    0 0 10px rgba(34, 151, 153, 0.4);
}

.nav-link {
  color: #fff;
  font-family: 'Helvetica', sans-serif;
  text-decoration: none;
  margin: 0 10rem;
  font-size: 1.5rem;
  padding: 0.5rem 1rem;
  border-radius: 10px;
  background-color: transparent;
  box-shadow: 0 0 0px rgba(0, 0, 0, 0);

  transition:
    background-image 0.4s ease-in-out,
    background-color 0.4s ease-in-out,
    color 0.4s ease-in-out,
    transform 0.2s ease-in-out,
    box-shadow 0.4s ease-in-out;
}

/* Efek hover untuk nav-link - Fokus pada perubahan ini */
.nav-link:hover {
  /* Gradient biru yang lebih gelap/soft */
  background-image: linear-gradient(to right, #229799, #4a69bd, #2c3e50);
  color: #fff;
  transform: translateY(-3px);
  box-shadow:
    0 5px 20px rgba(44, 62, 80, 0.4),
    0 0 10px rgba(34, 151, 153, 1);
}
</style>
