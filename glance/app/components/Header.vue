<script setup lang="ts">

</script>

<template>
  <header class="header">
   <div class=" container mx-auto py-5 flex justify-between items-center">
     <div class="">
       <a href="/" class="dark_momo logo">glance</a>
     </div>


     <SearchGlobal/>

     <div class="flex gap-8">
       <div class="flex flex-col gap-2 items-center">

         <svg width="26" height="24" viewBox="0 0 22 26" fill="none" xmlns="http://www.w3.org/2000/svg">
           <rect width="2" height="2" rx="1" fill="#454545"/>
           <rect x="6" width="20" height="2" rx="1" fill="#454545"/>
           <rect y="8" width="2" height="2" rx="1" fill="#454545"/>
           <rect x="6" y="8" width="20" height="2" rx="1" fill="#454545"/>
           <rect y="16" width="2" height="2" rx="1" fill="#454545"/>
           <rect x="6" y="16" width="20" height="2" rx="1" fill="#454545"/>
         </svg>
         <a href="/catalog" class="span_header">Каталог</a>
       </div>
       <div class="flex flex-col gap-2 items-center">
         <svg xmlns="http://www.w3.org/2000/svg" width="36" height="24" viewBox="0 0 22 26" fill="none">
           <path
               d="M9 22C9.55228 22 10 21.5523 10 21C10 20.4477 9.55228 20 9 20C8.44772 20 8 20.4477 8 21C8 21.5523 8.44772 22 9 22Z"
               stroke="#454545" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/>
           <path
               d="M19 22C19.5523 22 20 21.5523 20 21C20 20.4477 19.5523 20 19 20C18.4477 20 18 20.4477 18 21C18 21.5523 18.4477 22 19 22Z"
               stroke="#454545" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/>
           <path
               d="M1 1H5L7.68 15.2823C7.77144 15.7734 8.02191 16.2145 8.38755 16.5285C8.75318 16.8424 9.2107 17.0092 9.68 16.9996H19.4C19.8693 17.0092 20.3268 16.8424 20.6925 16.5285C21.0581 16.2145 21.3086 15.7734 21.4 15.2823L23 6.3332H6"
               stroke="#454545" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/>
         </svg>
         <span class="span_header">Корзина</span>
       </div>
       <div class="flex flex-col gap-2 items-center">
         <svg xmlns="http://www.w3.org/2000/svg" width="26" height="24" viewBox="0 0 22 26" fill="none">
           <path
               d="M21 23V20.6667C21 19.429 20.4732 18.242 19.5355 17.3668C18.5979 16.4917 17.3261 16 16 16H6C4.67392 16 3.40215 16.4917 2.46447 17.3668C1.52678 18.242 1 19.429 1 20.6667V23"
               stroke="#454545" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/>
           <path
               d="M10.5 11C13.2614 11 15.5 8.76142 15.5 6C15.5 3.23858 13.2614 1 10.5 1C7.73858 1 5.5 3.23858 5.5 6C5.5 8.76142 7.73858 11 10.5 11Z"
               stroke="#454545" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/>
         </svg>
         <span class="span_header">Профиль</span>
       </div>
     </div>
   </div>
  </header>
</template>

<style>
.logo {
  font-size: 1.75rem;
  font-style: normal;
  font-weight: 400;
  line-height: normal;
  background: linear-gradient(267deg, #260DC1 6.29%, #59006F 100%);
  background-clip: text;
  -webkit-background-clip: text;
  -webkit-text-fill-color: transparent;
}
.span_header {
  color: #454545;
  font-size: 0.875rem;
  font-style: normal;
  font-weight: 300;
  line-height: normal;
}

.header {
  border-bottom: 1px solid #C1C1C1;
}
</style>
