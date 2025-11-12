<script setup>
import UlComponent from "@/components/ui/Ul-component.vue";
import LiComponent from "@/components/ui/Li-component.vue";
import FilterCheckBox from "@/components/utils/Filter-CheckBox.vue";

defineProps({
  links:{
    type: Array,
    required: true,
  },
  filterCheckBoxParams:[
    {
      command:{
        type: String,
        required: true
      },
      buttonName:{
        type:String,
        required:true
      },
      checkboxList:{
        type:Array,
        required:true
      }
    }
  ]
})
</script>
<template>
  <form class="hidden lg:block">
    <h3 class="sr-only">Categories</h3>
    <UlComponent className="space-y-4 border-b border-gray-200 pb-6 text-sm font-medium text-gray-900">
      <LiComponent :links="links" />
    </UlComponent>
    <FilterCheckBox
        v-for="item in filterCheckBoxParams"
        :command="item.command"
        :button-name="item.buttonName"
        :checkbox-list="item.checkboxList"
    />
  </form>
</template>