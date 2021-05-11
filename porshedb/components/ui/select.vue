<template>
  <div>
    <v-row>
      <v-col>
        <v-autocomplete
          v-model="selection"
          clearable
          :items="items"
          :label="label"
          @change="$emit('update:item', selection)"
        ></v-autocomplete>
      </v-col>
    </v-row>
  </div>
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
      selection: '',
    }
  },
}
</script>
