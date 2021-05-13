<template>
  <v-autocomplete
    v-model="selected"
    hide-selected
    :items="items"
    :label="label"
    filled
    rounded
    solo
    @change="$emit('update:item', selected)"
  ></v-autocomplete>
</template>

<script>
export default {
  props: {
    item: {
      type: String,
      default: '',
    },
    items: {
      type: Array,
      default: () => [],
    },
    label: {
      type: String,
      default: '',
    },
  },
  data() {
    return {
      selected: '',
    }
  },
}
</script>
