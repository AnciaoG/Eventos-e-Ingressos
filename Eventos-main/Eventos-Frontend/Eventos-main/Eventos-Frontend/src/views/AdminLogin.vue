<template>
  <div class="login-container">
    <h2>Painel Admin</h2>
    <form @submit.prevent="login">
      <label>
        Email
        <input v-model="email" type="email" required autocomplete="username">
      </label>
      <label>
        Senha
        <input v-model="senha" type="password" required autocomplete="current-password">
      </label>
      <button type="submit">Entrar</button>
    </form>
    <p v-if="erro" class="error-msg">{{ erro }}</p>
  </div>
</template>
<script setup>
import { ref } from 'vue';
const email = ref('');
const senha = ref('');
const erro = ref('');
function login() {
  if(email.value === 'adm@adm.com' && senha.value === '123') {
    localStorage.setItem('adminAuth','yes');
    window.location.href = '/admin';
  } else {
    erro.value = 'Credenciais inválidas';
  }
}
</script>
<style scoped>
.login-container {
  max-width: 390px;
  margin: 3rem auto;
  background: var(--color-surface);
  border-radius: 16px;
  box-shadow: var(--shadow-card);
  padding: 2rem;
}
h2 { text-align:center; color:var(--color-primary); }
form { display: flex; flex-direction:column; gap:1.2rem; margin-top:1.2rem;}
label { font-weight:600; color:var(--color-primary);}
input { padding:0.7rem; font-size:1rem; border-radius:10px; border:1px solid var(--color-primary);}
button { background: var(--color-primary); color:#fff; border:none; font-size:1.1rem; font-weight:600; padding:0.7rem 0; border-radius:10px; cursor: pointer;}
button:hover { background: var(--color-primary-hover);}
.error-msg { color:#e53; margin-top:0.8rem; text-align:center;}
</style>
