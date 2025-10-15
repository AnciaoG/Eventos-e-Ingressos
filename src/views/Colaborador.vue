<template>
  <main class="colab-bg">
    <section class="colab-card">
      <h2>Área do Colaborador</h2>
      <button class="btn-cadastrar" @click="mostrarForm = !mostrarForm">
        {{ mostrarForm ? 'Fechar formulário' : 'Cadastrar Novo Evento' }}
      </button>

      <form v-if="mostrarForm" @submit.prevent="cadastrarEvento" class="form-evento" novalidate>
        <label for="nome">Nome do Evento</label>
        <input id="nome" type="text" v-model="nome" placeholder="Digite o nome do evento" required />

        <label for="data">Data</label>
        <input id="data" type="date" v-model="data" required />

        <label for="local">Localização</label>
        <input id="local" type="text" v-model="local" placeholder="Local do evento" required />

        <label for="img">URL da Imagem</label>
        <input id="img" type="text" v-model="img" placeholder="Cole a URL da imagem" required />

        <button type="submit" class="btn-submit">Cadastrar Evento</button>
      </form>

      <p v-if="mensagem" class="mensagem-sucesso">{{ mensagem }}</p>

      <section class="eventos">
        <h3>Meus Eventos</h3>
        <div class="eventos-grid">
          <div v-for="evento in eventos" :key="evento.id" class="evento-card">
            <img :src="evento.img" alt="Evento" class="evento-img" />
            <div class="evento-nome">{{ evento.nome }}</div>
            <div class="evento-data">{{ formatarData(evento.data) }}</div>
            <div class="evento-local">{{ evento.local }}</div>
          </div>
        </div>
      </section>
    </section>
  </main>
</template>

<script setup>
import { ref } from 'vue';

const mostrarForm = ref(false);
const nome = ref('');
const data = ref('');
const local = ref('');
const img = ref('');
const mensagem = ref('');
const eventos = ref([
  {
    id: 1,
    nome: 'Festival de Rock',
    data: '2025-11-15',
    local: 'Praça do Estádio',
    img: 'https://images.unsplash.com/photo-1506744038136-46273834b3fb?auto=format&fit=crop&w=350&q=80',
  },
  {
    id: 2,
    nome: 'Noite Eletrônica',
    data: '2025-12-02',
    local: 'Arena Multishow',
    img: 'https://images.unsplash.com/photo-1464983953574-0892a716854b?auto=format&fit=crop&w=350&q=80',
  },
]);

function formatarData(data) {
  return new Date(data).toLocaleDateString('pt-BR');
}

function cadastrarEvento() {
  if (!nome.value || !data.value || !local.value || !img.value) {
    mensagem.value = 'Por favor, preencha todos os campos.';
    return;
  }
  const novoId = eventos.value.length + 1;
  eventos.value.push({
    id: novoId,
    nome: nome.value,
    data: data.value,
    local: local.value,
    img: img.value,
  });
  mensagem.value = `Evento "${nome.value}" cadastrado com sucesso!`;
  nome.value = '';
  data.value = '';
  local.value = '';
  img.value = '';
  mostrarForm.value = false;
}
</script>

<style scoped>
.colab-bg {
  min-height: 100vh;
  background: linear-gradient(135deg, #eae0fd 40%, #f5f2fa 100%);
  display: flex;
  justify-content: center;
  align-items: flex-start;
  padding: 2rem;
}
.colab-card {
  width: 700px;
  background: white;
  border-radius: 18px;
  box-shadow: 0 2px 18px rgba(76, 31, 162, 0.1);
  padding: 2.5rem;
  text-align: left;
}
h2 {
  color: #7b1fa2;
  margin-bottom: 1.6rem;
}
.btn-cadastrar {
  background-color: #7b1fa2;
  color: white;
  font-weight: 700;
  border: none;
  border-radius: 18px;
  padding: 0.7rem 1.6rem;
  margin-bottom: 1.8rem;
  cursor: pointer;
  font-size: 1rem;
}
.btn-cadastrar:hover {
  background-color: #5a158e;
}
.form-evento {
  display: flex;
  flex-direction: column;
  gap: 1rem;
  margin-bottom: 1rem;
}
input[type='text'],
input[type='date'] {
  padding: 0.7rem;
  border-radius: 10px;
  border: 1px solid #d3c6ef;
  font-size: 1rem;
  background-color: #f5f2fa;
}
input[type='text']:focus,
input[type='date']:focus {
  outline: none;
  border-color: #7b1fa2;
  background-color: #ede4f7;
}
.btn-submit {
  font-weight: 700;
  border-radius: 14px;
  padding: 0.8rem 0;
  border: none;
  background: linear-gradient(90deg, #7b1fa2 60%, #36177e 100%);
  color: white;
  cursor: pointer;
}
.btn-submit:hover {
  background: linear-gradient(90deg, #6532c2 40%, #463390 100%);
}
.mensagem-sucesso {
  color: #2d1c99;
  font-weight: 700;
  margin-top: 1rem;
}
.eventos {
  margin-top: 3rem;
}
.eventos-grid {
  display: flex;
  gap: 1.8rem;
  flex-wrap: wrap;
}
.evento-card {
  width: calc(33.33% - 1.8rem);
  background: #faf6ff;
  border-radius: 16px;
  padding: 1rem;
  box-shadow: 0 2px 14px rgba(120, 62, 151, 0.1);
  cursor: pointer;
  transition: box-shadow 0.2s ease, transform 0.16s ease;
  display: flex;
  flex-direction: column;
  align-items: center;
}
.evento-card:hover {
  box-shadow: 0 8px 24px rgba(120, 62, 151, 0.15);
  transform: scale(1.02);
}
.evento-img {
  width: 100%;
  height: 130px;
  border-radius: 12px;
  object-fit: cover;
  margin-bottom: 1rem;
}
.evento-nome {
  color: #7b1fa2;
  font-weight: 700;
  font-size: 1.1rem;
}
.evento-data,
.evento-local {
  color: #46197e;
  font-weight: 600;
  font-size: 0.95rem;
  margin-top: 0.3rem;
  display: block;
  width: 100%;
  text-align: center;
}
</style>
