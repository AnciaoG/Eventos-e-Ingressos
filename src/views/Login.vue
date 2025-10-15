<template>
  <main class="auth-bg">
    <section class="auth-card">
      <h2>Entrar</h2>
      <form @submit.prevent="fazerLogin" novalidate>
        <label for="email">Email</label>
        <input id="email" type="email" v-model="email" required placeholder="seu@email.com" />

        <label for="senha">Senha</label>
        <input id="senha" type="password" v-model="senha" required placeholder="Digite sua senha" />

        <label>Tipo de usuário</label>
        <div class="tipo-user">
          <label><input type="radio" value="normal" v-model="tipo" /> Usuário</label>
          <label><input type="radio" value="colaborador" v-model="tipo" /> Colaborador</label>
          <label><input type="radio" value="admin" v-model="tipo" /> Admin</label>
        </div>

        <button type="submit">Entrar</button>
      </form>
      <p class="error-msg" v-if="erro">{{ erro }}</p>
    </section>
  </main>
</template>

<script setup>
import { ref } from 'vue';
import { useRouter } from 'vue-router';

const email = ref('');
const senha = ref('');
const tipo = ref('normal');
const erro = ref('');
const router = useRouter();

function fazerLogin() {
  if (email.value && senha.value) {
    if (tipo.value === 'admin') {
      router.push('/admin');
    } else if (tipo.value === 'colaborador') {
      router.push('/colaborador');
    } else {
      router.push('/eventos');
    }
  } else {
    erro.value = 'Preencha email e senha.';
  }
}
</script>

<style scoped>
.auth-bg {
  min-height: 100vh;
  background: linear-gradient(135deg, #36177e 0%, #7b1fa2 80%, #fff 100%);
  display: flex;
  align-items: center;
  justify-content: center;
}
.auth-card {
  background: #fff;
  border-radius: 18px;
  box-shadow: 0 2px 18px rgba(76,31,162,0.11);
  padding: 2.7rem 2.4rem 2rem;
  width: 100%;
  max-width: 340px;
  text-align: center;
}
h2 {
  color: #7b1fa2;
  margin-bottom: 2.2rem;
  font-size: 1.7rem;
  font-weight: bold;
}
form {
  display: flex;
  flex-direction: column;
  gap: 1.2rem;
}
label {
  text-align: left;
  font-weight: 600;
  color: #6532c2;
  margin-bottom: 0.2rem;
}
input[type="text"],
input[type="email"],
input[type="password"] {
  padding: 0.75rem;
  border-radius: 14px;
  border: 1px solid #d3c6ef;
  background: #f5f2fa;
  font-size: 1rem;
}
input:focus {
  border-color: #7b1fa2;
  outline: none;
  background: #ede4f7;
}
.tipo-user {
  display: flex;
  gap: 1.2rem;
  justify-content: center;
  margin-bottom: 0.5rem;
}
.tipo-user label {
  color: #5341a4;
  font-weight: 600;
  display: flex;
  align-items: center;
  gap: 0.3rem;
  font-size: 1rem;
  cursor: pointer;
}
button {
  background: linear-gradient(90deg, #7b1fa2 60%, #36177e 100%);
  color: white;
  font-weight: 700;
  padding: 0.9rem 0;
  border: none;
  border-radius: 14px;
  box-shadow: 0 1px 9px rgba(76,31,162,0.08);
  margin-top: 0.5rem;
  font-size: 1.1rem;
  cursor: pointer;
}
button:hover {
  background: linear-gradient(90deg, #6532c2 40%, #463390 100%);
}
.error-msg {
  color: #e53935;
  font-weight: 700;
  margin-top: 1rem;
}
</style>
