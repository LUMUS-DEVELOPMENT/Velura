
<script setup>
defineProps({
  command:{
    type: String,
    required: true
  },
  buttonName: {
    type: String,
    required: true
  },
  checkboxList:{
    type: Array,
    required: true,
  }
})

</script>
<template>
  <div class="border-t border-gray-200 px-4 py-6">
    <h3 class="-mx-2 -my-3 flow-root">
      <button type="button" command="--toggle" :commandfor="'filter-section-'+command"
              class="flex w-full items-center justify-between bg-white px-2 py-3 text-gray-400 hover:text-gray-500">
        <span class="font-medium text-gray-900">{{buttonName}}</span>
        <span class="ml-6 flex items-center">
                    <svg viewBox="0 0 20 20" fill="currentColor" data-slot="icon" aria-hidden="true"
                         class="size-5 in-aria-expanded:hidden">
                      <path
                          d="M10.75 4.75a.75.75 0 0 0-1.5 0v4.5h-4.5a.75.75 0 0 0 0 1.5h4.5v4.5a.75.75 0 0 0 1.5 0v-4.5h4.5a.75.75 0 0 0 0-1.5h-4.5v-4.5Z"/>
                    </svg>
                    <svg viewBox="0 0 20 20" fill="currentColor" data-slot="icon" aria-hidden="true"
                         class="size-5 not-in-aria-expanded:hidden">
                      <path d="M4 10a.75.75 0 0 1 .75-.75h10.5a.75.75 0 0 1 0 1.5H4.75A.75.75 0 0 1 4 10Z"
                            clip-rule="evenodd" fill-rule="evenodd"/>
                    </svg>
                  </span>
      </button>
    </h3>
    <el-disclosure :id="'filter-section-'+command" hidden class="block pt-6">
      <div  class="space-y-6">
        <div v-for="item in checkboxList" class="flex gap-3">
          <div class="flex h-5 shrink-0 items-center">
            <div class="group grid size-4 grid-cols-1">
              <input id="filter-mobile-size-0" type="checkbox" :name="item.name" :value="item.value"
                     class="col-start-1 row-start-1 appearance-none rounded-sm border border-gray-300 bg-white checked:border-indigo-600 checked:bg-indigo-600 indeterminate:border-indigo-600 indeterminate:bg-indigo-600 focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-indigo-600 disabled:border-gray-300 disabled:bg-gray-100 disabled:checked:bg-gray-100 forced-colors:appearance-auto"/>
              <svg viewBox="0 0 14 14" fill="none"
                   class="pointer-events-none col-start-1 row-start-1 size-3.5 self-center justify-self-center stroke-white group-has-disabled:stroke-gray-950/25">
                <path d="M3 8L6 11L11 3.5" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"
                      class="opacity-0 group-has-checked:opacity-100"/>
                <path d="M3 7H11" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"
                      class="opacity-0 group-has-indeterminate:opacity-100"/>
              </svg>
            </div>
          </div>
          <label for="filter-mobile-size-0" class="min-w-0 flex-1 text-gray-500">{{item.value}}</label>
        </div>
      </div>
    </el-disclosure>
  </div>
</template>