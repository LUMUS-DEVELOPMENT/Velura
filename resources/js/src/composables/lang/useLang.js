import {ref} from "vue";


import useEn from "@/composables/lang/useEn.js";
import useDe from "@/composables/lang/useDe.js";
import useIt from "@/composables/lang/useIt.js";
import useZn from "@/composables/lang/useZn.js";
const useLang =  () => ref({
    languages: [useEn, useDe, useIt, useZn],
    currentLang: useEn
});
export default useLang;
