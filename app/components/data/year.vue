<template>
  <div>
    <DataDefault :response.sync="item" :collection="'years'" />
  </div>
</template>

<script>
export default {
  props: {
    year: {
      type: Object,
      default: () => ({}),
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
        this.$emit('update:year', newVal)
      },
    },
  },
}
</script>
