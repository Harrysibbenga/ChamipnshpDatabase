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
import Cookies from 'js-cookie'
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
    data: {
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
    admin() {
      return this.$store.getters['users/admin']
    },
  },
  methods: {
    add(evt) {
      // Check if admin user is logged in
      console.log(this.admin)
      console.log(Cookies.get('admin_token'))
      if (this.admin) {
        // add data to database
        console.log('Item added', evt.target.value)
        // this.itemList.push(evt.target.value)
      } else {
        // Prompt to login
        this.$store.commit('global/SET_DIALOG', true)
      }
      // if (this.data === 'championship') {

      // }
    },
  },
}
</script>
