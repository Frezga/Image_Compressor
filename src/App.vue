<script setup>
import Navbar from '@/components/Navbar.vue'
import { RouterView } from 'vue-router'
// import AOS from 'aos'
import 'aos/dist/aos.css'
import { ref, onMounted} from 'vue';
AOS.init()

//usage example of fetch GET Request
const message = ref('loading...');
const error = ref(null);
async function fetchData(){
  try{
    const response = await fetch('http://localhost:8000/Image_Compression');
    if(!response.ok){
      throw new Error(`HTTP error! status: ${response.status}`);
    }
    const data = await response.json();
    message.value = data.message; //took an asumption backend is returning a object with 'message' property
  }
  catch(e){
    error.value = e.message;
    console.error("fetch error:", e);
  }
}

onMounted(() => {
  fetchData();
});

//usage example of fetch POST Request with JSON Data
const postResponse = ref(null);
const postError = ref(null);
const inputValue = ref('');
async function postData(){
  postResponse.value = null;
  postError.value = null;

  try{
    const response = await fetch('http://localhost:8000/Image_Compression', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
      },
      body: JSON.stringify({my_data: inputValue.value}), //send the data in json format
    });
    if(!response.ok){
      throw new Error(`HTTP error! status: ${response.status}`);
    }
    const data = await response.json();
    postResponse.value = data;
  }
  catch(e){
    postError.value = e.message;
    console.error("POST error: ", e);
  }
}
//fetch (url, options) is receive two argument

</script>

<template>
  <Navbar />
  <RouterView />
</template>

<style>
#app {
  font-family:
    DM Sans,
    sans-serif;
  font-weight: 300;
  font-style: normal;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
}

body,
html {
  margin: 0;
  font-family:
    sans-serif,
    DM Sans;
}
</style>

<script>
import AOS from 'aos'

export default {
  mounted() {
    AOS.refresh() // atau AOS.init() jika pertama kali
  },
  activated() {
    AOS.refresh()
  },
}
</script>
