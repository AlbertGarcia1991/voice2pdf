import { mount } from '@vue/test-utils'
import { describe, it, expect, beforeEach, vi } from 'vitest'
import Pages from '../Pages.vue'
import * as pdfjsLib from 'pdfjs-dist'

// Mock canvas context
const mockContext = {
  drawImage: vi.fn(),
  clearRect: vi.fn(),
  getImageData: vi.fn(),
  putImageData: vi.fn(),
  scale: vi.fn(),
  translate: vi.fn(),
  rotate: vi.fn(),
  save: vi.fn(),
  restore: vi.fn(),
}

// Mock HTMLCanvasElement
HTMLCanvasElement.prototype.getContext = vi.fn(() => mockContext)

let mockPdf: any = null

vi.mock('pdfjs-dist', () => ({
  getDocument: vi.fn(() => ({
    promise: Promise.resolve(mockPdf)
  })),
  GlobalWorkerOptions: {
    workerSrc: ''
  },
  version: '3.11.174',
}))

describe('Pages.vue', () => {
  beforeEach(() => {
    vi.clearAllMocks()
    mockPdf = {
      numPages: 2,
      getPage: vi.fn().mockImplementation(() => ({
        getViewport: () => ({ width: 800, height: 600 }),
        render: vi.fn().mockResolvedValue({})
      }))
    }
  })

  it('renders canvas elements for each page', async () => {
    const wrapper = mount(Pages, {
      props: {
        pdfUrl: 'test.pdf'
      }
    })

    await wrapper.vm.$nextTick()
    await new Promise(resolve => setTimeout(resolve, 0)) // Wait for PDF loading

    const canvases = wrapper.findAll('canvas')
    expect(canvases).toHaveLength(2)
  })

  it('handles PDF loading error', async () => {
    const consoleSpy = vi.spyOn(console, 'error').mockImplementation(() => {})
    const mockError = new Error('Failed to load PDF')
    vi.mocked(pdfjsLib.getDocument).mockReturnValue({
      promise: Promise.reject(mockError)
    })

    const wrapper = mount(Pages, {
      props: {
        pdfUrl: 'test.pdf'
      }
    })

    await wrapper.vm.$nextTick()
    await new Promise(resolve => setTimeout(resolve, 0)) // Wait for PDF loading

    expect(consoleSpy).toHaveBeenCalledWith('Error loading PDF:', mockError)
    consoleSpy.mockRestore()
  })

  it('updates when pdfUrl changes', async () => {
    const wrapper = mount(Pages, {
      props: {
        pdfUrl: 'test.pdf'
      }
    })

    await wrapper.vm.$nextTick()
    await new Promise(resolve => setTimeout(resolve, 0)) // Wait for PDF loading

    // Change the PDF URL
    await wrapper.setProps({ pdfUrl: 'new.pdf' })
    await wrapper.vm.$nextTick()
    await new Promise(resolve => setTimeout(resolve, 0)) // Wait for PDF loading

    expect(pdfjsLib.getDocument).toHaveBeenCalledTimes(2)
  })
})
