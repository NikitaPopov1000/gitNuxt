<script setup lang="ts">

</script>

<template>
<div class="search relative flex-1 w-full mx-32">
  <input type="text" placeholder="Поиск" class="global_search py-4 px-12 w-full">
  <svg class="absolute top-4 left-4" xmlns="http://www.w3.org/2000/svg" width="18" height="18" viewBox="0 0 18 18" fill="none">
    <path d="M8.11111 15.2222C12.0385 15.2222 15.2222 12.0385 15.2222 8.11111C15.2222 4.18375 12.0385 1 8.11111 1C4.18375 1 1 4.18375 1 8.11111C1 12.0385 4.18375 15.2222 8.11111 15.2222Z" stroke="#454545" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/>
    <path d="M17 17L13.1333 13.1333" stroke="#454545" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/>
  </svg>
</div>
</template>

<style scoped>
.global_search {
  border-radius: 0.5rem;
  background: #DEDEDE;
  color: #454545;
  font-size: 1rem;
  font-style: normal;
  font-weight: 400;
  line-height: normal;
  outline:none;
}
</style>