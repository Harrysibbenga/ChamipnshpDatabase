<template>
  <div>
    <DataDefault :response.sync="item" :collection="'tracks'" />
  </div>
</template>

<script>
export default {
  props: {
    track: {
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
        this.$emit('update:track', newVal)
      },
    },
  },
}
</script>
