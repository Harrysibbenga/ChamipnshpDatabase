<template>
  <div>
    <DataDefault :response.sync="item" :collection="'sessions'" />
  </div>
</template>

<script>
export default {
  props: {
    session: {
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
        this.$emit('update:session', newVal)
      },
    },
  },
}
</script>
