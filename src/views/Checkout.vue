<template>
  <main class="checkout-main">
    <h2>Finalizar pedido</h2>
    <form @submit.prevent="finalizarCompra" class="checkout-form">
      <div><label>Nome<input v-model="nome" required /></label></div>
      <div><label>Email<input v-model="email" required /></label></div>
      <div>
        <label>Pagamento
          <select v-model="pagamento" required>
            <option value="" disabled>Escolha...</option>
            <option>Crédito</option>
            <option>Pix</option>
            <option>Boleto</option>
          </select>
        </label>
      </div>
      <button type="submit">Confirmar</button>
    </form>
    <div v-if="confirmado" class="msg-confirmado">
      <span>✅ Pedido enviado!</span>
      <button @click="retornar">Voltar para eventos</button>
    </div>
  </main>
</template>
<script setup>
import { ref } from 'vue';
import { useRouter, useRoute } from 'vue-router';
const nome = ref(''); const email = ref(''); const pagamento = ref('');
const confirmado = ref(false);
const router = useRouter();
function finalizarCompra() { confirmado.value = true; }
function retornar() { router.push('/'); }
</script>
<style scoped>
.checkout-main { max-width:440px; background:var(--color-surface); margin:3rem auto; padding:2.6rem 2.4rem; border-radius:22px; box-shadow:var(--shadow-card); }
h2 { color:var(--color-primary); text-align:center; margin-bottom:2rem;}
.checkout-form { display:grid; gap:1rem; margin-top:1.2rem;}
label { font-weight:600;}
input,select { width:100%; padding:0.7rem 0.6rem; border-radius:10px; border:1px solid var(--color-primary);}
button { background:var(--color-primary); color:#fff; border:none; border-radius:10px; font-weight:600; font-size:1.15rem; padding:0.8rem 0; width:100%; margin-top:1.4rem;}
button:hover { background:var(--color-primary-hover);}
.msg-confirmado { text-align:center;}
</style>
