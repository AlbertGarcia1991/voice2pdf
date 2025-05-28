import { vi } from 'vitest'
import '@testing-library/jest-dom'

// Mock URL.createObjectURL
vi.stubGlobal('URL', {
  createObjectURL: vi.fn((blob) => `blob:${blob}`),
  revokeObjectURL: vi.fn(),
})

// Mock fetch
global.fetch = vi.fn()

// Mock canvas context
const mockContext = {
  fillRect: vi.fn(),
  clearRect: vi.fn(),
  getImageData: vi.fn(() => ({
    data: new Array(4),
  })),
  putImageData: vi.fn(),
  createImageData: vi.fn(() => []),
  setTransform: vi.fn(),
  drawImage: vi.fn(),
  save: vi.fn(),
  fillText: vi.fn(),
  restore: vi.fn(),
  beginPath: vi.fn(),
  moveTo: vi.fn(),
  lineTo: vi.fn(),
  closePath: vi.fn(),
  stroke: vi.fn(),
  translate: vi.fn(),
  scale: vi.fn(),
  rotate: vi.fn(),
  arc: vi.fn(),
  fill: vi.fn(),
  measureText: vi.fn(() => ({
    width: 0,
  })),
  transform: vi.fn(),
  rect: vi.fn(),
  clip: vi.fn(),
}

const mockCanvas = {
  getContext: vi.fn(() => mockContext),
  toDataURL: vi.fn(),
  height: 0,
  width: 0,
}

// Mock canvas element
vi.stubGlobal('HTMLCanvasElement', {
  prototype: mockCanvas,
})

// Mock getContext
vi.stubGlobal('getContext', vi.fn(() => mockContext))

// Mock ResizeObserver
vi.stubGlobal('ResizeObserver', vi.fn().mockImplementation(() => ({
  observe: vi.fn(),
  unobserve: vi.fn(),
  disconnect: vi.fn(),
})))

// Mock IntersectionObserver
vi.stubGlobal('IntersectionObserver', vi.fn().mockImplementation(() => ({
  observe: vi.fn(),
  unobserve: vi.fn(),
  disconnect: vi.fn(),
})))

// Mock DataTransfer for Node.js environment
global.DataTransfer = class {
  files = [];
  items = {
    add: (file) => this.files.push(file),
    remove: (index) => this.files.splice(index, 1),
    clear: () => { this.files = []; }
  };
}; 