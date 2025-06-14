<template>
  <section class="about-section">
    <div class="about-illustration">
      <Ilustrasi />
    </div>
    <div class="about-glass-box" data-aos="fade-up" data-aos-duration="1000" data-aos-delay="600">
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

<style src="@/assets/aboutpage.css"></style>
