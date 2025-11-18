<script setup>
defineOptions({ name: 'NavItem' })
defineProps({
  id: { type: String, default: null },
  label: String,
  menuId: String,
  menuData: Object,
});
</script>
<template>
  <div class="group/popover flex">
    <div class="relative flex">
      <button :popovertarget="menuId" class="relative flex items-center justify-center text-sm font-medium group-not-has-open/popover:text-gray-700  group-has-open/popover:text-indigo-600  group-not-has-open/popover:hover:text-gray-800">
        {{ label }}
      </button>
    </div>
    <el-popover :id="menuId" anchor="bottom" popover class="w-full overflow-visible bg-white text-sm text-gray-500">
      <MegaMenu :menuData="menuData"/>
    </el-popover>
  </div>
</template>
