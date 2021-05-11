<template>
  <div>
    <v-row>
      <v-col>
        <v-autocomplete
          v-model="item"
          clearable
          :items="items"
          label="Track"
          @change="$emit('update:track', item)"
        ></v-autocomplete>
      </v-col>
    </v-row>
  </div>
</template>

<script>
export default {
  props: {
    track: {
      type: String,
      default: '',
    },
  },
  data: () => ({
    items: ['Foo', 'Bar', 'Fizz', 'Buzz'],
    item: '',
  }),
}
</script>
