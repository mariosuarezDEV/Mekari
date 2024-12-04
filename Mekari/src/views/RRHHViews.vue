<script lang="ts">
export default {
  data: () => ({

  }),
  methods:{
    //Metodos
    saludar(){
      alert('Hola');
    }
  }
}
</script>


<template>
  <div className="grid grid-cols-1 md:grid-cols-3 gap-5">
    <!-- Contenido del componente -->
     <h1 className="text-3xl text-slate-900 text-start font-bold md:col-span-3">
        Panel de Recursos Humanos
     </h1>
  </div>
</template>
