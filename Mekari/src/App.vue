<script lang="ts" setup>
import { RouterLink, RouterView  } from 'vue-router'

</script>

<template>
  <div className="bg-slate-100 h-screen">

    <!-- Barra de Navegación -->
    <div className="flex justify-start items-center gap-10 bg-zinc-900 text-white p-4 shadow-md rounded-bl-xl">

      <h1 className="font-bold text-3xl">Mekari</h1>

      <div className="flex gap-10">
        <RouterLink to="/" >Módulos</RouterLink>
        <RouterLink to="/perfil" >Mi perfil</RouterLink>
        <RouterLink to="/configuracion" >Configuración</RouterLink>
        <RouterLink to="/logout" >Cerrar Sesión</RouterLink>
      </div>

    </div>

    <!-- Contenido -->
    <div className="container mx-auto mt-4 p-2">
      <RouterView />
    </div>

  </div>

</template>
