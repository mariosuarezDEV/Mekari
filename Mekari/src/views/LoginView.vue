<script lang="ts">
export default{
  data: () => ({
    title: 'Loign de Mekari'
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
  <div>
    <h1>{{ title }}</h1>
    <button v-on:click="saludar">
      Saludar
    </button>
  </div>
</template>
