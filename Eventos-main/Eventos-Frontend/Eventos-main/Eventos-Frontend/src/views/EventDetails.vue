<template>
  <div class="details-wrap" v-if="evento">
    <div class="details-card">
      <span class="icon-main">🎸</span>
      <h2>{{ evento.nome }}</h2>
      <p><strong>Local:</strong> {{ evento.local }}</p>
      <p><strong>Data:</strong> {{ evento.data }}</p>
      <p class="desc">{{ evento.descricao }}</p>
    </div>
    <TicketType :ingressos="evento.ingressos" @selecionar="irParaCheckout"/>
  </div>
</template>
<script setup>
import TicketType from '../components/TicketType.vue';
import { ref, onMounted } from 'vue';
import { useRoute, useRouter } from 'vue-router';
const eventos = [
  {id:1, nome:"Concerto Rock",local:"Auditório Central",data:"2025-10-15",descricao:"Show especial de rock...",ingressos:[{tipo:"Pista",preco:50,disponivel:100},{tipo:"VIP",preco:120,disponivel:50}]},
  {id:2, nome:"Simpósio Tecnologia",local:"Centro de Convenções",data:"2025-11-20",descricao:"Evento sobre tecnologia...",ingressos:[{tipo:"Individual",preco:80,disponivel:200}]}
];
const route = useRoute();
const router = useRouter();
const evento = ref(null);
onMounted(()=>{ evento.value = eventos.find(e=> e.id === Number(route.params.id)); });
function irParaCheckout(ticket) {
  router.push({ name: "Checkout", query: { tipo: ticket.tipo, quantidade: 1, preco: ticket.preco }});
}
</script>
<style scoped>
.details-wrap { display:flex; flex-direction:column; align-items:center; padding:2rem 0;}
.details-card {
  background: #eefbfd;
  border-radius: 24px;
  box-shadow: 0 5px 38px rgba(24,116,205,0.08);
  padding:2rem 2.2rem; margin-bottom:2.2rem; min-width:300px; text-align:left;
  color: #234;
}
.icon-main { font-size:2rem; color:var(--color-primary); margin-bottom:0.2rem;}
h2 { color:var(--color-primary); font-size:1.55rem;}
.desc { margin-top:0.7rem; font-size:1rem; color:#356;}
</style>
