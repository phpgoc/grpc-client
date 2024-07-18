<script lang="ts">
  import Header from "$components/Header.svelte";
  import { t } from "i18next";
  import { availableLanguages, changeLanguage, lang } from "$lib/i18n";

  import { Page } from "$lib/types";
  import { goto } from "$app/navigation";

  let selectedLanguage = lang; // 默认选择第一种语言
  function handleLanguageChange() {
    // window.alert(selectedLanguage);
    changeLanguage(selectedLanguage).then(() => {
      goto("/?r=_settings");
    });
  }
</script>

<Header page={Page.Settings} />
<div class="full-width">
  <p class="larger-text">选择语言</p>
  <select bind:value={selectedLanguage}>
    {#each availableLanguages as language}
      <option value={language} selected={language === selectedLanguage}
        >{language.toUpperCase()}</option
      >
    {/each}
  </select>
  <button on:click={handleLanguageChange}>{t("confirm")}</button>
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
  select {
    width: 33%; /* Set width to 1/3 of the parent container */
    padding: 8px; /* Optional: Adjust padding for better visual appearance */
    margin: 0 auto; /* Center the select element if the parent container allows */
    /* Add any additional styling here */
  }
</style>
