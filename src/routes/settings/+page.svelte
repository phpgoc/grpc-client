<script lang="ts">
  import Header from "$components/Header.svelte";
  import { t } from "i18next";
  import { availableLanguages, changeLanguage, lang } from "$lib/i18n";

  import { Page } from "$lib/types";
  import { goto } from "$app/navigation";

  let selectedLanguage = lang;
  function handleLanguageChange() {
    // window.alert(selectedLanguage);
    changeLanguage(selectedLanguage).then(() => {
      goto("/?r=_settings");
    });
  }
</script>

<Header page={Page.Settings} />
<div class="full-width">
  <p class="larger-text">{t("please_select")}</p>
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
