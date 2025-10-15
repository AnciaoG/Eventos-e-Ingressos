<template>
  <div class="stat-card">
    <span class="stat-icon">{{ icon }}</span>
    <div class="stat-title">{{ title }}</div>
    <div class="stat-value">{{ value }}</div>
  </div>
</template>
<script setup>
defineProps({ title:String, value:[String,Number], icon:String });
</script>
<style scoped>
.stat-card {
  background:linear-gradient(95deg,#e3f6fa 0%,#e9fafb 100%);
  border-radius:16px;
  box-shadow:var(--shadow-card);
  padding:1.2rem 2.4rem;
  display:flex;
  flex-direction:column;
  align-items:center;
  min-width:120px;
}
.stat-icon { font-size:2rem; }
.stat-title { font-size:1rem; margin:0.6rem 0; color:var(--color-primary);}
.stat-value { font-size:1.4rem; font-weight:700; color:#222;}
</style>
