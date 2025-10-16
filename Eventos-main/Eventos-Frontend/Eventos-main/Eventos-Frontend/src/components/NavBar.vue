<template>
  <nav class="navbar">
    <div class="logo">Eventos! <span class="emoji">🎫</span></div>
    <ul class="menu">
      <li><router-link to="/">Início</router-link></li>
      <li><router-link to="/admin/login">Admin</router-link></li>
    </ul>
    <button class="theme-toggle" @click="$emit('toggle-theme')">
      🌙
    </button>
  </nav>
</template>
<style scoped>
.navbar {
  background: linear-gradient(90deg, #21808d 0%, #2dd2e0 100%);
  color: #fff;
  padding: 1.1rem 2.3rem;
  display: flex;
  align-items: center;
  justify-content: space-between;
  box-shadow: 0 4px 20px rgba(33,128,141,0.08);
}
.logo {
  font-weight: 700;
  font-size: 1.45rem;
  letter-spacing: 0.7px;
}
.menu {
  list-style: none;
  display: flex;
  gap: 1.5rem;
  margin: 0;
  padding: 0;
}
.menu li a {
  color: #fff; text-decoration: none;
  font-weight: 600; font-size: 1.07rem;
  border-radius: 8px; padding: 0.3rem 0.7rem;
  transition: background 0.27s;
}
.menu li a.router-link-exact-active, .menu li a:hover {
  background: rgba(255,255,255,0.19);
}
.theme-toggle {
  background: transparent;
  border: none;
  font-size: 1.45rem;
  color: #fff;
  margin-left: 1.2rem;
  cursor: pointer;
}
</style>
