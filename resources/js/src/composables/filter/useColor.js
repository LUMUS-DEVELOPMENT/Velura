import {ref} from "vue";


const useColor = () => ref([
    { name: 'color[]', value: 'white' },
    { name: 'color[]', value: 'beige' },
    { name: 'color[]', value: 'blue' },
    { name: 'color[]', value: 'brown' },
    { name: 'color[]', value: 'green' },
    { name: 'color[]', value: 'purple' }
]);
export default useColor;