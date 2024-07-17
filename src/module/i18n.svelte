<script context="module" lang="ts">
    import i18next from 'i18next';
    import {Set,Get} from "$module/store.svelte"

    import en from "$i18n/en.json";
    import zh from "$i18n/zh.json";
    export let lang : string = await Get("lang");
    if (lang == null) {
        lang = "zh";
        await Set("lang","zh");
    }
    i18next.init({
        lng: lang,
        resources: {
            en: {translation: en},
            zh: {translation: zh}
        }
    });
    
  
    export const availableLanguages = ['en', 'zh'];
  
    export function changeLanguage(i_lang: string): boolean {
        i18next.language = i_lang
        console.log(i18next.language);
        Set("lang",i_lang);
        return i_lang == "en"
    }
  
    export function t(key: string): string {
      return i18next.t(key);
    }
  </script>