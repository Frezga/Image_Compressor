<template>
  <section class="about-section">
    <div class="about-illustration">
      <Ilustrasi />
    </div>
    <div class="about-glass-box">
      <h2 class="about-title">About Project</h2>
      <p>
        Project kompresi gambar adalah project mata kuliah Aljabar Linear pada semester dua. Project
        ini menggunakan PCA untuk mereduksi data multi dimensi menjadi data dengan dimensi yang
        lebih kecil, dengan tetap mempertahankan karakteristik dari data tersebut.
      </p>
      <p>
        Untuk memulai program kompresi gambar, User harus <i>scroll down</i> ke bawah sehingga
        muncul box di mana User bisa menginput media (dalam kasus ini adalah foto). Setelah
        menginput media, User bisa mengatur seberapa besar persentase kompresi yang akan dikenakan
        pada media.
      </p>
      <p>
        Setelahnya, User hendaklah menekan result agar media bisa diproses. Setelah beberapa saat,
        User akan dialihkan ke page baru di mana hasil dari kompresi sudah terlihat. Selain hasil
        kompresi, terdapat juga penampakan media yang kita input sebelum diproses sehingga User bisa
        melihat perbandingan di antara keduanya.
      </p>
      <p>
        Dibawah hasil kompresi juga terdapat keterangan tentang program seperti persentase perbedaan
        kedua gambar dan lamanya eksekusi program. User juga bisa men-<i>download</i> hasil dari
        media yang sudah dikompresi.
      </p>
    </div>
  </section>
</template>

<script setup>
import Ilustrasi from '@/components/Ilustrasi.vue'
</script>

<style scoped>
.about-section {
  height: 100vh;
  width: 100vw;
  position: relative;
  display: flex;
  align-items: center;
  justify-content: center;
  background: transparent;
}

.about-illustration {
  position: absolute;
  left: 0;
  top: -40px; /* geser ke atas */
  z-index: 1;
  width: 45vw;
  height: 100vh;
  max-width: 45vw;
  max-height: 100vh;
  overflow: hidden;
  pointer-events: none;
  box-sizing: border-box;
  display: block;
}

.about-glass-box {
  max-width: 900px;
  width: 90vw;
  background: rgba(30, 40, 60, 0.28);
  border-radius: 28px;
  box-shadow:
    0 8px 40px 0 rgba(30, 233, 182, 0.13),
    0 0 32px 4px rgba(95, 110, 228, 0.1);
  backdrop-filter: blur(16px);
  border: 2px solid rgba(255, 255, 255, 0.18);
  padding: 2.8rem 2.8rem 2.8rem 2.8rem;
  color: #f3f6fa;
  font-size: 1.22rem;
  font-family: 'DM Sans', sans-serif;
  position: relative;
  z-index: 2;
  text-align: left;
  filter: drop-shadow(0 0 16px #1de9b6aa);
  box-sizing: border-box;
  margin: 0; /* hilangkan margin */
}

.about-title {
  font-size: 2.3rem;
  font-weight: bold;
  margin-bottom: 1.5rem;
  color: #fff;
  text-shadow:
    0 0 8px #1de9b6cc,
    0 2px 8px #5f6ee4aa;
  letter-spacing: 1px;
}

.about-glass-box p {
  margin-bottom: 1.1rem;
  line-height: 1.7;
  color: #e0f2f1;
  text-shadow: 0 0 4px #1de9b633;
}

@media (max-width: 1000px) {
  .about-glass-box {
    max-width: 98vw;
    width: 98vw;
    padding: 1.2rem;
  }
}
</style>
