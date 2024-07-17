<script lang="ts">
    import Header from "$components/Header.svelte";
    import {t} from 'i18next';
    import {Page} from "$lib/types";
</script>

<Header page={Page.Upload} />
{t("upload")}