<script setup lang="ts">
import { Card, CardContent } from '@/components/ui/card'

// Hier wird definiert, welche Daten die Karte von außen empfängt
interface Props {
  name: string
  revenue: string
  changeValue: string
  changePercent: string
  isPositive: boolean // Bestimmt, ob es grün oder rot angezeigt wird
}

defineProps<Props>()
</script>

<template>
  <Card class="bg-slate-900/50 border-slate-800 text-white min-w-45 flex-1">
    <CardContent class="p-4">
      <div class="flex items-center gap-2 mb-3">
        <div class="w-5 h-5 rounded-sm bg-blue-500/20 flex items-center justify-center">
          <span class="text-[10px] text-blue-400">●</span>
        </div>
        <span class="text-sm font-medium text-slate-300">{{ name }}</span>
      </div>

      <div class="text-2xl font-bold mb-1">
        {{ revenue }} <span class="text-[10px] text-slate-500 font-normal">In Bill USD</span>
      </div>

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
