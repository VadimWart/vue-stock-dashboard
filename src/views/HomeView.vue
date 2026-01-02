<script setup lang="ts">
import MetricCard from '@/components/dashboard/MetricCard.vue'

// Später kommen diese Daten aus einem Store oder einer API
const companies = [
  { name: 'Apple', revenue: '38.52', changeValue: '1.06', changePercent: '2.83', isPositive: true },
  {
    name: 'Meta',
    revenue: '435.57',
    changeValue: '5.81',
    changePercent: '1.32',
    isPositive: false,
  },
  {
    name: 'Amazon',
    revenue: '127.09',
    changeValue: '3.45',
    changePercent: '2.79',
    isPositive: true,
  },
  {
    name: 'Microsoft',
    revenue: '52.87',
    changeValue: '0.98',
    changePercent: '1.89',
    isPositive: true,
  },
  {
    name: 'Google',
    revenue: '76.03',
    changeValue: '2.15',
    changePercent: '2.91',
    isPositive: false,
  },
  { name: 'Tesla', revenue: '24.32', changeValue: '1.12', changePercent: '4.82', isPositive: true },
  {
    name: 'Nvidia',
    revenue: '13.51',
    changeValue: '0.67',
    changePercent: '5.21',
    isPositive: false,
  },
]
</script>

<template>
  <div class="flex flex-wrap gap-4">
    <MetricCard v-for="company in companies" :key="company.name" v-bind="company" />
  </div>
</template>
