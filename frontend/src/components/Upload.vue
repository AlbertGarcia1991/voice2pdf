<template>
  <div class="upload-container">
    <input
      type="file"
      accept="application/pdf"
      @change="handleFileSelect"
      class="file-input"
    />
    <div v-if="error" class="error">{{ error }}</div>
    <div v-if="uploadId" class="success">
      File uploaded successfully! Upload ID: {{ uploadId }}
    </div>
    <Pages v-if="pdfUrl" :pdf-url="pdfUrl" />
  </div>
</template>

<script setup lang="ts">
import { ref } from 'vue'
import Pages from './Pages.vue'

const uploadId = ref<string | null>(null)
const error = ref<string | null>(null)
const pdfUrl = ref<string | null>(null)

const handleFileSelect = async (event: Event) => {
  const input = event.target as HTMLInputElement
  if (!input.files?.length) return

  const file = input.files[0]
  if (file.type !== 'application/pdf') {
    error.value = 'Please select a PDF file'
    return
  }

  const formData = new FormData()
  formData.append('file', file)

  try {
    const response = await fetch('http://localhost:8000/api/upload/', {
      method: 'POST',
      body: formData,
    })

    if (!response.ok) {
      throw new Error('Upload failed')
    }

    const data = await response.json()
    uploadId.value = data.upload_id
    error.value = null
    
    // Create a blob URL for the PDF
    pdfUrl.value = URL.createObjectURL(file)
  } catch (err) {
    error.value = err instanceof Error ? err.message : 'Upload failed'
    uploadId.value = null
  }
}
</script>

<style scoped>
.upload-container {
  padding: 20px;
  max-width: 800px;
  margin: 0 auto;
}

.file-input {
  display: block;
  margin-bottom: 20px;
  padding: 10px;
  border: 2px dashed #ccc;
  border-radius: 4px;
  width: 100%;
}

.error {
  color: #dc3545;
  margin-bottom: 10px;
}

.success {
  color: #28a745;
  margin-bottom: 10px;
}
</style> 