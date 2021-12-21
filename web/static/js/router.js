import Dashboard from "./views/Dashboard.js";
import Search from "./views/Search.js";
import Rank from "./views/Rank.js";
import Statistics from "./views/Statistics.js";
import About from "./views/About.js";

const routes = [
  {
    path: "/",
    component: Dashboard,
  },
  {
    path: "/search/:keyword",
    props: true,
    component: Search,
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
  {
    path: "*",
    component: {
      template: '<div class="py-5 text-center">404 Not Found</div>'
    }
  }
];

export default new VueRouter({
  routes,
});
