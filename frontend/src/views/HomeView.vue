<script setup lang="ts">
import { ref, onMounted } from 'vue'
import MetricCard from '@/components/dashboard/MetricCard.vue'
import type { CompanyMetric } from '@/types/dashboard'

// State-Variablen für die Firmen-Daten und den Ladezustand
const companies = ref<CompanyMetric[]>([])
const loading = ref(true)

// Daten vom Backend abrufen, wenn die Komponente gemountet wird
onMounted(async () => {
  try {
    const response = await fetch('http://localhost:8000/api/metrics')
    if (!response.ok) {
      throw new Error('Netzwerk-Antwort war nicht ok')
    }
    // Daten setzen
    companies.value = await response.json()
  } catch (error) {
    console.error('Fehler beim Abrufen der Daten:', error)
  } finally {
    loading.value = false
  }
})
</script>

<template>
  <div class="p-6">

    <div v-if="loading" class="text-slate-400 animate-pulse">
      Fetching live market data...
    </div>

    <div class="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-3 xl:grid-cols-4 gap-4" v-else>
      <MetricCard v-for="company in companies" :key="company.symbol" v-bind="company" />
    </div>
  </div>
</template>
