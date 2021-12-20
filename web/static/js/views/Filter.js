export default {
  name: "Filter",
  data: () => ({
    result: null,
  }),
  computed: {
    keyword() {
        return this.$route.params.keyword;
    }
  },
  async created() {
    const url = new URLSearchParams();
    url.set("keyword", this.keyword);
    const response = await axios.get(`/filter?${url.toString()}`);
    this.result = response.data;
  },
  template: `
<div class="py-12 bg-white">
  <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
    <div class="lg:text-center">
      <h2 class="text-base text-indigo-600 font-semibold tracking-wide uppercase">在我們的數據庫中</h2>
      <p class="mt-2 text-3xl leading-8 font-extrabold tracking-tight text-gray-900 sm:text-4xl">
        目前有 {{ result.count }} 篇文章
      </p>
      <p class="mt-4 max-w-2xl text-xl text-gray-500 lg:mx-auto">
        內容提到了「{{ keyword }}」
      </p>
    </div>

    <div class="mt-10">
      <dl class="flex justify-center">
        <div v-for="(i, j) in result.origin_count" :key="j">
          <span class="ml-16 text-lg leading-6 font-medium text-gray-900">{{ j }}</span>
          <span class="mt-2 ml-16 text-base text-gray-500">{{ i }}</span>
        </div>
      </dl>
    </div>
  </div>
</div>
  `
};
