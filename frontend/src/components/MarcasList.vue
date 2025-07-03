<template>
  <div class="container">
    <!-- Estado de carga -->
    <div v-if="loading" class="loading">
      <div class="spinner"></div>
      <p>Cargando marcas...</p>
    </div>

    <!-- Estado de error -->
    <div v-else-if="error" class="error">
      <h3>Error al cargar las marcas</h3>
      <p>{{ error }}</p>
      <button @click="fetchMarcas" class="retry-button">
        Reintentar
      </button>
    </div>

    <!-- Contenido principal -->
    <div v-else>
      <div class="header">
        <h2 class="title">Marcas Disponibles</h2>
        <span class="count">{{ marcas.length }} marcas</span>
      </div>

      <div class="grid">
        <div 
          v-for="marca in marcas" 
          :key="marca.id" 
          class="card"
        >
          <div class="card-header">
            <span class="id">#{{ marca.id }}</span>
          </div>
          <div class="card-body">
            <h3 class="nombre">{{ marca.nombre }}</h3>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup lang="ts">
import { ref, onMounted } from 'vue'

// Interfaz TypeScript para las marcas
interface Marca {
  id: number
  nombre: string
}

// Estados reactivos
const marcas = ref<Marca[]>([])
const loading = ref(true)
const error = ref<string | null>(null)

// Función para obtener las marcas
const fetchMarcas = async () => {
  try {
    loading.value = true
    error.value = null
    
    const response = await fetch('http://localhost:5000/marcas/')
    
    if (!response.ok) {
      throw new Error(`Error: ${response.status}`)
    }
    
    const data: Marca[] = await response.json()
    marcas.value = data
  } catch (err) {
    error.value = err instanceof Error ? err.message : 'Error desconocido'
  } finally {
    loading.value = false
  }
}

// Cargar datos al montar el componente
onMounted(() => {
  fetchMarcas()
})
</script>

<style scoped>
.container {
  max-width: 1200px;
  margin: 0 auto;
  padding: 2rem;
  font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif;
}

.header {
  display: flex;
  justify-content: space-between;
  align-items: center;
  margin-bottom: 2rem;
  padding-bottom: 1rem;
  border-bottom: 2px solid #e5e7eb;
}

.title {
  font-size: 2rem;
  font-weight: 700;
  color: #1f2937;
  margin: 0;
}

.count {
  background: #3b82f6;
  color: white;
  padding: 0.5rem 1rem;
  border-radius: 20px;
  font-size: 0.875rem;
  font-weight: 500;
}

.grid {
  display: grid;
  grid-template-columns: repeat(auto-fill, minmax(280px, 1fr));
  gap: 1.5rem;
}

.card {
  background: white;
  border-radius: 12px;
  box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.1), 0 2px 4px -1px rgba(0, 0, 0, 0.06);
  transition: all 0.3s ease;
  overflow: hidden;
  border: 1px solid #e5e7eb;
  cursor: pointer;
}

.card:hover {
  transform: translateY(-4px);
  box-shadow: 0 20px 25px -5px rgba(0, 0, 0, 0.1), 0 10px 10px -5px rgba(0, 0, 0, 0.04);
}

.card-header {
  background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
  padding: 1rem;
  display: flex;
  justify-content: flex-end;
}

.id {
  background: rgba(255, 255, 255, 0.2);
  color: white;
  padding: 0.25rem 0.75rem;
  border-radius: 12px;
  font-size: 0.75rem;
  font-weight: 600;
  backdrop-filter: blur(10px);
}

.card-body {
  padding: 1.5rem;
}

.nombre {
  font-size: 1.25rem;
  font-weight: 600;
  color: #1f2937;
  margin: 0;
  text-align: center;
}

/* Estados de carga y error */
.loading,
.error {
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  padding: 3rem;
  text-align: center;
}

.spinner {
  width: 40px;
  height: 40px;
  border: 4px solid #f3f4f6;
  border-top: 4px solid #3b82f6;
  border-radius: 50%;
  animation: spin 1s linear infinite;
  margin-bottom: 1rem;
}

@keyframes spin {
  0% {
    transform: rotate(0deg);
  }
  100% {
    transform: rotate(360deg);
  }
}

.loading p {
  color: #6b7280;
  font-size: 1.125rem;
  margin: 0;
}

.error {
  color: #dc2626;
}

.error h3 {
  margin: 0 0 0.5rem 0;
  font-size: 1.25rem;
}

.error p {
  margin: 0 0 1rem 0;
  color: #6b7280;
}

.retry-button {
  background: #3b82f6;
  color: white;
  border: none;
  padding: 0.75rem 1.5rem;
  border-radius: 8px;
  font-weight: 500;
  cursor: pointer;
  transition: background-color 0.2s;
}

.retry-button:hover {
  background: #2563eb;
}

/* Responsive */
@media (max-width: 768px) {
  .container {
    padding: 1rem;
  }

  .header {
    flex-direction: column;
    gap: 1rem;
    text-align: center;
  }

  .title {
    font-size: 1.5rem;
  }

  .grid {
    grid-template-columns: 1fr;
  }
}

/* Animaciones para la lista */
.grid {
  animation: fadeIn 0.5s ease-in;
}

@keyframes fadeIn {
  from {
    opacity: 0;
    transform: translateY(20px);
  }
  to {
    opacity: 1;
    transform: translateY(0);
  }
}

.card {
  animation: slideIn 0.3s ease-out;
}

@keyframes slideIn {
  from {
    opacity: 0;
    transform: scale(0.95);
  }
  to {
    opacity: 1;
    transform: scale(1);
  }
}
</style>