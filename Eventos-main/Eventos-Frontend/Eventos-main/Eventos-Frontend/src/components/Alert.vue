<template>
  <div class="alert" :class="tipo">
    <slot />
  </div>
</template>
<script setup>
defineProps({ tipo: { type: String, default: "info" } });
</script>
<style scoped>
.alert {
  padding:0.9rem 1.4rem; border-radius:10px; margin:1.1rem 0;
  background:linear-gradient(90deg,#e6efeb 70%,#fdfdfd 100%);
  font-weight:600; color:#21808d; box-shadow:var(--shadow-card);
}
.alert.success { background:linear-gradient(90deg,#dafce6,#eefff6); color:#129941;}
.alert.error { background:linear-gradient(90deg,#ffe6e6,#fff3f3); color:#e53935;}
</style>
