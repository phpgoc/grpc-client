<script lang="ts">
  // import {t} from "$module/i18n.svelte";

  import { Page } from "$lib/types";
  import { t } from "i18next";

  // 使用枚举作为属性类型
  export let page: Page = Page.Index;
</script>

<div class="flex justify-between bg-gray-100 p-5">
  <a
    href="/index"
    class="nav-link mx-2 text-gray-800 no-underline {page === Page.Index
      ? 'active'
      : ''}">{t("index")}</a
  >
  <a
    href="/help"
    class="nav-link mx-2 text-gray-800 no-underline {page === Page.Help
      ? 'active'
      : ''}">{t("help")}</a
  >
  <a
    href="/upload"
    class="nav-link mx-2 text-gray-800 no-underline {page === Page.Upload
      ? 'active'
      : ''}">{t("upload")}</a
  >
  <a
    href="/call"
    class="nav-link mx-2 text-gray-800 no-underline {page === Page.Call
      ? 'active'
      : ''}">{t("call")}</a
  >
  <a
    href="/settings"
    class="nav-link mx-2 text-gray-800 no-underline {page === Page.Settings
      ? 'active'
      : ''}">{t("settings")}</a
  >
</div>

<style>
  .nav-link,
  .active {
    font-weight: 900; /* 加粗3倍，使用最粗的字体权重 */
    font-size: 2em; /* 增大字体大小 */
    width: 80%; /* 设置宽度为容器的80% */
    margin: auto; /* 水平和垂直居中 */
    display: flex; /* 使用flex布局 */
    justify-content: center; /* 水平居中文本 */
    align-items: center; /* 垂直居中文本 */
    text-align: center; /* 确保文本居中对齐 */
  }
  .flex {
    height: 10vh; /* Adjust this value to change the header height */
    justify-content: space-between;
    background-color: #f5f7fa;
    padding: 1vh 0; /* Example padding that also scales with viewport height */
  }

  .nav-link {
    flex-grow: 1; /* Allow each nav-link to grow and fill the container */
    text-align: center; /* Center the text within each nav-link */
    /* Other styles remain unchanged */
  }
  .nav-link:hover {
    text-decoration: underline;
  }
  .active {
    color: #4a90e2; /* Bright blue color for text */
    background-color: #00ff00; /* Light grey background */
    /* Ensure the element does not change the layout */
    margin: 0;
    padding: 0;
    border: none;
  }
</style>
