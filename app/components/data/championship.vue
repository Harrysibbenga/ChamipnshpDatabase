<template>
  <div>
    <h1 class="text-h5 py-5">Please select a Championship</h1>
    <DataDefault :response.sync="item" :collection="'championships'" />
  </div>
</template>

<script>
export default {
  props: {
    champ: {
      type: String,
      default: '',
    },
  },
  data() {
    return {
      default: '',
    }
  },
  computed: {
    item: {
      get() {
        return this.default
      },
      set(newVal) {
        this.$emit('update:champ', newVal)
      },
    },
  },
}
</script>
