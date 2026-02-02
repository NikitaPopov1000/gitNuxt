<script setup lang="ts">
const { data, pending, error, refresh } = await useFetch('http://127.0.0.1:5000/categories')
const categories = computed(() => data.value?.items || [])
console.log(categories)
</script>

<template>
<div class="w-full container mx-auto">
  <CarouselMain />
  <h6 class="title-category pb-7">Каталог</h6>
  <div class="flex gap-4" v-for="category in categories" :key='category.id'>
  <CardCategory :title="category.title"/>
  </div>
  <div class="stocks py-12">
    <h6 class="title-stocks">Акции</h6>
    <CardProduct />
  </div>
</div>
</template>

<style scoped>
.title-category {
  font-size: 2rem;
  font-style: normal;
  font-weight: 400;
  line-height: normal;
  color: #0C0C0C;
}

.title-stocks {
  color: #0C0C0C;
  font-size: 2rem;
  font-style: normal;
  font-weight: 400;
  line-height: normal;
}
</style>