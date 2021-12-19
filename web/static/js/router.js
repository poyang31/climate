import Dashboard from "./views/Dashboard.js";
import About from "./views/About.js";

const routes = [
  {
    path: "/",
    component: Dashboard,
  },
  {
    path: "/about",
    component: About,
  },
];

export default new VueRouter({
  routes,
});
