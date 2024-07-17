<script lang="ts">
    import Header from "$components/Header.svelte";
    import {t } from 'i18next';
    import {availableLanguages,changeLanguage, lang} from "$lib/i18n.ts";
    import {Page} from "$lib/types";
   

    let selectedLanguage = lang; // 默认选择第一种语言
    let b = false
    function handleLanguageChange() {
      // window.alert(selectedLanguage);
        b = changeLanguage(selectedLanguage)
    }
</script>

<Header page={Page.Settings} />
<div class="full-width">
  <p class="larger-text"> 选择语言</p>
  <select bind:value={selectedLanguage} >
  {#each availableLanguages as language}
    <option value={language} selected={language === selectedLanguage} >{language.toUpperCase() }</option>
  {/each}
  </select>
  <button on:click={handleLanguageChange}>确定</button>
</div>

<div class="full-width">
{b}
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