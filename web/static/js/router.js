import Dashboard from "./views/Dashboard.js";
import Filter from "./views/Filter.js";
import Rank from "./views/Rank.js";
import Statistics from "./views/Statistics.js";
import About from "./views/About.js";

const routes = [
  {
    path: "/",
    component: Dashboard,
  },
  {
    path: "/filter/:keyword",
    props: true,
    component: Filter,
  },
  {
    path: "/rank",
    component: Rank,
  },
  {
    path: "/statistics",
    component: Statistics,
  },
  {
    path: "/about",
    component: About,
  },
];

export default new VueRouter({
  routes,
});
