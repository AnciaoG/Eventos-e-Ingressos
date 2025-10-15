<template>
  <main class="home-bg">
    <header class="main-header">
      <h1>EVENTOS+</h1>
      <button class="login-btn" @click="irParaLogin">Login</button>
    </header>
    <section class="hero">
      <h2>Encontre e compre ingressos para eventos!</h2>
    </section>
    <section class="categorias">
      <h3>Categorias</h3>
      <div class="categoria-list">
        <div v-for="cat in categorias" :key="cat.nome" class="cat-card">
          <span>{{ cat.nome }}</span>
        </div>
      </div>
    </section>
    <section class="eventos">
      <h3>Eventos em destaque</h3>
      <div class="eventos-grid">
        <div v-for="ev in eventos" :key="ev.id" class="evento-card">
          <img :src="ev.img" alt="evento" class="evento-img" />
          <div class="evento-nome">{{ ev.nome }}</div>
          <div class="evento-data">{{ formatarData(ev.data) }}</div>
          <div class="evento-local">{{ ev.local }}</div>
        </div>
      </div>
    </section>
  </main>
</template>

<script setup>
import { useRouter } from 'vue-router';
const router = useRouter();

function irParaLogin() {
  router.push('/login');
}

const categorias = [
  { nome: 'Show' },
  { nome: 'Palestras' },
  { nome: 'Teatro' },
];

const eventos = [
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
  {
    id: 3,
    nome: 'Stand Up Comedy',
    data: '2025-12-17',
    local: 'Teatro Central',
    img: 'https://images.unsplash.com/photo-1511671782779-c97d3d27a1d4?auto=format&fit=crop&w=350&q=80',
  },
];

function formatarData(data) {
  return new Date(data).toLocaleDateString('pt-BR');
}
</script>

<style scoped>
.home-bg {
  min-height: 100vh;
  background: #f7f5fa;
}
.main-header {
  background: #7b1fa2;
  color: #fff;
  padding: 1.8rem 2rem 1rem 2rem;
  display: flex;
  justify-content: space-between;
  align-items: center;
  border-radius: 0 0 22px 22px;
}
.login-btn {
  background: #fff;
  color: #7b1fa2;
  border: none;
  border-radius: 12px;
  font-weight: 700;
  padding: 0.6rem 1.4rem;
  font-size: 1rem;
  cursor: pointer;
}
.hero {
  text-align: center;
  margin: 3rem 0 2rem 0;
}
.hero h2 {
  color: #7b1fa2;
}
.categorias {
  padding: 1rem 2rem;
}
.categoria-list {
  display: flex;
  gap: 1.2rem;
}
.cat-card {
  background: #e1c3fa;
  border-radius: 11px;
  padding: 1rem 2.2rem;
  color: #4b1fa2;
  font-weight: 600;
}
.eventos {
  padding: 1rem 2rem;
}
.eventos-grid {
  display: flex;
  gap: 2rem;
  flex-wrap: wrap;
}
.evento-card {
  background: #fff;
  border-radius: 13px;
  box-shadow: 0 2px 12px #7a1fa24e;
  padding: 1rem;
  width: 205px;
  display: flex;
  flex-direction: column;
  align-items: center;
}
.evento-img {
  width: 100%;
  height: 110px;
  object-fit: cover;
  border-radius: 9px;
}
.evento-nome {
  font-weight: 700;
  color: #7b1fa2;
  margin-top: 0.8rem;
}
.evento-data,
.evento-local {
  color: #463390;
  font-size: 1rem;
}
</style>
