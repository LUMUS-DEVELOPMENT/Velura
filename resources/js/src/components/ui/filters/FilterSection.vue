<script setup>
import FilterButton from "@/components/ui/filters/FilterButton.vue";
import FilterInput from "@/components/ui/filters/FilterInput.vue";

defineProps({
  command: String,
  buttonName: String,
  checkboxList: Array
});
</script>

<template>
  <div class="border-t border-gray-200 px-4 py-6">
    <FilterButton :button-name="buttonName" :command="command" />

    <el-disclosure :id="'filter-section-'+command" hidden class="block pt-6">
        <div class="pt-6">
          <div class="space-y-6">
            <FilterInput
                v-for="item in checkboxList"
                :key="item.name"
                :item="item"
            />
          </div>
        </div>
    </el-disclosure>
  </div>

</template>
