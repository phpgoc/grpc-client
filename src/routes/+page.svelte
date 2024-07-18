<script lang="ts">
  import { onMount } from "svelte";
  import { initializeI18next } from "$lib/i18n";
  import { goto } from "$app/navigation";
  import { page } from "$app/stores";
  $: r = $page.url.searchParams.get("r") || "_index";

  console.log(r);
  onMount(async () => {
    await initializeI18next();
    r = r.replace("_", "/");
    goto(r);
  });
</script>

r={r}
