<script setup lang="ts">
const props = defineProps({
  title: String,
})
</script>

<template>
<div class="w-full max-w-50 h-full max-h-52.75  ">
<div class="flex items-center img-container justify-center bg-[#BCC5FF] rounded-lg">
  <img src="/images/image_1.png" loading="lazy" alt="">
</div>
<p class="text-center pt-3 footer-card">{{ props.title }}</p>
</div>

</template>



<style scoped>
 .img-container {
   padding: 1.25rem 3rem;
 }

 .footer-card {
   color: #000;
   font-size: 1.25rem;
   font-style: normal;
   font-weight: 300;
   line-height: normal;
 }
</style>