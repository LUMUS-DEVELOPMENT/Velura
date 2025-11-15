import {ref} from "vue";
const useLinks = ()=>ref([
    { name: 'Tops', path: '#' },
    { name: 'Backpacks', path: '#' },
    { name: 'Travel Bags', path: '#' },
    { name: 'Hip Bags', path: '#' },
    { name: 'Laptop Sleeves', path: '#' },
])

export default useLinks;