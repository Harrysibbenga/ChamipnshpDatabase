<template>
  <div>
    <DataDefault :response.sync="item" :collection="'road_conditions'" />
  </div>
</template>

<script>
export default {
  props: {
    road: {
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
        this.$emit('update:road', newVal)
      },
    },
  },
}
</script>
