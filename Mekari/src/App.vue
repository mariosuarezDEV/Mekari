<script lang="ts" setup>
import { RouterLink, RouterView  } from 'vue-router'

</script>

<template>
  <div>
    <!-- Barra de Navegación -->
     <div className="grid grid-cols-2 bg-gray-700 text-white shadow-lg">

      <div>
        <h1 className="font-bold text-2xl p-4">
          Mekari
        </h1>
      </div>

      <div className="flex flex-nowrap gap-10 justify-end items-center mr-10">
        <RouterLink to="/" className="">Dashboard</RouterLink>
        <RouterLink to="/perfil" className="">Mi perfil</RouterLink>
        <RouterLink to="/configuracion" className="">Configuración</RouterLink>
        <RouterLink to="/logout" className="">Cerrar Sesión</RouterLink>
      </div>

     </div>
    <RouterView />
  </div>

</template>
