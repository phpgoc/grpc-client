<script lang="ts">
    import Header from "$components/Header.svelte";
    import {t,availableLanguages,changeLanguage} from '$module/i18n.svelte';
   

    let selectedLanguage = availableLanguages[0]; // 默认选择第一种语言
    let b = false
    function handleLanguageChange() {
      // window.alert(selectedLanguage);
        console.log (123)
        b = changeLanguage(selectedLanguage)
        count ++
    }
    let count = 0;
</script>

<Header />
<div class="full-width">
  <p class="larger-text"> 选择语言</p>
  <select bind:value={selectedLanguage} >
  {#each availableLanguages as language}
    <option value={language}>{language.toUpperCase()}</option>
  {/each}
  </select>
  {count}
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