<script setup>
defineProps({
  buttonName: String,
  command: String
});
</script>
<template>
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
</template>
