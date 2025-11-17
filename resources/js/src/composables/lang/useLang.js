import {ref} from "vue";


import useEn from "@/composables/lang/useEn.js";
import useRu from "@/composables/lang/useRu.js";
import useDe from "@/composables/lang/useDe.js";
import useIt from "@/composables/lang/useIt.js";
import useZn from "@/composables/lang/useZn.js";
const useLang =  () => ref({
    languages: [useEn, useRu,useDe, useIt, useZn],
    currentLang: useEn
});
export default useLang;
