<template>
  <div class="container">
    <!-- Estado de carga -->
    <div v-if="loading" class="loading">
      <div class="spinner"></div>
      <p>Cargando proveedores...</p>
    </div>

    <!-- Estado de error -->
    <div v-else-if="error" class="error">
      <h3>Error al cargar los proveedores</h3>
      <p>{{ error }}</p>
      <button @click="fetchProveedores" class="retry-button">
        Reintentar
      </button>
    </div>

    <!-- Contenido principal -->
    <div v-else>
      <div class="header">
        <h2 class="title">Proveedores</h2>
        <span class="count">{{ proveedores.length }} proveedores</span>
      </div>

      <div class="grid">
        <div 
          v-for="proveedor in proveedores" 
          :key="proveedor.id" 
          class="card"
        >
          <div class="card-header">
            <span class="id">#{{ proveedor.id }}</span>
          </div>
          
          <div class="card-body">
            <h3 class="nombre">{{ proveedor.nombre }}</h3>
            
            <div class="contact-info">
              <div class="info-item">
                <div class="info-icon">
                  <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
                    <path d="M21 10c0 7-9 13-9 13s-9-6-9-13a9 9 0 0 1 18 0z"></path>
                    <circle cx="12" cy="10" r="3"></circle>
                  </svg>
                </div>
                <span class="info-text">{{ proveedor.direccion }}</span>
              </div>
              
              <div class="info-item">
                <div class="info-icon">
                  <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
                    <path d="M22 16.92v3a2 2 0 0 1-2.18 2 19.79 19.79 0 0 1-8.63-3.07 19.5 19.5 0 0 1-6-6 19.79 19.79 0 0 1-3.07-8.67A2 2 0 0 1 4.11 2h3a2 2 0 0 1 2 1.72 12.84 12.84 0 0 0 .7 2.81 2 2 0 0 1-.45 2.11L8.09 9.91a16 16 0 0 0 6 6l1.27-1.27a2 2 0 0 1 2.11-.45 12.84 12.84 0 0 0 2.81.7A2 2 0 0 1 22 16.92z"></path>
                  </svg>
                </div>
                <a :href="`tel:${proveedor.telefono}`" class="info-text phone-link">
                  {{ formatTelefono(proveedor.telefono) }}
                </a>
              </div>
              
              <div class="info-item">
                <div class="info-icon">
                  <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
                    <path d="M4 4h16c1.1 0 2 .9 2 2v12c0 1.1-.9 2-2 2H4c-1.1 0-2-.9-2-2V6c0-1.1.9-2 2-2z"></path>
                    <polyline points="22,6 12,13 2,6"></polyline>
                  </svg>
                </div>
                <a :href="`mailto:${proveedor.email}`" class="info-text email-link">
                  {{ proveedor.email }}
                </a>
              </div>
            </div>
          </div>
          
          <div class="card-footer">
            <button class="contact-button" @click="contactarProveedor(proveedor)">
              Contactar
            </button>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup lang="ts">
import { ref, onMounted } from 'vue'

// Interfaz TypeScript para los proveedores
interface Proveedor {
  id: number
  nombre: string
  direccion: string
  email: string
  telefono: string
}

// Estados reactivos
const proveedores = ref<Proveedor[]>([])
const loading = ref(true)
const error = ref<string | null>(null)

// Función para obtener los proveedores
const fetchProveedores = async () => {
  try {
    loading.value = true
    error.value = null
    
    const response = await fetch('http://127.0.0.1:5000/proveedores/')
    
    if (!response.ok) {
      throw new Error(`Error: ${response.status}`)
    }
    
    const data: Proveedor[] = await response.json()
    proveedores.value = data
  } catch (err) {
    error.value = err instanceof Error ? err.message : 'Error desconocido'
  } finally {
    loading.value = false
  }
}

// Función para formatear el teléfono
const formatTelefono = (telefono: string): string => {
  // Formato: 11-4455-6677
  if (telefono.length === 10) {
    return `${telefono.slice(0, 2)}-${telefono.slice(2, 6)}-${telefono.slice(6)}`
  }
  return telefono
}

// Función para contactar proveedor
const contactarProveedor = (proveedor: Proveedor) => {
  const mensaje = `Hola ${proveedor.nombre}, me gustaría obtener más información sobre sus servicios.`
  const whatsappUrl = `https://wa.me/54${proveedor.telefono}?text=${encodeURIComponent(mensaje)}`
  window.open(whatsappUrl, '_blank')
}

// Cargar datos al montar el componente
onMounted(() => {
  fetchProveedores()
})
</script>

<style scoped>
.container {
  max-width: 1400px;
  margin: 0 auto;
  padding: 2rem;
  font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif;
  background: #f8fafc;
  min-height: 100vh;
}

.header {
  display: flex;
  justify-content: space-between;
  align-items: center;
  margin-bottom: 2rem;
  padding: 1.5rem;
  background: white;
  border-radius: 16px;
  box-shadow: 0 1px 3px rgba(0, 0, 0, 0.1);
}

.title {
  font-size: 2.5rem;
  font-weight: 800;
  color: #1e293b;
  margin: 0;
  background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
  -webkit-background-clip: text;
  -webkit-text-fill-color: transparent;
  background-clip: text;
}

