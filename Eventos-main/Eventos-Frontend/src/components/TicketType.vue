<template>
  <div class="ticket-type-card" v-for="ticket in ingressos" :key="ticket.tipo">
    <div class="title">{{ ticket.tipo }}</div>
    <div class="price">R$ {{ ticket.preco.toFixed(2) }}</div>
    <div class="available">Disponíveis: {{ ticket.disponivel }}</div>
    <button @click="$emit('selecionar', ticket)">Selecionar</button>
  </div>
</template>
<script setup>
defineProps({ ingressos: Array });
</script>
<style scoped>
.ticket-type-card {
  background: var(--color-surface);
  border-radius: 16px;
  box-shadow: var(--shadow-card);
  padding: 1rem 1.5rem;
  margin: 0.7rem 0;
  display: flex;
  flex-direction: column;
  gap: 0.55rem;
}
.title { color: var(--color-primary); font-weight: bold; font-size: 1rem; }
.price { font-size: 1.05rem; margin-bottom: 0.2rem; }
.available { font-size: 0.9rem; color: #376; }
button {
  align-self: flex-start;
  background: var(--color-primary);
  color: #fff;
  border:none;
  border-radius: 10px;
  font-weight: 600;
  padding: 0.4rem 1.4rem;
  margin-top: 0.4rem;
  cursor: pointer;
}
button:hover { background: var(--color-primary-hover); }
</style>
