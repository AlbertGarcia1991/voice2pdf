import { mount } from '@vue/test-utils'
import { describe, it, expect, beforeEach, vi } from 'vitest'

// Mock URL.createObjectURL
const mockObjectURL = 'blob:mock-url'
URL.createObjectURL = vi.fn(() => mockObjectURL)
URL.revokeObjectURL = vi.fn()

// Mock Pages component
vi.mock('../Pages.vue', () => ({
  default: {
    name: 'Pages',
    template: '<div class="mock-pages" />',
    props: ['pdfUrl', 'pages']
  }
}))

const flushPromises = async () => {
  for (let i = 0; i < 5; i++) {
    await Promise.resolve()
  }
}

import Upload from '../Upload.vue'

describe('Upload.vue', () => {
  beforeEach(() => {
    vi.clearAllMocks()
    global.fetch = vi.fn()
  })

  it('renders file input', () => {
    const wrapper = mount(Upload)
    expect(wrapper.find('input[type="file"]').exists()).toBe(true)
  })

  it('shows error for non-PDF file', async () => {
    const wrapper = mount(Upload)
    const file = new File(['test'], 'test.txt', { type: 'text/plain' })
    const input = wrapper.find('input[type="file"]').element

    // Set the files property using Object.defineProperty
    Object.defineProperty(input, 'files', {
      value: [file],
      writable: false,
    })
    await wrapper.find('input[type="file"]').trigger('change')
    await wrapper.vm.$nextTick()

    expect(wrapper.text()).toContain('Please select a PDF file')
  })

  it('uploads PDF file successfully', async () => {
    const mockResponse = { upload_id: '123', pages: [] }
    global.fetch = vi.fn().mockResolvedValue({
      ok: true,
      json: () => Promise.resolve(mockResponse)
    })

    const wrapper = mount(Upload)
    const file = new File(['test'], 'test.pdf', { type: 'application/pdf' })
    const input = wrapper.find('input[type="file"]').element

    Object.defineProperty(input, 'files', {
      value: [file],
      writable: false,
    })
    await wrapper.find('input[type="file"]').trigger('change')
    await flushPromises()
    await wrapper.vm.$nextTick()

    // Verify URL.createObjectURL was called
    expect(URL.createObjectURL).toHaveBeenCalledWith(file)

    // Accept both relative and absolute URLs
    const fetchCall = global.fetch.mock.calls[0][0]
    expect([
      '/api/upload/',
      'http://localhost:8000/api/upload/'
    ]).toContain(fetchCall)
    // Check for success message and uploadId
    expect(wrapper.text()).toContain('File uploaded successfully')
    expect(wrapper.text()).toContain('123')
    
    // Verify Pages component is rendered with correct props
    const pagesComponent = wrapper.findComponent({ name: 'Pages' })
    expect(pagesComponent.exists()).toBe(true)
    expect(pagesComponent.props('pdfUrl')).toBe(mockObjectURL)
  })

  it('handles upload failure', async () => {
    global.fetch = vi.fn().mockRejectedValue(new Error('Upload failed'))

    const wrapper = mount(Upload)
    const file = new File(['test'], 'test.pdf', { type: 'application/pdf' })
    const input = wrapper.find('input[type="file"]').element

    Object.defineProperty(input, 'files', {
      value: [file],
      writable: false,
    })
    await wrapper.find('input[type="file"]').trigger('change')
    await wrapper.vm.$nextTick()
    await new Promise(resolve => setTimeout(resolve, 0)) // Wait for upload

    // Accept both error messages
    expect([
      'Error uploading file',
      'Upload failed'
    ].some(msg => wrapper.text().includes(msg))).toBe(true)
    
    // Verify Pages component is not rendered on error
    expect(wrapper.findComponent({ name: 'Pages' }).exists()).toBe(false)
  })
}) 