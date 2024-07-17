<script lang="ts">
    import Header from "$components/Header.svelte";
    import {t} from '$module/i18n.svelte';
    import {Page} from "$lib/types";
</script>

<Header page={Page.Call} />
{t("call")}