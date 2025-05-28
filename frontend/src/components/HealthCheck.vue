<template>
  <div class="health-check">
    <h2>Backend Health Status</h2>
    <p v-if="loading">Loading...</p>
    <p v-else-if="error">Error: {{ error }}</p>
    <p v-else>Status: {{ status }}</p>
  </div>
</template>

<script>
import { ref, onMounted } from 'vue'

export default {
  name: 'HealthCheck',
  setup() {
    const status = ref('')
    const loading = ref(true)
    const error = ref(null)

    const checkHealth = async () => {
      try {
        const response = await fetch('http://localhost:8000/api/health/')
        const data = await response.json()
        status.value = data.status
      } catch (err) {
        error.value = err.message
      } finally {
        loading.value = false
      }
    }

    onMounted(() => {
      checkHealth()
    })

    return {
      status,
      loading,
      error
    }
  }
}
</script>

<style scoped>
.health-check {
  padding: 20px;
  border-radius: 8px;
  background-color: #f5f5f5;
  margin: 20px;
}
</style> 