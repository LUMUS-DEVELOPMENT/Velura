import {ref} from "vue";

const useWomen = () =>ref({
    Clothing: [
        { name: 'Tops', path: '/#' },
        { name: 'Dresses', path: '#' },
        { name: 'Pants', path: '#' },
    ],
    Accessories: [
        { name: 'Watches', path: '#' },
        { name: 'Bags', path: '#' },
    ],
    Brands: [
        { name: 'Full Nelson', path: '#' },
        { name: 'My Way', path: '#' },
    ],
});
export default useWomen;