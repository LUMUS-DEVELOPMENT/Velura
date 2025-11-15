import {ref} from "vue";

const useCategory = () => ref([
    { name: 'category[]', value: 'new-arrivals' },
    { name: 'category[]', value: 'sale' },
    { name: 'category[]', value: 'travel' },
    { name: 'category[]', value: 'organization' },
    { name: 'category[]', value: 'accessories' }
]);
export default useCategory;