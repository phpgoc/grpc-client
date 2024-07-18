// Tauri doesn't have a Node.js server to do proper SSR
// so we will use adapter-static to prerender the app (SSG)
// See: https://beta.tauri.app/start/frontend/sveltekit/ for more info
import adapter from "@sveltejs/adapter-static";
import { vitePreprocess } from "@sveltejs/vite-plugin-svelte";
import path from "path";

/** @type {import('@sveltejs/kit').Config} */
const config = {
  preprocess: vitePreprocess(),
  kit: {
    adapter: adapter(),

    alias: {
      $components: path.resolve("./src/components"),
      $config: path.resolve("./src/config"),
      $module: path.resolve("./src/module"),
      $i18n: path.resolve("./src/i18n"),
    },
  },
  compilerOptions: {
    errorMode: "throw",
  },
};

export default config;
