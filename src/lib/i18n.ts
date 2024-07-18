import i18next from "i18next";
import { createI18nStore } from "svelte-i18next";
import en from "$i18n/en.json";
import zh from "$i18n/zh.json";

import {Get , Set} from "$module/store.svelte";

export let lang: string="zh" ;

export  async function initializeI18next() {
  lang = await Get("lang") || "zh";
  await i18next.init({
    lng: lang,
    resources: {
      en: {
        translation: en,
      },
      zh: {
        translation: zh,
      },
    },
    interpolation: {
      escapeValue: false, // not needed for svelte as it escapes by default
    },
  });
}

export default () => createI18nStore(i18next);

export const availableLanguages = ["en", "zh"];

export  async function changeLanguage(i_lang: string):Promise< boolean> {
  i18next.language = i_lang;
  console.log(i18next.language);
   await  Set("lang", i_lang);
  return i_lang == "en";
}
