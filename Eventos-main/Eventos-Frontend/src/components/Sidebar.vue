<template>
  <aside class="sidebar">
    <router-link to="/admin">Dashboard</router-link>
    <router-link to="/admin/eventos">Eventos</router-link>
    <router-link to="/admin/relatorios">Relatórios</router-link>
    <router-link to="/admin/configuracoes">Configurações</router-link>
  </aside>
</template>
<style scoped>
.sidebar {
  width:220px; height:100vh; padding:2rem 0 0 0; background:#f7f9fc; border-right:1px solid var(--color-gray);
  box-shadow:0 0 8px rgba(0,0,0,0.03); display:flex; flex-direction:column;
}
.router-link {
  color:var(--color-primary); font-weight:600; font-size:1.1rem; padding:1rem 2rem; text-decoration:none;
}
.router-link.router-link-exact-active { background:#e3f6fa; border-radius:0 15px 15px 0;}
</style>
