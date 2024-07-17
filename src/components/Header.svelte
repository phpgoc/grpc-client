<script>
    import {t} from "$module/i18n.svelte";
  </script>
  
  <div class="flex justify-between p-5 bg-gray-100">
    <a href="/" class="nav-link no-underline text-gray-800 mx-2">{t("index")}</a>
    <a href="/upload" class="nav-link no-underline text-gray-800 mx-2">{t("upload")}</a>
    <a href="/" class="nav-link no-underline text-gray-800 mx-2">{t("call")}</a>
    <a href="/settings" class="nav-link no-underline text-gray-800 mx-2">{t("settings")}</a>
  </div>
  
  <style>
    /* Tailwind CSS 已经包含了大部分所需的样式，如果有特别的样式需求可以在这里添加 */
    .nav-link:hover {
      text-decoration: underline;
    }
  </style>