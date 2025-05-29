import { mount } from '@vue/test-utils'
import { describe, it, expect, vi, beforeEach } from 'vitest'
import HealthCheck from '../HealthCheck.vue'

describe('HealthCheck', () => {
  beforeEach(() => {
    vi.clearAllMocks()
  })

  it('displays loading state initially', () => {
    const wrapper = mount(HealthCheck)
    expect(wrapper.text()).toContain('Loading...')
  })

  it('displays status when API call succeeds', async () => {
    global.fetch = vi.fn().mockResolvedValue({
      ok: true,
      json: () => Promise.resolve({ status: 'ok' })
    })

    const wrapper = mount(HealthCheck)
    await wrapper.vm.$nextTick()
    await new Promise(resolve => setTimeout(resolve, 0)) // Wait for fetch to complete

    expect(wrapper.text()).toContain('Status: ok')
  })

  it('displays error when API call fails', async () => {
    global.fetch = vi.fn().mockRejectedValue(new Error('Network error'))

    const wrapper = mount(HealthCheck)
    await wrapper.vm.$nextTick()
    await new Promise(resolve => setTimeout(resolve, 0)) // Wait for fetch to complete

    expect(wrapper.text()).toContain('Error: Network error')
  })
}) 