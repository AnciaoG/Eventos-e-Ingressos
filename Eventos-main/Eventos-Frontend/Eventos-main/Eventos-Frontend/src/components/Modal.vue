<template>
  <div class="modal-overlay" v-if="show">
    <div class="modal-content">
      <button class="modal-close" @click="$emit('close')">&times;</button>
      <slot />
    </div>
  </div>
</template>
<script setup>
defineProps({ show: Boolean });
</script>
<style scoped>
.modal-overlay {
  position: fixed; top: 0; left: 0; right:0; bottom:0;
  background: rgba(19,52,59,0.18);
  z-index: 200;
  display: flex; align-items: center; justify-content: center;
}
.modal-content {
  background: var(--color-surface);
  border-radius: 24px;
  min-width: 320px;
  min-height: 160px;
  padding: 2.2rem 2.3rem;
  box-shadow: 0 8px 22px rgba(33,128,141,0.19);
  position: relative;
}
.modal-close {
  position: absolute;
  top: 1rem; right: 1rem;
  background: none; border: none;
  font-size: 2rem;
  color: var(--color-primary);
  cursor: pointer;
}
</style>
