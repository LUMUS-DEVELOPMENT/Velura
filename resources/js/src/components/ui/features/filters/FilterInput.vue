<script setup>
const props = defineProps({
      item: {
            name:String,
            value:String
      }
    });
const emit = defineEmits('change')
</script>
<template>
  <div class="flex gap-3">
    <div class="flex h-5 shrink-0 items-center">
      <div class="group grid size-4 grid-cols-1">
        <input type="checkbox" :id="item.name"  :name="item.name"  :value="item.value"
            class="col-start-1 row-start-1 rounded-sm border-gray-300 checked:bg-indigo-600"
            @change="emit('change', emit.event.target.checked, props.item)" />
        <svg viewBox="0 0 14 14" class="pointer-events-none size-3.5 stroke-white">
          <path d="M3 8L6 11L11 3.5" stroke-width="2" />
        </svg>
      </div>
    </div>
    <label :for="item.name" class="text-gray-500">
      {{ item.value }}
    </label>
  </div>
</template>
