<script lang="ts">
    import Header from "$components/Header.svelte";
    
    import {Page} from "$lib/types";
    import {Set,Get} from "$module/store.svelte"
    import { onMount } from "svelte";
    let url : string = "";
    let download_path : string = "";
    onMount(async () => {
         url = await Get("url");
         download_path  = await Get("download_path");
    });
    function handUrl(){
        Set("url",url);
    }
    function handleDownloadPath(){
        Set("download_path",download_path);
    }
</script>
<Header page={Page.Index}/>

<div class="full-width">
    <p class="larger-text"> 调用地址</p>
    <input type="text" bind:value={url} placeholder="请输入调用地址"/>

    <button on:click={handUrl}>确定</button>
</div>
<div class="full-width">
    <p class="larger-text"> 下载根路径</p>
    <input  bind:value={download_path} placeholder="请输入下载根路径"/>
    <button on:click={handleDownloadPath}>确定</button>
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