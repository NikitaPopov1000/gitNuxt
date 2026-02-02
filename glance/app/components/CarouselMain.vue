<script setup lang="ts">
const items = [
 '/images/banner.png',
]
</script>

<template>
  <UCarousel v-slot="{ item }" arrows :items="items" class="w-full max-w-[8-rem] mx-auto py-10">
    <img :src="item" width="320" height="320" class="rounded-lg w-full" loading="lazy">
  </UCarousel>
</template>

<style scoped>

</style>