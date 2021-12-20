export default {
  name: "Rank",
  data: () => ({
    levels: null
  }),
  async created() {
    const response = await axios.get("/rank")
    this.levels = response.data
  },
  template: `
<div>
    <table class="mt-3 w-full table-auto">
        <thead>
            <tr>
                <th class="border-b dark:border-gray-600 font-medium p-4 pl-8 pt-0 pb-3 text-gray-400 dark:text-gray-200 text-left">排行</th>
                <th class="border-b dark:border-gray-600 font-medium p-4 pl-8 pt-0 pb-3 text-gray-400 dark:text-gray-200 text-left">字詞</th>
                <th class="border-b dark:border-gray-600 font-medium p-4 pl-8 pt-0 pb-3 text-gray-400 dark:text-gray-200 text-left">出現次數</th>
            </tr>
        </thead>
        <tbody>
            <tr v-for="(i, j, k) in levels" :key="k">
                <td class="border-b border-gray-100 dark:border-gray-700 p-4 pl-8 text-gray-500 dark:text-gray-400" v-text="k+1"></td>
                <td class="border-b border-gray-100 dark:border-gray-700 p-4 pl-8 text-gray-500 dark:text-gray-400" v-text="j"></td>
                <td class="border-b border-gray-100 dark:border-gray-700 p-4 pl-8 text-gray-500 dark:text-gray-400" v-text="i"></td>
            </tr>
        </tbody>
    </table>
</div>
  `,
};
