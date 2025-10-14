<template>
  <div class="card event-card" @click="$emit('detalhes', evento.id)">
    <div class="cardbody">
      <h3>{{ evento.nome }}</h3>
      <div class="event-meta">{{ formatDate(evento.data) }} &middot; {{ evento.local }}</div>
      <p>{{ evento.descricao }}</p>
      <div class="event-price">
        A partir de R$ {{ getMinPrice(evento.ingressos) }}
      </div>
    </div>
  </div>
</template>
<script setup>
defineProps({ evento: Object });
function formatDate(dateString) {
  const date = new Date(dateString);
  return date.toLocaleDateString('pt-BR');
}
function getMinPrice(ingressos) {
  return Math.min(...ingressos.map(i => i.preco)).toFixed(2);
}
</script>
<style scoped>
.card.event-card {
  border-radius: var(--radius-lg);
  background: var(--color-surface);
  box-shadow: var(--shadow-card);
  padding: 1.4rem;
  transition: transform .16s, box-shadow .16s;
  cursor: pointer;
}
.card.event-card:hover {
  transform: translateY(-2px) scale(1.01);
  box-shadow: 0 10px 28px rgba(33,128,141,0.11);
}
h3 {
  margin-bottom: 0.5rem;
  color: var(--color-primary);
}
.event-meta {
  font-size: 0.95rem;
  color: #62806b;
  margin-bottom: 0.7rem;
}
.event-price {
  font-weight: bold;
  color: var(--color-primary);
  margin-top: 0.7rem;
}
</style>
