const RankPie = {
  name: "RankPie",
  extends: VueChartJs.Pie,
  data: () => ({
    levels: null,
  }),
  computed: {
    drawData() {
      return {
        labels: Object.keys(this.levels),
        datasets: [
          {
            data: Object.values(this.levels),
            backgroundColor: [
              "rgb(255, 99, 132)",
              "rgb(54, 162, 235)",
              "rgb(255, 205, 86)",
              "rgb(255, 199, 132)",
              "rgb(164, 162, 235)",
              "rgb(255, 205, 86)",
              "rgb(255, 159, 132)",
              "rgb(354, 162, 235)",
              "rgb(255, 205, 86)",
              "rgb(255, 205, 86)",
            ],
            hoverOffset: 4,
          },
        ],
      };
    },
  },
  async created() {
    const response = await axios.get("/rank");
    this.levels = response.data;
    this.renderChart(this.drawData, this.options);
  },
}

export default {
  name: "Statistics",
  components: {
    RankPie
  },
  template: `
<div class="w-full py-11 flex justify-center">
  <rank-pie />
</div>
  `
};
