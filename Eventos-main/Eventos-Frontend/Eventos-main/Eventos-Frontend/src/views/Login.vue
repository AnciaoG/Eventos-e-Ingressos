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

      <p class="cadastro-link">
        Não tem conta?
        <button class="btn-cadastro" @click="irParaCadastro">Criar Conta</button>
      </p>
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
    if (tipo.value === 'admin') router.push('/admin');
    else if (tipo.value === 'colaborador') router.push('/colaborador');
    else router.push('/eventos');
  } else {
    erro.value = 'Preencha email e senha.';
  }
}

function irParaCadastro() {
  router.push('/cadastro');
}
</script>

<style scoped>
.auth-bg {
  min-height: 100vh;
  background: linear-gradient(135deg, #ece1fa 40%, #f0e5fe 100%);
  display: flex;
  justify-content: center;
  align-items: center;
  padding: 1rem;
}

.auth-card {
  background: white;
  border-radius: 18px;
  padding: 2.5rem 3rem;
  box-shadow: 0 2px 22px rgba(123, 31, 162, 0.17);
  width: 360px;
  text-align: center;
}

h2 {
  color: #7b1fa2;
  font-weight: 900;
  margin-bottom: 2rem;
}

label {
  font-weight: 700;
  color: #5a157c;
  display: block;
  margin: 0.7rem 0 0.3rem 0;
  text-align: left;
}

input[type='email'],
input[type='password'] {
  width: 100%;
  padding: 0.75rem;
  font-size: 1rem;
  border-radius: 12px;
  border: 1.5px solid #d1c1eb;
  background-color: #f4ebff;
  outline: none;
}

input:focus {
  border-color: #7b1fa2;
  background-color: #eae0fd;
}

.tipo-user {
  margin: 1rem 0 1.8rem 0;
  display: flex;
  justify-content: space-between;
  color: #7b1fa2;
  font-weight: 700;
}

.tipo-user label {
  cursor: pointer;
}

button[type='submit'] {
  width: 100%;
  padding: 0.9rem;
  border-radius: 18px;
  border: none;
  background: linear-gradient(90deg, #7b1fa2 60%, #46187e 100%);
  color: white;
  font-weight: 900;
  font-size: 1rem;
  cursor: pointer;
  box-shadow: 0 2px 14px #36177e55;
  transition: background 0.3s ease;
}

button[type='submit']:hover {
  background: linear-gradient(90deg, #543293 40%, #463390 100%);
}

.error-msg {
  margin-top: 1rem;
  color: #a12727;
  font-weight: 700;
}

.cadastro-link {
  margin-top: 2rem;
  font-weight: 700;
  color: #7b1fa2;
}

.btn-cadastro {
  background: none;
  border: none;
  color: #7b1fa2;
  cursor: pointer;
  font-weight: 700;
  font-size: 1rem;
  text-decoration: underline;
  margin-left: 0.3rem;
}

.btn-cadastro:hover {
  color: #5a158e;
}
</style>
