<script context="module" lang="ts">
  import { Store } from "tauri-plugin-store-api";

  const store = new Store("./settings.dat");

  export async function Get(key: string): Promise<string | null> {
    return await store.get(key);
  }
  export async function Set(key: string, value: string | null): Promise<void> {
    await store.set(key, value);
  }
</script>
