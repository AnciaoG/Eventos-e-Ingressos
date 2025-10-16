<template>
  <div class="dashboard-wrap">
    <div class="stats-grid">
      <StatCard title="Total Vendas" :value="1200" icon="💸"/>
      <StatCard title="Eventos Ativos" :value="4" icon="🎉"/>
      <StatCard title="Ingressos Vendidos" :value="923" icon="🎫"/>
    </div>
    <div class="events-section">
      <h3>Eventos</h3>
      <table>
        <thead><tr><th>Evento</th><th>Data</th><th></th></tr></thead>
        <tbody>
          <tr v-for="evento in eventos" :key="evento.id">
            <td>{{ evento.nome }}</td>
            <td>{{ evento.data }}</td>
            <td>
              <button @click="$emit('editar', evento)">Editar</button>
            </td>
          </tr>
        </tbody>
      </table>
      <button @click="$emit('novo')">Novo Evento</button>
    </div>
  </div>
</template>
<script setup>
import StatCard from '../components/Statcard.vue';
const eventos = [
  {id:1, nome:'Concerto Rock', data:'2025-10-15'},
  {id:2, nome:'Simpósio Tecnologia', data:'2025-11-20'}
];
</script>
<style scoped>
.dashboard-wrap {
  max-width: 1000px;
  margin: 2rem auto;
  padding: 1.6rem;
  background: var(--color-surface); border-radius: 16px;
}
.stats-grid {
  display: flex; gap:1.6rem; justify-content:center; margin-bottom:2rem;
}
.events-section { background:#fafcff; border-radius:14px; box-shadow:var(--shadow-card); padding:1.2rem;}
h3 { margin-bottom: 1rem;}
table { width:100%; border-collapse:collapse;}
th, td { padding:0.9rem 1rem; border-bottom:1px solid var(--color-gray);}
button { background:var(--color-primary); color:#fff; border:none; border-radius:8px; padding:0.38rem 1.1rem; font-weight:600; cursor:pointer;}
button:hover { background:var(--color-primary-hover);}
</style>
