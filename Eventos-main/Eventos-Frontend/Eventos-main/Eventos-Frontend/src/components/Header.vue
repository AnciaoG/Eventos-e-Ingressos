<template>
  <header>
    <h1>Eventos</h1>
    <nav>
      <router-link to="/">Início</router-link>
      <router-link to="/login">Admin</router-link>
    </nav>
  </header>
</template>

<script setup>
</script>

<style scoped>
header {
  background: #007bff;
  color: white;
  padding: 1rem 2rem;
  display: flex;
  align-items: center;
  justify-content: space-between;
}
nav a {
  color: white;
  margin-left: 1rem;
  text-decoration: none;
}
nav a:hover,
nav a.router-link-exact-active {
  text-decoration: underline;
}
</style>
