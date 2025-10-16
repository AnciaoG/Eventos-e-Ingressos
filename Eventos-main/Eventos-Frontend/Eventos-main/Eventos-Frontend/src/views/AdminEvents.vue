<template>
  <main>
    <h2>{{ isEditando ? 'Editar Evento' : 'Cadastrar Evento' }}</h2>
    <form @submit.prevent="salvar">
      <label>Nome:
        <input type="text" v-model="evento.nome" required />
      </label>
      <label>Local:
        <input type="text" v-model="evento.local" required />
      </label>
      <label>Data:
        <input type="date" v-model="evento.data" required />
      </label>
      <label>Descrição:
        <textarea v-model="evento.descricao"></textarea>
      </label>
      <button type="submit">Salvar</button>
    </form>
  </main>
</template>

<script setup>
import { ref, watchEffect, onMounted } from 'vue';
import { useRoute, useRouter } from 'vue-router';

const route = useRoute();
const router = useRouter();

const isEditando = ref(false);
const evento = ref({
  nome: '',
  local: '',
  data: '',
  descricao: '',
});

const eventos = ref([
  {
    id: 1,
    nome: 'Concerto Rock',
    local: 'Auditório Central',
    data: '2025-10-15',
    descricao: 'Show especial de rock com bandas renomadas',
  },
  {
    id: 2,
    nome: 'Simpósio Tecnologia',
    local: 'Centro de Convenções',
    data: '2025-11-20',
    descricao: 'Evento sobre as últimas tendências em tecnologia',
  },
]);

onMounted(() => {
  if (route.params.id) {
    isEditando.value = true;
    const id = Number(route.params.id);
    let editEvent = eventos.value.find((e) => e.id === id);
    if (editEvent) evento.value = { ...editEvent };
  }
});

function salvar() {
  if (isEditando.value) {
    // Atualiza evento existente
    const idx = eventos.value.findIndex((e) => e.id === Number(route.params.id));
    if (idx !== -1) eventos.value[idx] = { ...evento.value, id: Number(route.params.id) };
  } else {
    // Adiciona novo evento
    const novoId = Math.max(...eventos.value.map((e) => e.id)) + 1;
    eventos.value.push({ ...evento.value, id: novoId });
  }
  router.push('/admin');
}
</script>

<style scoped>
main {
  background: var(--cor-secundaria);
  padding: 2rem;
  max-width: 480px;
  margin: 2rem auto;
  border-radius: 16px;
  box-shadow: 0 5px 20px rgba(0, 0, 0, 0.1);
  color: var(--cor-texto);
}
h2 {
  color: var(--cor-primary);
  margin-bottom: 1rem;
  font-weight: 700;
  text-align: center;
}
form label {
  display: block;
  font-weight: 600;
  margin-bottom: 0.5rem;
}
input,
textarea {
  display: block;
  width: 100%;
  padding: 0.6rem 1rem;
  border-radius: 12px;
  border: 1px solid var(--cor-borda);
  box-shadow: inset 0 1px 5px #cbd6e6;
  font-size: 1rem;
  margin-bottom: 1.2rem;
  resize: vertical;
  transition: border-color 0.3s ease;
  color: var(--cor-texto);
  background: white;
}
input:focus,
textarea:focus {
  border-color: var(--cor-primary);
  outline: none;
  box-shadow: 0 0 8px var(--cor-primary);
}
button {
  width: 100%;
  background-color: var(--cor-primary);
  border: none;
  color: white;
  padding: 0.8rem 0;
  font-size: 1.2rem;
  font-weight: 700;
  border-radius: 16px;
  cursor: pointer;
  transition: background-color 0.3s ease;
}
button:hover {
  background-color: var(--cor-primary-dark);
}
</style>
