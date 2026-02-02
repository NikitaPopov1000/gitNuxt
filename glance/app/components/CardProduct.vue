<script setup lang="ts">
const items = [
  '/images/Rectangle_81.pmg',
  '/images/Rectangle_81.pmg',
]

const props = defineProps<{
  name: string,
  price: number,
  old_price: number,
  inStock: boolean,
}>()

const inCart = ref<boolean>(false)

function addCart(): void {
  inCart.value = !inCart.value;
}

const favorite = ref(false)
</script>

<template>
  <div class="card w-full max-w-54 h-full max-h-132">
    <div class="card_wrapper p-6">
      <div class="card-img">
        <UCarousel v-slot="{ item }" dots :items="items" class="w-full max-w-xs mx-auto">
          <img src="/images/Rectangle_81.png" class="rounded-lg max-w-42 w-full max-h-54" alt="">
        </UCarousel>
      </div>
      <div class="card-body pt-11 text-center pb-4">
        <h6 class="card-name">{{ props.name || "Смартфон Apple iPhone 14 128GB" }}</h6>
      </div>
      <div class="price_card flex gap-2">
        <h6 class="price">{{ props.price || "84 999 ₽" }}</h6>
        <p class="old_price mt-auto" v-if="props.old_price > 1">{{ props.old_price }}</p>
      </div>
      <div class="favorite_and_stock pt-4 flex justify-between items-center">
        <p class="inStock" v-if="props.inStock=true">В наличии</p>
        <p class="unStock" v-if="props.inStock=false">Не в наличии</p>
        <button class="like" @click="favorite = !favorite">
          <svg
              class="heart"
              :class="{ active: favorite }"
              xmlns="http://www.w3.org/2000/svg"
              width="20"
              height="17"
              viewBox="0 0 20 17"
          >
            <path
                d="M17.612 2.32611C17.1722 1.90569 16.65 1.57219 16.0752 1.34465C15.5005 1.11711 14.8844 1 14.2623 1C13.6401 1 13.0241 1.11711 12.4493 1.34465C11.8746 1.57219 11.3524 1.90569 10.9126 2.32611L9.99977 3.19821L9.08699 2.32611C8.19858 1.4773 6.99364 1.00044 5.73725 1.00044C4.48085 1.00044 3.27591 1.4773 2.38751 2.32611C1.4991 3.17492 1 4.32616 1 5.52656C1 6.72696 1.4991 7.87819 2.38751 8.727L3.30029 9.5991L9.99977 16L16.6992 9.5991L17.612 8.727C18.0521 8.30679 18.4011 7.80785 18.6393 7.25871C18.8774 6.70957 19 6.12097 19 5.52656C19 4.93214 18.8774 4.34355 18.6393 3.7944C18.4011 3.24526 18.0521 2.74633 17.612 2.32611Z"
                fill="none"
                stroke="currentColor"
                stroke-width="2"
                stroke-linecap="round"
                stroke-linejoin="round"
            />
          </svg>

        </button>
      </div>
      <div class="pt-5">
        <button class="addCart" @click="addCart()"><span v-if="!inCart">В корзину</span> <span
            v-if="inCart">В корзине</span></button>
      </div>
    </div>
  </div>
</template>

<style>
.card-name {
  color: #0C0C0C;
  font-size: 1.25rem;
  font-style: normal;
  font-weight: 400;
  line-height: 2rem; /* 160% */
}

.price {
  color: #0C0C0C;
  font-size: 20px;
  font-style: normal;
  font-weight: 500;
  line-height: normal;
}

.old_price {
  color: #ABABAB;
  font-size: 0.875rem;
  font-style: normal;
  font-weight: 300;
  line-height: normal;
  text-decoration-line: line-through;
}

.inStock {
  color: #169B00;
  font-size: 0.875rem;
  font-style: normal;
  font-weight: 300;
  line-height: normal;
}

.unStock {
  color: red;
  font-size: 0.875rem;
  font-style: normal;
  font-weight: 300;
  line-height: normal;
}

.like {
  display: flex;
  width: 2.5rem;
  height: 2.5rem;
  padding: 0.5rem 0.75rem;
  flex-direction: column;
  justify-content: center;
  align-items: center;
  gap: 0.625rem;
  border-radius: 0.5rem;
  background: #F6F6F6;
  box-shadow: 1px 1px 20px 0 rgba(0, 0, 0, 0.10);
}

.heart {
  color: #0C0C0C;
  transition: color 0.2s ease;
}

.heart.active {
  color: red;
}

.addCart {
  display: flex;
  width: 10.25rem;
  height: 2.75rem;
  padding: 0.625rem 1rem;
  justify-content: center;
  align-items: center;
  gap: 0.625rem;
  border-radius: 0.5rem;
  background: #091D9E;
}

</style>