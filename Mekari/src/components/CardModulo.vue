<script lang="ts" setup>
import { RouterLink  } from 'vue-router'
import { defineProps } from 'vue'
import type { PropsCard } from '../interfaces/PropsCard';
defineProps<PropsCard>()
</script>

<template>
  <div className="bg-white rounded-lg p-4 grid grid-cols-1 gap-2 shadow-lg">
    <h1 className="text-xl font-semibold text-slate-900">
      {{ titulo }}
    </h1>
    <hr>
    <p className="text-slate-900">
      {{ descripcion }}
    </p>
    <RouterLink v-bind:to="ruta" className="flex bg-sky-800 text-white p-2 rounded-md w-full justify-center items-center">Acceder</RouterLink>
  </div>
</template>
