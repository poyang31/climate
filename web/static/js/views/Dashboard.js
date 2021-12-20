export default {
  name: "Home",
  data: () => ({
    keyword: null
  }),
  methods: {
    search() {
        if (!this.keyword) return
        this.$router.push(`/filter/${this.keyword}`)
    }
  },
  template: `
<div>
  <div class="bg-cyan-50">
    <div
      class="
        max-w-7xl
        mx-auto
        py-12
        px-4
        sm:px-6
        lg:py-16 lg:px-8 lg:flex lg:items-center lg:justify-between
      "
    >
      <h2
        class="text-3xl font-extrabold tracking-tight text-gray-900 sm:text-4xl"
      >
        <span class="block">Climate</span>
        <span class="block text-blue-600">臺灣網際網路聲量分析儀</span>
      </h2>
      <div class="mt-8 flex lg:mt-0 lg:flex-shrink-0">
        <div>
          <label for="search" class="block text-sm font-medium text-gray-700"
            >嘗試搜尋一些東西吧？</label
          >
          <div class="mt-1 relative rounded-md shadow-sm inline-flex shadow">
            <input
              type="text"
              name="search"
              id="search"
              class="
                focus:ring-blue-500 focus:border-blue-500
                block
                w-full
                pl-7
                pr-12
                py-3
                sm:text-sm
                border-gray-300
                rounded-md
              "
              placeholder="例如：王力宏..."
              @keydown.enter="search"
              v-model="keyword"
            />
          </div>
          <div class="ml-3 inline-flex rounded-md shadow">
            <button
              class="
                inline-flex
                items-center
                justify-center
                px-5
                py-3
                border border-transparent
                text-base
                font-medium
                rounded-md
                text-white
                bg-blue-600
                hover:bg-blue-700
              "
              @click="search"
            >
              Search
            </button>
          </div>
        </div>
      </div>
    </div>
  </div>
  <div class="py-12 bg-white">
    <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
      <div class="lg:text-center">
        <h2
          class="text-base text-blue-600 font-semibold tracking-wide uppercase"
        >
          特色
        </h2>
        <p
          class="
            mt-2
            text-3xl
            leading-8
            font-extrabold
            tracking-tight
            text-gray-900
            sm:text-4xl
          "
        >
          我們的價值
        </p>
        <p class="mt-4 max-w-2xl text-xl text-gray-500 lg:mx-auto">
          這些是 Climate 所能做到的
        </p>
      </div>

      <div class="mt-10">
        <dl
          class="
            space-y-10
            md:space-y-0 md:grid md:grid-cols-2 md:gap-x-8 md:gap-y-10
          "
        >
          <div class="relative">
            <dt>
              <div
                class="
                  absolute
                  flex
                  items-center
                  justify-center
                  h-12
                  w-12
                  rounded-md
                  bg-blue-500
                  text-white
                "
              >
                <svg
                  class="h-6 w-6"
                  xmlns="http://www.w3.org/2000/svg"
                  fill="none"
                  viewBox="0 0 24 24"
                  stroke="currentColor"
                  aria-hidden="true"
                >
                  <path
                    stroke-linecap="round"
                    stroke-linejoin="round"
                    stroke-width="2"
                    d="M21 12a9 9 0 01-9 9m9-9a9 9 0 00-9-9m9 9H3m9 9a9 9 0 01-9-9m9 9c1.657 0 3-4.03 3-9s-1.343-9-3-9m0 18c-1.657 0-3-4.03-3-9s1.343-9 3-9m-9 9a9 9 0 019-9"
                  />
                </svg>
              </div>
              <p class="ml-16 text-lg leading-6 font-medium text-gray-900">
                高效率的爬蟲系統
              </p>
            </dt>
            <dd class="mt-2 ml-16 text-base text-gray-500">
              Climate 利用了 Scrapy
              框架，提供了高效率的捕捉速度，讓資料能快速的被整理並寫入資料庫內。
            </dd>
          </div>

          <div class="relative">
            <dt>
              <div
                class="
                  absolute
                  flex
                  items-center
                  justify-center
                  h-12
                  w-12
                  rounded-md
                  bg-blue-500
                  text-white
                "
              >
                <svg
                  xmlns="http://www.w3.org/2000/svg"
                  class="h-5 w-5"
                  viewBox="0 0 20 20"
                  fill="currentColor"
                >
                  <path
                    d="M5 3a1 1 0 000 2c5.523 0 10 4.477 10 10a1 1 0 102 0C17 8.373 11.627 3 5 3z"
                  />
                  <path
                    d="M4 9a1 1 0 011-1 7 7 0 017 7 1 1 0 11-2 0 5 5 0 00-5-5 1 1 0 01-1-1zM3 15a2 2 0 114 0 2 2 0 01-4 0z"
                  />
                </svg>
              </div>
              <p class="ml-16 text-lg leading-6 font-medium text-gray-900">
                三種資料來源
              </p>
            </dt>
            <dd class="mt-2 ml-16 text-base text-gray-500">
              我們使用 PTT、Dcard、巴哈姆特
              作為資料來源，進行分析與解構，整理出資料提供使用者閱覽。
            </dd>
          </div>

          <div class="relative">
            <dt>
              <div
                class="
                  absolute
                  flex
                  items-center
                  justify-center
                  h-12
                  w-12
                  rounded-md
                  bg-blue-500
                  text-white
                "
              >
                <svg
                  class="h-6 w-6"
                  xmlns="http://www.w3.org/2000/svg"
                  fill="none"
                  viewBox="0 0 24 24"
                  stroke="currentColor"
                  aria-hidden="true"
                >
                  <path
                    stroke-linecap="round"
                    stroke-linejoin="round"
                    stroke-width="2"
                    d="M13 10V3L4 14h7v7l9-11h-7z"
                  />
                </svg>
              </div>
              <p class="ml-16 text-lg leading-6 font-medium text-gray-900">
                穩定的資料庫系統
              </p>
            </dt>
            <dd class="mt-2 ml-16 text-base text-gray-500">
              我們採用 MongoDB 作為資料庫儲存媒介，作為大數據操作的第一步。
            </dd>
          </div>

          <div class="relative">
            <dt>
              <div
                class="
                  absolute
                  flex
                  items-center
                  justify-center
                  h-12
                  w-12
                  rounded-md
                  bg-blue-500
                  text-white
                "
              >
                <svg
                  xmlns="http://www.w3.org/2000/svg"
                  class="h-6 w-6"
                  fill="none"
                  viewBox="0 0 24 24"
                  stroke="currentColor"
                >
                  <path
                    stroke-linecap="round"
                    stroke-linejoin="round"
                    stroke-width="2"
                    d="M14.828 14.828a4 4 0 01-5.656 0M9 10h.01M15 10h.01M21 12a9 9 0 11-18 0 9 9 0 0118 0z"
                  />
                </svg>
              </div>
              <p class="ml-16 text-lg leading-6 font-medium text-gray-900">
                漂亮的操作介面
              </p>
            </dt>
            <dd class="mt-2 ml-16 text-base text-gray-500">
              我們設計了一個漂亮的圖形介面，透過 HTML 5 呈現我們的資料。
            </dd>
          </div>
        </dl>
      </div>
    </div>
  </div>
  <div
    class="
      mt-10
      mx-auto
      max-w-7xl
      px-4
      sm:mt-12 sm:px-6
      md:mt-16
      lg:mt-20 lg:px-8
      xl:mt-28
    "
  >
    <div class="sm:text-center lg:text-left">
      <h1
        class="
          text-4xl
          tracking-tight
          font-extrabold
          text-gray-900
          sm:text-5xl
          md:text-6xl
        "
      >
        <span class="block xl:inline">持續的</span>
        <span class="block text-blue-600 xl:inline">進步當中</span>
      </h1>
      <p
        class="
          mt-3
          text-base text-gray-500
          sm:mt-5 sm:text-lg sm:max-w-xl sm:mx-auto
          md:mt-5 md:text-xl
          lg:mx-0
        "
      >
        這是一份來自國立高雄科技大學的實驗專案，這是一項實驗項目，用於分析臺灣社群網路趨勢及聲量，類似Google
        Trends，並以開放原始碼的方式呈現。
      </p>
      <div class="mt-5 sm:mt-8 sm:flex sm:justify-center lg:justify-start">
        <div class="rounded-md shadow">
          <a
            href="#"
            class="
              w-full
              flex
              items-center
              justify-center
              px-8
              py-3
              border border-transparent
              text-base
              font-medium
              rounded-md
              text-white
              bg-blue-600
              hover:bg-blue-700
              md:py-4 md:text-lg md:px-10
            "
          >
            一起來幫助我們吧？
          </a>
        </div>
        <div class="mt-3 sm:mt-0 sm:ml-3">
          <a
            href="#"
            class="
              w-full
              flex
              items-center
              justify-center
              px-8
              py-3
              border border-transparent
              text-base
              font-medium
              rounded-md
              text-blue-700
              bg-blue-100
              hover:bg-blue-200
              md:py-4 md:text-lg md:px-10
            "
          >
            聯絡我們
          </a>
        </div>
      </div>
    </div>
  </div>
</div>
`,
};
