<script lang="ts" setup>
import { ref } from 'vue';
import { RouterLink } from 'vue-router';
import CardModulo from '../components/CardModulo.vue';

const incidencias = ref(["Incidencia 1", "Incidencia 2", "Incidencia 3", "Incidencia 4", "Incidencia 5"]);

</script>


<template>
  <div className="grid grid-cols-1 md:grid-cols-3 gap-5">
    <!-- Contenido del componente -->
    <h1 className="text-3xl text-zinc-900 text-start font-bold md:col-span-3">
        Panel de Recursos Humanos
    </h1>

    <!-- Vista principal -->
    <div className="grid grid-cols-3 md:col-span-3 p-4 gap-4">

      <div className="col-span-3 md:col-span-1 bg-white p-4 rounded-lg shadow-sm gap-4">
        <h1 className="text-2xl font-bold text-zinc-900">
          Ultimas incidencias registradas
        </h1>
        <div className="mt-2 mb-4">
          <!-- Lista de la ultimas incidencias-->
          <ul>
            <!-- Sino hay incidencias poner "No hay incidencias registradas por hoy"-->
            <li v-if="incidencias.length == 0" className="text-zinc-900">No hay incidencias registradas por hoy</li>
            <!-- Si hay incidencias mostrarlas-->
            <div v-else>
              <li v-for="incidencia in incidencias" v-bind:key="incidencia" className="text-zinc-900 border-b p-2">{{ incidencia }}</li>
            </div>
          </ul>
        </div>
        <RouterLink to="/rrhh/incidencias" className="bg-zinc-900 text-white p-2 rounded-md w-full justify-center items-center">Consultar todas las incidencias</RouterLink>
      </div>

      <div className="col-span-3 md:col-span-2 bg-white p-4 rounded-lg shadow-sm gap-4">
        <h1 className="text-2xl font-bold text-zinc-900">
          Empleados Activos
        </h1>
      </div>

    </div>
    <!-- Apartado de modulos-->
    <CardModulo titulo="Gestión de empleados" ruta="/rrhh/empleados"></CardModulo>
    <CardModulo titulo="Tabla de incidencias" ruta="/rrhh/incidencias"></CardModulo>
    <CardModulo titulo="Consultar contratos" ruta="/rrhh/conratos"></CardModulo>
    <CardModulo titulo="Nueva entrevista de trabajo" ruta="/rrhh/entrevista"></CardModulo>
    <CardModulo titulo="Pago de nominas" ruta="/rrhh/nomina"></CardModulo>
    <CardModulo titulo="Lógica de la empresa" ruta="/rrhh/empresa"></CardModulo>
  </div>
</template>
