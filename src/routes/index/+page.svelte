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
  <div class="larger-text">{t("grpc_base_url")}</div>
  <input type="text" bind:value={url} placeholder={t("grpc_base_url")} />

  <button on:click={handUrl}>{t("confirm")}</button>
</div>
<div class="full-width">
  <div class="larger-text">{t("download_root")}</div>
  <input bind:value={download_path} placeholder={t("download_root")} />
  <button on:click={handleDownloadPath}>{t("confirm")}</button>
</div>

<style>
  .full-width > div.larger-text {
    flex-basis: 25%; /* 分配固定的空间给div.larger-text */
    flex-grow: 0; /* 防止div.larger-text根据内容大小扩展 */
    flex-shrink: 0; /* 防止div.larger-text根据内容大小缩小 */
    font-size: 150%; /* 比其他元素大50% */
    margin-right: 10px; /* 添加右边距以避免元素紧挨着 */
  }

  .full-width > input {
    flex-grow: 1; /* 允许<input>元素填充剩余空间 */
    flex-basis: 0%; /* 从0开始扩展，以填充剩余空间 */
    margin-right: 10px; /* 添加右边距以避免元素紧挨着 */
  }

  .full-width > button {
    flex-basis: 15%; /* 分配固定的空间给<button> */
    flex-grow: 0; /* 防止<button>根据内容大小扩展 */
    flex-shrink: 0; /* 防止<button>根据内容大小缩小 */
  }
</style>
