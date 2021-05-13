<template>
  <div>
    <h1 class="text-h5 py-5">Please select a Championship</h1>
    <UiCombobox :label="label" :item.sync="item" :items="items"></UiCombobox>
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
      label: 'Championships',
      default: '',
      items: ['Porsche Carrera Cup'],
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
