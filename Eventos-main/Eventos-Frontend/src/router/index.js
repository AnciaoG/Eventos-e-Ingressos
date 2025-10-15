import { createRouter, createWebHistory } from 'vue-router';

// Views do projeto:
import Home from '../views/Home.vue';
import EventDetails from '../views/EventDetails.vue';
import Checkout from '../views/Checkout.vue';
import AdminLogin from '../views/AdminLogin.vue';
import AdminDashboard from '../views/AdminDashboard.vue';

const routes = [
  { path: '/', component: Home },
  { path: '/evento/:id', component: EventDetails, props: true },
  { path: '/checkout', name: 'Checkout', component: Checkout },
  { path: '/admin/login', component: AdminLogin },
  { path: '/admin', component: AdminDashboard },
  // Coloque aqui outras views/admin se precisar, como /admin/eventos!
];

const router = createRouter({
  history: createWebHistory(),
  routes,
});

export default router;
