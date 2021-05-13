<template>
  <div>
    <v-row>
      <v-col>
        <v-combobox
          v-model="selected"
          :search-input.sync="search"
          hide-selected
          clearable
          :items="itemList"
          :label="label"
          refs="selection"
          @change="$emit('update:item', selected)"
          @keydown.enter="add($event)"
        >
          <template #no-data>
            <v-list-item>
              <v-list-item-content>
                <v-list-item-title>
                  No results matching "<strong>{{ search }}</strong
                  >". Press <kbd>enter</kbd> to create a new one
                </v-list-item-title>
              </v-list-item-content>
            </v-list-item>
          </template>
        </v-combobox>
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
      selected: '',
      search: null,
    }
  },
  computed: {
    itemList() {
      return this.items
    },
  },
  methods: {
    add(evt) {
      this.itemList.push(evt.target.value)
    },
  },
}
</script>
