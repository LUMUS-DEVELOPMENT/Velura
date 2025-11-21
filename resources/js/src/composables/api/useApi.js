import {ref} from "vue";

export function useApi() {
    const loading = ref(false)
    const error = ref(null)

    const request = async (method, url, payload = null, config = {}) => {
        loading.value = true
        error.value = null

        try {
            const response = await window.axios({
                method,
                url,
                data: payload,
                ...config
            })

            return response.data

        } catch (err) {
            if (err.response) {
                error.value = err.response.data
            } else if (err.request) {
                error.value = { message: 'No server response' }
            } else {
                error.value = { message: err.message || 'Unknown error' }
            }

            throw error.value
        } finally {
            loading.value = false
        }
    }

    return {
        loading,
        error,
        request,
    }
}
