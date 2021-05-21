<template>
  <div>
    <DataDefault :response.sync="item" :collection="'weather_conditions'" />
  </div>
</template>

<script>
export default {
  props: {
    weather: {
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
        this.$emit('update:weather', newVal)
      },
    },
  },
}
</script>
