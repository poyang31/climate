const dynamicColors = () => {
  const r = Math.floor(Math.random() * 100 + 150);
  const g = Math.floor(Math.random() * 100 + 150);
  const b = Math.floor(Math.random() * 100 + 150);
  return "rgb(" + r + "," + g + "," + b + ")";
};

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
            backgroundColor: Object.keys(this.levels).map(dynamicColors),
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
};

export default {
  name: "Statistics",
  components: {
    RankPie,
  },
  template: `
<div class="w-full py-11 flex justify-center">
  <rank-pie />
</div>
  `,
};
