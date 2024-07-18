<script lang="ts">
  import Header from "$components/Header.svelte";

  import { Page } from "$lib/types";
  import { Set, Get } from "$module/store.svelte";
  import { onMount } from "svelte";
  import { t } from "i18next";

  let url: string | null = "";
  let download_path: string | null = "";
  onMount(async () => {
    url = await Get("url");
    download_path = await Get("download_path");
  });
  function handUrl() {
    Set("url", url);
  }
  function handleDownloadPath() {
    Set("download_path", download_path);
  }
</script>

<Header page={Page.Index} />

<div class="full-width">
  <p class="larger-text">{t("grpc_base_url")}</p>
  <input type="text" bind:value={url} placeholder={t("grpc_base_url")} />

  <button on:click={handUrl}>{t("confirm")}</button>
</div>
<div class="full-width">
  <p class="larger-text">{t("download_root")}</p>
  <input bind:value={download_path} placeholder={t("download_root")} />
  <button on:click={handleDownloadPath}>{t("confirm")}</button>
</div>

<style>
  .full-width {
    display: flex;
    justify-content: space-between; /* 使子元素横向铺满整个窗口 */
    align-items: center; /* 垂直居中 */
    width: 100%;
    padding: 0 15% 0 1%;
    margin-bottom: 30px;
  }
  .larger-text {
    font-size: 150%; /* 比其他元素大50% */
  }
</style>
