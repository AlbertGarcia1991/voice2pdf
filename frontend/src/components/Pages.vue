<template>
  <div class="pages-container">
    <div
      v-for="(canvas, index) in canvases"
      :key="index"
      class="page-wrapper"
    >
      <canvas
        :id="`page-${index + 1}`"
        ref="canvasRefs"
      />
    </div>
  </div>
</template>

<script setup lang="ts">
import { ref, onMounted, watch } from 'vue'
import * as pdfjsLib from 'pdfjs-dist'

// Set the worker source
pdfjsLib.GlobalWorkerOptions.workerSrc = `//cdnjs.cloudflare.com/ajax/libs/pdf.js/${pdfjsLib.version}/pdf.worker.min.js`

const props = defineProps<{
  pdfUrl: string
}>()

const canvasRefs = ref<HTMLCanvasElement[]>([])
const canvases = ref<number[]>([])

const renderPage = async (pdf: pdfjsLib.PDFDocumentProxy, pageNumber: number) => {
  const page = await pdf.getPage(pageNumber)
  const canvas = document.getElementById(`page-${pageNumber}`) as HTMLCanvasElement
  const context = canvas.getContext('2d')

  if (!context) return

  const viewport = page.getViewport({ scale: 1.5 })
  canvas.height = viewport.height
  canvas.width = viewport.width

  const renderContext = {
    canvasContext: context,
    viewport: viewport,
  }

  await page.render(renderContext).promise
}

const loadPDF = async () => {
  try {
    const loadingTask = pdfjsLib.getDocument(props.pdfUrl)
    const pdf = await loadingTask.promise
    const numPages = pdf.numPages

    // Create canvas elements for each page
    canvases.value = Array.from({ length: numPages }, (_, i) => i + 1)

    // Wait for the next tick to ensure canvases are rendered
    await new Promise(resolve => setTimeout(resolve, 0))

    // Render each page
    for (let i = 1; i <= numPages; i++) {
      await renderPage(pdf, i)
    }
  } catch (error) {
    console.error('Error loading PDF:', error)
  }
}

watch(() => props.pdfUrl, (newUrl) => {
  if (newUrl) {
    loadPDF()
  }
})

onMounted(() => {
  if (props.pdfUrl) {
    loadPDF()
  }
})
</script>

<style scoped>
.pages-container {
  display: flex;
  flex-direction: column;
  align-items: center;
  gap: 20px;
  padding: 20px;
}

.page-wrapper {
  box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
  margin-bottom: 20px;
}

canvas {
  display: block;
  max-width: 100%;
  height: auto;
}
</style>
