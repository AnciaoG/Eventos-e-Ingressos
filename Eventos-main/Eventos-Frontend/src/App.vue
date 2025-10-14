<template>
  <div id="app">
    <NavBar @toggle-theme="toggleTheme" />
    <router-view />
  </div>
</template>

<script setup>
import { ref, watchEffect } from 'vue';
import NavBar from './components/NavBar.vue';

// Sistema de tema claro/escuro simples
const tema = ref(localStorage.getItem('tema') || 'light');
function toggleTheme() {
  tema.value = tema.value === 'light' ? 'dark' : 'light';
}
watchEffect(() => {
  document.body.setAttribute('data-theme', tema.value);
  localStorage.setItem('tema', tema.value);
});
</script>

<style>
:root {
  --color-primary: #21808d;
  --color-primary-hover: #1d7480;
  --color-bg: #fdfdfd;
  --color-surface: #fff;
  --color-text: #13343b;
  --color-gray: #f5f5f5;
  --radius-lg: 14px;
  --shadow-card: 0 1px 3px rgba(0,0,0,0.04), 0 1px 2px rgba(0,0,0,0.02);
}
body[data-theme='dark'] {
  --color-bg: #1a2225;
  --color-surface: #223239;
  --color-text: #f7f9f9;
  --color-primary: #21e0e0;
  --color-primary-hover: #15bcbc;
  --color-gray: #2d363c;
}
body {
  background: var(--color-bg);
  color: var(--color-text);
  font-family: "Segoe UI", Arial, sans-serif;
  margin: 0;
  transition: background 0.2s, color 0.2s;
}
#app { min-height: 100vh; }
</style>