.count {
  background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
  color: white;
  padding: 0.75rem 1.5rem;
  border-radius: 25px;
  font-size: 0.875rem;
  font-weight: 600;
  box-shadow: 0 4px 15px rgba(102, 126, 234, 0.4);
}

.grid {
  display: grid;
  grid-template-columns: repeat(auto-fill, minmax(380px, 1fr));
  gap: 2rem;
}

.card {
  background: white;
  border-radius: 20px;
  box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.1), 0 2px 4px -1px rgba(0, 0, 0, 0.06);
  transition: all 0.3s ease;
  overflow: hidden;
  border: 1px solid #e2e8f0;
}

.card:hover {
  transform: translateY(-8px);
  box-shadow: 0 25px 50px -12px rgba(0, 0, 0, 0.25);
}

.card-header {
  background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
  padding: 1.25rem;
  display: flex;
  justify-content: flex-end;
}

.id {
  background: rgba(255, 255, 255, 0.25);
  color: white;
  padding: 0.5rem 1rem;
  border-radius: 15px;
  font-size: 0.875rem;
  font-weight: 700;
  backdrop-filter: blur(10px);
  border: 1px solid rgba(255, 255, 255, 0.2);
}

.card-body {
  padding: 2rem;
}

.nombre {
  font-size: 1.5rem;
  font-weight: 700;
  color: #1e293b;
  margin: 0 0 1.5rem 0;
  text-align: center;
}

.contact-info {
  display: flex;
  flex-direction: column;
  gap: 1rem;
}

.info-item {
  display: flex;
  align-items: flex-start;
  gap: 0.75rem;
  padding: 0.75rem;
  background: #f8fafc;
  border-radius: 12px;
  transition: background-color 0.2s;
}

.info-item:hover {
  background: #e2e8f0;
}

.info-icon {
  color: #667eea;
  flex-shrink: 0;
  margin-top: 0.125rem;
}

.info-text {
  color: #475569;
  font-size: 0.875rem;
  line-height: 1.5;
  word-break: break-word;
}

.phone-link,
.email-link {
  text-decoration: none;
  color: #667eea;
  font-weight: 500;
  transition: color 0.2s;
}

.phone-link:hover,
.email-link:hover {
  color: #4f46e5;
  text-decoration: underline;
}

.card-footer {
  padding: 1.5rem 2rem;
  background: #f8fafc;
  border-top: 1px solid #e2e8f0;
}

.contact-button {
  width: 100%;
  background: linear-gradient(135deg, #10b981 0%, #059669 100%);
  color: white;
  border: none;
  padding: 0.875rem 1.5rem;
  border-radius: 12px;
  font-weight: 600;
  font-size: 0.875rem;
  cursor: pointer;
  transition: all 0.2s;
  box-shadow: 0 4px 15px rgba(16, 185, 129, 0.4);
}

.contact-button:hover {
  transform: translateY(-2px);
  box-shadow: 0 8px 25px rgba(16, 185, 129, 0.6);
}

.contact-button:active {
  transform: translateY(0);
}

/* Estados de carga y error */
.loading,
.error {
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  padding: 4rem;
  text-align: center;
  background: white;
  border-radius: 20px;
  margin: 2rem 0;
}

.spinner {
  width: 50px;
  height: 50px;
  border: 4px solid #e2e8f0;
  border-top: 4px solid #667eea;
  border-radius: 50%;
  animation: spin 1s linear infinite;
  margin-bottom: 1.5rem;
}

@keyframes spin {
  0% { transform: rotate(0deg); }
  100% { transform: rotate(360deg); }
}

.loading p {
  color: #64748b;
  font-size: 1.25rem;
  font-weight: 500;
  margin: 0;
}

.error {
  color: #dc2626;
}

.error h3 {
  margin: 0 0 1rem 0;
  font-size: 1.5rem;
  font-weight: 700;
}

.error p {
  margin: 0 0 1.5rem 0;
  color: #64748b;
  font-size: 1rem;
}

.retry-button {
  background: linear-gradient(135deg, #ef4444 0%, #dc2626 100%);
  color: white;
  border: none;
  padding: 0.875rem 2rem;
  border-radius: 12px;
  font-weight: 600;
  cursor: pointer;
  transition: all 0.2s;
  box-shadow: 0 4px 15px rgba(239, 68, 68, 0.4);
}

.retry-button:hover {
  transform: translateY(-2px);
  box-shadow: 0 8px 25px rgba(239, 68, 68, 0.6);
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
    padding: 1rem;
  }

  .title {
    font-size: 2rem;
  }

  .grid {
    grid-template-columns: 1fr;
  }

  .card-body {
    padding: 1.5rem;
  }

  .card-footer {
    padding: 1rem 1.5rem;
  }
}

/* Animaciones */
.grid {
  animation: fadeIn 0.6s ease-out;
}

@keyframes fadeIn {
  from {
    opacity: 0;
    transform: translateY(30px);
  }
  to {
    opacity: 1;
    transform: translateY(0);
  }
}

.card {
  animation: slideUp 0.4s ease-out;
}

@keyframes slideUp {
  from {
    opacity: 0;
    transform: translateY(20px) scale(0.95);
  }
  to {
    opacity: 1;
    transform: translateY(0) scale(1);
  }
}
</style>