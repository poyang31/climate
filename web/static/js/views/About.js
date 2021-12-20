export default {
  name: "About",
  data: () => ({
    author: {
      name: "Po-Yang Chen",
      website: "https://github.com/poyang31"
    },
    contributors: [
      {
        name: "arymax",
        website: "https://github.com/arymax"
      },
      {
        name: "a789363",
        website: "https://github.com/a789363"
      }
    ]
  }),
  template: `
  <div class="bg-white shadow overflow-hidden sm:rounded-lg">
  <div class="px-4 py-5 sm:px-6">
    <h3 class="text-lg leading-6 font-medium text-gray-900">Climate</h3>
    <p class="mt-1 max-w-2xl text-sm text-gray-500">
      臺灣網際網路聲量分析儀
    </p>
  </div>
  <div class="border-t border-gray-200">
    <dl>
      <div class="bg-gray-50 px-4 py-5 sm:grid sm:grid-cols-3 sm:gap-4 sm:px-6">
        <dt class="text-sm font-medium text-gray-500">開發代號</dt>
        <dd class="mt-1 text-sm text-gray-900 sm:mt-0 sm:col-span-2">
          hw_2021_12
        </dd>
      </div>
      <div class="bg-white px-4 py-5 sm:grid sm:grid-cols-3 sm:gap-4 sm:px-6">
        <dt class="text-sm font-medium text-gray-500">儲存庫</dt>
        <dd class="mt-1 text-sm text-gray-900 sm:mt-0 sm:col-span-2">
          <a href="https://github.com/poyang31/hw_2021_12"
            >https://github.com/poyang31/hw_2021_12</a
          >
        </dd>
      </div>
      <div class="bg-gray-50 px-4 py-5 sm:grid sm:grid-cols-3 sm:gap-4 sm:px-6">
        <dt class="text-sm font-medium text-gray-500">開發者</dt>
        <dd class="mt-1 text-sm text-gray-900 sm:mt-0 sm:col-span-2">
          {{ author.name }} (<a
            :href="author.website"
            v-text="author.website"
          />)
        </dd>
      </div>
      <div class="bg-white px-4 py-5 sm:grid sm:grid-cols-3 sm:gap-4 sm:px-6">
        <dt class="text-sm font-medium text-gray-500">貢獻者</dt>
        <dd class="mt-1 text-sm text-gray-900 sm:mt-0 sm:col-span-2">
          <ul
            role="list"
            class="border border-gray-200 rounded-md divide-y divide-gray-200"
          >
            <li
              v-for="(i, j) in contributors"
              :key="j"
              class="pl-3 pr-4 py-3 flex items-center justify-between text-sm"
            >
              <div class="w-0 flex-1 flex items-center">
                <svg
                  xmlns="http://www.w3.org/2000/svg"
                  class="flex-shrink-0 h-6 w-6 text-gray-400"
                  fill="none"
                  viewBox="0 0 24 24"
                  stroke="currentColor"
                >
                  <path
                    stroke-linecap="round"
                    stroke-linejoin="round"
                    stroke-width="2"
                    d="M16 7a4 4 0 11-8 0 4 4 0 018 0zM12 14a7 7 0 00-7 7h14a7 7 0 00-7-7z"
                  />
                </svg>
                <span class="ml-2 flex-1 w-0 truncate">
                  {{ i.name }} (<a :href="i.website" v-text="i.website" />)
                </span>
              </div>
            </li>
          </ul>
        </dd>
      </div>
      <div class="bg-gray-50 px-4 py-5 sm:grid sm:grid-cols-3 sm:gap-4 sm:px-6">
        <dt class="text-sm font-medium text-gray-500">授權</dt>
        <dd class="mt-1 text-sm text-gray-900 sm:mt-0 sm:col-span-2">
          <a href="https://git.io/JD9T3">MIT License</a>
        </dd>
      </div>
      <div class="bg-white px-4 py-5 sm:grid sm:grid-cols-3 sm:gap-4 sm:px-6">
        <dt class="text-sm font-medium text-gray-500">版權宣告</dt>
        <dd class="mt-1 text-sm text-gray-900 sm:mt-0 sm:col-span-2">
          &copy; 2021 Po-Yang Chen(https://github.com/poyang31) 版權所有
        </dd>
      </div>
    </dl>
  </div>
</div>
  `,
};
