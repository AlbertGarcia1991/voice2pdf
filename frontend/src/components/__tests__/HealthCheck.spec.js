import { mount } from '@vue/test-utils'
import { describe, it, expect, vi, beforeEach } from 'vitest'
import HealthCheck from '../HealthCheck.vue'

describe('HealthCheck', () => {
  beforeEach(() => {
    global.fetch = vi.fn()
  })

  it('displays loading state initially', () => {
    const wrapper = mount(HealthCheck)
    expect(wrapper.text()).toContain('Loading')
  })

  it('displays status when API call succeeds', async () => {
    global.fetch.mockResolvedValueOnce({
      json: () => Promise.resolve({ status: 'ok' })
    })

    const wrapper = mount(HealthCheck)
    await wrapper.vm.$nextTick()
    await wrapper.vm.$nextTick()

    expect(wrapper.text()).toContain('Status: ok')
  })

  it('displays error when API call fails', async () => {
    global.fetch.mockRejectedValueOnce(new Error('Network error'))

    const wrapper = mount(HealthCheck)
    await wrapper.vm.$nextTick()
    await wrapper.vm.$nextTick()

    expect(wrapper.text()).toContain('Error: Network error')
  })
}) 