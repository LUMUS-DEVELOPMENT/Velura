<template>
  <div class=" relative flex items-end space-x-1 left-[max-content]">
    <button v-if="current" type="button" class="flex items-center px-3 py-2 text-sm font-medium"
            command="--toggle"
            commandfor="language-menu">
      <span class="h-4 w-4 me-1.5" v-html="current.icon"></span>
      {{ current.label }}
    </button>
    <el-disclosure
        id="language-menu"
        class="absolute top-14 border shadow-lg w-44 bg-white mt-1 rounded-base animate-dropdown"
        hidden>
      <ul class="p-2 text-sm font-medium">
        <LangItem v-for="item in languages" :key="item.code" :language="item"
            :is-active="current && item.code === current.code"
            @select="select"/>
      </ul>
    </el-disclosure>
  </div>
</template>
<script setup>
  import { ref, watch } from "vue";
  import LangItem from "@/components/ui/features/lang/LangItem.vue";
  import useLang from "@/composables/lang/useLang.js";
  import {useRules} from "@/composables/useRules.js";

  const {setFormLang} = useRules();

  const  {languages, currentLang} = useLang().value;

  const emit = defineEmits(["update:modelValue"]);
  const current = ref(null);

  watch(
      () => languages,
      (langs) => {
        if (Array.isArray(langs) && langs.length > 0) {
          current.value = currentLang || langs[0];
        }
      },
      { immediate: true }
  );
  watch(
      () => currentLang,
      (val) => {
        if (val) current.value = val;
      }
  );
  function select(language) {
    current.value = language;
    emit("update:modelValue", language);
    setFormLang(language.code);
  }
</script>
