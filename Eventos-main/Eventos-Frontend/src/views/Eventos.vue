<template>
  <main class="eventos-bg">
    <section class="eventos-container">
      <h2>Eventos Disponíveis</h2>
      <p class="subtitle">Confira as atrações para você.</p>

      <div class="eventos-grid">
        <div
          v-for="evento in eventos"
          :key="evento.id"
          class="evento-card"
          @click="abrirModal(evento)"
        >
          <img :src="evento.img" alt="Capa evento" class="evento-img" />
          <div class="info">
            <span class="evento-nome">{{ evento.nome }}</span>
            <span class="evento-data">{{ formatarData(evento.data) }}</span>
            <span class="evento-local"> {{ evento.local }}</span>
          </div>
        </div>
      </div>

      <div v-if="modalAberto" class="modal-overlay" @click="fecharModal">
        <div class="modal-content" @click.stop>
          <h3>{{ eventoSelecionado.nome }}</h3>
          <img :src="eventoSelecionado.img" alt="Imagem do evento" />
          <p>{{ eventoSelecionado.descricao }}</p>

          <button class="comprar-btn-modal" @click="comprarIngresso(eventoSelecionado.id)">
            Comprar ingresso
          </button>
          <button class="btn-fechar" @click="fecharModal">Fechar</button>
        </div>
      </div>
    </section>
  </main>
</template>

<script setup>
import { ref, onMounted } from 'vue'
import { useRouter } from 'vue-router'
import { api } from '../services/api'  

const router = useRouter()

const eventos = ref([])
const modalAberto = ref(false)
const eventoSelecionado = ref(null)

onMounted(async () => {
  try {
    const res = await api.get('eventos/')   
    eventos.value = res.data
    console.log('Eventos carregados:', eventos.value)
  } catch (err) {
    console.error('Erro ao carregar eventos:', err)
  }
})

function abrirModal(evento) {
  eventoSelecionado.value = evento
  modalAberto.value = true
}

function fecharModal() {
  modalAberto.value = false
  eventoSelecionado.value = null
}

function comprarIngresso(id) {
  router.push({ path: '/pagamento', query: { id } })
}

function formatarData(data) {
  return new Date(data).toLocaleDateString('pt-BR')
}
</script>


<style scoped>
.eventos-bg {
  background: linear-gradient(135deg, #f7f2ff 40%, #f1eaff 100%);
  min-height: 100vh;
  padding: 2rem;
}

.eventos-container {
  max-width: 900px;
  margin: 0 auto;
  background: #fff;
  border-radius: 22px;
  box-shadow: 0 6px 36px rgba(123, 31, 162, 0.15);
  padding: 3rem 2.5rem;
  box-sizing: border-box;
}

.eventos-container h2 {
  color: #7b1fa2;
  font-weight: 900;
  font-size: 2rem;
  text-transform: uppercase;
  margin-bottom: 0.8rem;
}

.subtitle {
  color: #46187e;
  margin-bottom: 2rem;
  font-size: 1.1rem;
  font-weight: 700;
}

.eventos-grid {
  display: flex;
  flex-wrap: wrap;
  gap: 2rem;
  justify-content: flex-start;
}

.evento-card {
  background: #faf6ff;
  border-radius: 20px;
  box-shadow: 0 6px 24px rgba(120, 80, 180, 0.12);
  overflow: hidden;
  width: 280px;
  text-align: left;
  cursor: pointer;
  transition: transform 0.2s, box-shadow 0.25s;
}

.evento-card:hover {
  box-shadow: 0 10px 36px rgba(123, 31, 162, 0.25);
  transform: scale(1.05);
}

.evento-img {
  width: 100%;
  height: 150px;
  object-fit: cover;
}

.info {
  padding: 1.2rem 1.5rem;
}

.evento-nome {
  font-weight: 900;
  font-size: 1.2rem;
  color: #601a99;
}

.evento-data,
.evento-local {
  font-size: 1rem;
  color: #7b1fa2;
}

.modal-overlay {
  position: fixed;
  top: 0;
  left: 0;
  right: 0;
  bottom: 0;
  background-color: rgba(75, 35, 146, 0.85);
  display: flex;
  justify-content: center;
  align-items: center;
  z-index: 3000;
}

.modal-content {
  background: #fff;
  border-radius: 20px;
  padding: 2rem;
  max-width: 520px;
  text-align: center;
  box-shadow: 0 8px 18px rgba(123, 31, 162, 0.3);
}

.modal-content img {
  width: 100%;
  border-radius: 12px;
  margin-bottom: 1rem;
}

.comprar-btn-modal {
  background: linear-gradient(90deg, #7b1fa2, #46187e);
  color: white;
  border: none;
  border-radius: 18px;
  padding: 1rem;
  font-weight: 700;
  width: 100%;
  margin-bottom: 1rem;
  cursor: pointer;
}

.btn-fechar {
  color: #7b1fa2;
  font-weight: bold;
  background: none;
  border: none;
  cursor: pointer;
}
</style>
