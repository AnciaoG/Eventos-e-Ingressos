<template>
  <main class="eventos-bg">
    <section class="endstadium-section">
      <h2>Eventos Disponíveis</h2>
      <p class="subtitle">Confira as atrações para você.</p>
      <div class="eventos-grid">
        <div v-for="evento in eventos" :key="evento.id" class="evento-card">
          <img :src="evento.img" alt="Capa evento" class="evento-img" />
          <div class="info">
            <span class="evento-nome">{{ evento.nome }}</span>
            <span class="evento-data">{{ formatarData(evento.data) }}</span>
            <span class="evento-local">
              📍 {{ evento.local }}
            </span>
            <button class="comprar-btn">Comprar ingresso</button>
          </div>
        </div>
      </div>
    </section>
  </main>
</template>

<script setup>
const eventos = [
  {
    id: 1,
    nome: "Festival de Rock",
    data: "2025-11-15",
    local: "Praça do Estádio",
    img: "https://images.unsplash.com/photo-1506744038136-46273834b3fb?auto=format&fit=crop&w=350&q=80",
  },
  {
    id: 2,
    nome: "Noite Eletrônica",
    data: "2025-12-02",
    local: "Arena Multishow",
    img: "https://images.unsplash.com/photo-1464983953574-0892a716854b?auto=format&fit=crop&w=350&q=80",
  },
  {
    id: 3,
    nome: "Stand Up Comedy",
    data: "2025-12-17",
    local: "Teatro Central",
    img: "https://images.unsplash.com/photo-1511671782779-c97d3d27a1d4?auto=format&fit=crop&w=350&q=80",
  },
];

function formatarData(data) {
  return new Date(data).toLocaleDateString("pt-BR");
}
</script>

<style scoped>
.eventos-bg {
  background: linear-gradient(135deg, #f5f2fa 40%, #eae0fd 100%);
  min-height: 100vh;
  padding: 2rem;
}
.endstadium-section {
  max-width: 900px;
  margin: 0 auto;
  background: #fff;
  border-radius: 28px;
  box-shadow: 0 6px 36px rgba(76, 31, 162, 0.08);
  padding: 2.5rem;
}
.endstadium-section h2 {
  color: #7b1fa2;
  text-transform: uppercase;
  font-size: 2rem;
  letter-spacing: 1.2px;
  margin-bottom: 1rem;
  font-weight: bold;
}
.subtitle {
  color: #36177e;
  margin-bottom: 2rem;
  font-size: 1.1rem;
  font-weight: 600;
}
.eventos-grid {
  display: flex;
  gap: 2rem;
  flex-wrap: wrap;
  justify-content: flex-start;
}
.evento-card {
  background: #faf6ff;
  border-radius: 18px;
  box-shadow: 0 2px 18px rgba(120, 80, 180, 0.07);
  overflow: hidden;
  width: 250px;
  display: flex;
  flex-direction: column;
  align-items: center;
  cursor: pointer;
  transition: transform 0.16s, box-shadow 0.18s;
}
.evento-card:hover {
  box-shadow: 0 6px 18px rgba(105, 61, 192, 0.15);
  transform: scale(1.03);
}
.evento-img {
  width: 100%;
  height: 130px;
  object-fit: cover;
}
.info {
  width: 100%;
  padding: 1rem;
  display: flex;
  flex-direction: column;
  align-items: flex-start;
  gap: 0.5rem;
}
.evento-nome {
  font-weight: 700;
  font-size: 1.15rem;
  color: #5a19c7;
}
.evento-data {
  font-size: 1rem;
  color: #36177e;
  font-weight: 600;
}
.evento-local {
  font-size: 1rem;
  color: #7b1fa2;
  display: flex;
  align-items: center;
}
.comprar-btn {
  margin-top: 1rem;
  padding: 0.6rem 1.3rem;
  font-weight: 700;
  border: none;
  border-radius: 12px;
  color: white;
  background: linear-gradient(90deg, #7b1fa2 60%, #36177e 100%);
  cursor: pointer;
  font-size: 1rem;
  transition: box-shadow 0.12s;
}
.comprar-btn:hover {
  background: linear-gradient(90deg, #6532c2 40%, #463390 100%);
  box-shadow: 0 6px 18px rgba(120, 31, 162, 0.14);
}
</style>
