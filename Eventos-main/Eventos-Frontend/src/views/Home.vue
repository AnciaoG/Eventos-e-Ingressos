<template>
  <div class="home-wrap">
    <h2 class="home-title">Próximos eventos</h2>
    <div class="event-list">
      <EventCard v-for="evento in eventos" :key="evento.id" :evento="evento" @detalhes="verDetalhes"/>
    </div>
  </div>
</template>

<script setup>
import EventCard from '../components/EventCard.vue'
import { ref } from 'vue'
import { useRouter } from 'vue-router'

const eventos = ref([
  {id:1, nome:"Concerto Rock", local:"Auditório Central", data:"2025-10-15", descricao:"Show especial de rock...", ingressos:[{tipo:"Pista",preco:50,disponivel:100},{tipo:"VIP",preco:120,disponivel:50}]},
  {id:2, nome:"Simpósio Tecnologia", local:"Centro de Convenções", data:"2025-11-20", descricao:"Evento sobre tecnologia...", ingressos:[{tipo:"Individual",preco:80,disponivel:200}]}
])

const router = useRouter();

function verDetalhes(id) {
  router.push(`/evento/${id}`);
}
</script>

<style scoped>
.home-wrap {
  max-width: 980px;
  margin: 2rem auto 0 auto;
  padding: 0 1rem;
}

.home-title {
  font-size: 2rem;
  color: var(--color-primary);
  font-weight: 800;
  margin-bottom: 1.5rem;
  text-align: center;
}

.event-list {
  display: flex;
  flex-wrap: wrap;
  gap: 1.5rem;
  justify-content: center;
}
</style>
