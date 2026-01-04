<script setup lang="ts">
import { RouterView } from 'vue-router'
</script>

<template>
  <div class="min-h-screen bg-slate-950 text-slate-50 p-6 font-sans">

    <header class="mb-8">
      <h1 class="text-2xl font-bold tracking-tight">Stocks Live Tracker</h1>
    </header>

    <main>
      <RouterView />
    </main>

  </div>
</template>

<style>

body {
  margin: 0;
  background-color: #020617;
}
</style>
