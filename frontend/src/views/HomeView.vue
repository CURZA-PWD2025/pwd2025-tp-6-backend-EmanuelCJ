<template>
  <header>
    <nav>
      <ul>
        <li><router-link to="/">Inicio</router-link></li>
        <li><router-link to="/marcas">Marcas</router-link></li>
        <li><router-link to="/articulos">Artículos</router-link></li>
        <li><router-link to="/categorias">Categorías</router-link></li>
        <li><router-link to="/proveedores">Proveedores</router-link></li>
      </ul>
    </nav>
  </header>
  <main>
    <router-view></router-view>
  </main>
  <footer>
    <p>&copy; 2025 Emanuel C. J.</p>
  </footer>
</template>

<script setup lang="ts">

</script>

<style scoped>

</style>