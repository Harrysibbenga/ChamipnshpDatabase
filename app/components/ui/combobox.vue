<template>
  <div>
    <v-row>
      <v-col>
        <v-combobox
          v-model="selected"
          :search-input.sync="search"
          clearable
          :items="itemList"
          :label="label"
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

        <ModalLogin />
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
    upload: {
      type: Object,
      default: () => ({}),
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
    token() {
      return this.$store.getters['global/token']
    },
  },
  methods: {
    add(evt) {
      // Check if admin user is logged in
      if (this.token) {
        // update upload prop with input data and ststus update
        const data = {
          item: evt.target.value,
          status: true,
        }

        this.$emit('update:upload', data)
      } else {
        // Prompt to login
        this.$store.commit('global/SET_DIALOG', true)
      }
    },
  },
}
</script>
