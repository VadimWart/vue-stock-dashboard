<script setup lang="ts">
import { Card, CardContent } from '@/components/ui/card'
import StockChart from '@/components/dashboard/StockChart.vue'
import type { CompanyMetric } from '@/types/dashboard'

defineProps<CompanyMetric>()
</script>

<template>
  <Card class="bg-slate-900/50 border-slate-800 text-white w-full overflow-hidden">
    <CardContent class="p-4">
      <div class="flex items-center gap-2 mb-3">
        <div class="w-8 h-8 rounded-full bg-white/10 overflow-hidden flex items-center justify-center">
          <img v-if="logoUrl" :src="logoUrl" class="w-full h-full object-contain" />
        </div>
        <span class="text-sm font-medium text-slate-300">{{ name }}</span>
      </div>

      <div class="text-2xl font-bold mb-1">
        {{ revenue }} <span class="text-[20px] text-slate-500 font-bold">$</span>
      </div>

       <StockChart :history="history" :is-positive="isPositive" />

      <div class="flex items-center gap-2">
        <span
          :class="isPositive ? 'text-emerald-400' : 'text-rose-400'"
          class="text-xs font-semibold"
        >
          {{ isPositive ? '↑' : '↓' }} {{ changeValue }}
        </span>
        <span
          :class="
            isPositive ? 'bg-emerald-500/10 text-emerald-400' : 'bg-rose-500/10 text-rose-400'
          "
          class="text-[10px] px-1.5 py-0.5 rounded"
        >
          {{ changePercent }}%
        </span>
      </div>
    </CardContent>
  </Card>
</template>
