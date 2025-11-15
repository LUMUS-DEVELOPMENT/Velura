import {ref} from "vue";


const useSize = () => ref([
    { name: 'size[]', value: '2L' },
    { name: 'size[]', value: '6l' },
    { name: 'size[]', value: '12l' },
    { name: 'size[]', value: '18l' },
    { name: 'size[]', value: '20l' },
    { name: 'size[]', value: '40l' }
]);
export default useSize;