import router from "./router.js";

const app = new Vue({
  router,
  data: () => ({
    show_menu: false,
    menu: [
      {
        type: "inner-link",
        name: "主控台",
        target: "/",
      },
      {
        type: "inner-link",
        name: "關鍵字排行",
        target: "/rank",
      },
      {
        type: "inner-link",
        name: "字詞圖表分析",
        target: "/statistics",
      },
      {
        type: "inner-link",
        name: "關於",
        target: "/about",
      },
    ],
  }),
  methods: {
    go(path) {
      if (this.isCurrent(path)) return;
      this.show_menu = false;
      this.$router.push(path);
    },
    isCurrent(path) {
      if (path === this.$route.path) return true;
      else return false;
    },
  },
}).$mount("#app");
