<template>
  <div>
    <a-input v-model:value="time" placeholder="Basic usage" />
  </div>
</template>>
<script lang="ts">
import { defineComponent } from 'vue'
export default defineComponent({
  data () {
    return {
      time: 0
    }
  }
})
</script>