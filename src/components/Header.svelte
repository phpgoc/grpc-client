<script lang="ts">

    // import {t} from "$module/i18n.svelte";

    import {Page} from "$lib/types";
    import {t} from "i18next"

  // 使用枚举作为属性类型
  export let page: Page = Page.Index;

</script>
  
  <div class="flex justify-between p-5 bg-gray-100">
  <a href="/" class="nav-link no-underline text-gray-800 mx-2 {page === Page.Index ? 'active' : ''}">{t("index")}</a>
  <a href="/upload" class="nav-link no-underline text-gray-800 mx-2 {page === Page.Upload ? 'active' : ''}">{t("upload")}</a>
  <a href="/call" class="nav-link no-underline text-gray-800 mx-2 {page === Page.Call ? 'active' : ''}">{t("call")}</a>
  <a href="/settings" class="nav-link no-underline text-gray-800 mx-2 {page === Page.Settings ? 'active' : ''}">{t("settings")}</a>
</div>
  
<style>
    /* Tailwind CSS 已经包含了大部分所需的样式，如果有特别的样式需求可以在这里添加 */
    .nav-link:hover {
      text-decoration: underline;
    }
    .active {
  color: #4a90e2; /* Bright blue color for text */
  background-color: #f5f7fa; /* Light grey background */
  padding: 10px;
  border-radius: 5px;
  box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1); /* Subtle shadow for depth */
}
</style>