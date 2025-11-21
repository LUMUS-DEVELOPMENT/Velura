import {useApi} from "./useApi.js"
export function useProductApi() {
    const {request, loading, error} = useApi()

    const getAll = () => request('GET', '/api/products')
    const getById = (id) => request('GET', `/api/products/${id}`)



    return {
        loading,
        error,
        getAll,
        getById,
    }
}
