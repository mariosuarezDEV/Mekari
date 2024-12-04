<script lang="ts" setup>
import CardModulo from '@/components/CardModulo.vue';
</script>

<template>
  <div className="grid grid-cols-1 md:grid-cols-3 gap-5">
    <h1 className="text-3xl text-zinc-900 text-start font-bold md:col-span-3">
      Módulos de Mekari
    </h1>
    <CardModulo titulo="Recursos Humanos" descripcion=" Simplifica la gestión de tu equipo y mejora la productividad con nuestro módulo de RRHH intuitivo y fácil de usar." ruta="/rrhh" />

  </div>
</template>
