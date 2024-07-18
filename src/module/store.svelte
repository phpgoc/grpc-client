<script context="module" lang="ts">
  import { Store } from "tauri-plugin-store-api";

  const store = new Store("d:/settings.dat");

  export function Get(key: string): Promise<string> {
    return store.get(key) as Promise<string>;
  }
  export function Set(key: string, value: string): Promise<void> {
    return store.set(key, value);
  }
</script>
