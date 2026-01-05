<script setup lang="ts">
import { computed } from 'vue'

const props = defineProps<{
  history: number[]
  isPositive: boolean
}>()

const series = computed(() => [{
  name: 'Price',
  data: props.history
}])

const chartOptions = computed(() => ({
  chart: {
    type: 'line',
    sparkline: { enabled: true },
    animations: { enabled: true },
    parentHeightOffset: 0,
    toolbar: { show: false }
  },
  grid: {
    padding: {
      top: 2,
      right: 0,
      bottom: 2,
      left: 0
    }
  },
  stroke: {
    curve: 'smooth',
    width: 2
  },
  colors: [props.isPositive ? '#10b981' : '#f43f5e'],
  tooltip: { enabled: false },
  markers: { size: 0 }
}))
</script>

<template>
  <div class="h-10 w-full overflow-hidden">
    <apexchart
      type="line"
      height="40"
      :options="chartOptions"
      :series="series"
    />
  </div>
</template>
