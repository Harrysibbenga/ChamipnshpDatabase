<template>
  <v-col>
    <v-menu
      ref="menu"
      v-model="menu"
      :close-on-content-click="false"
      :return-value.sync="selectDate"
      transition="scale-transition"
      offset-y
      min-width="auto"
    >
      <template #activator="{ on, attrs }">
        <v-text-field
          v-model="selectDate"
          label="Picker in menu"
          prepend-icon="mdi-calendar"
          readonly
          v-bind="attrs"
          v-on="on"
        >
        </v-text-field>
      </template>
      <v-date-picker v-model="selectDate" no-title scrollable>
        <v-spacer></v-spacer>
        <v-btn text color="primary" @click="menu = false"> Cancel </v-btn>
        <v-btn text color="primary" @click="save(selectDate)"> OK </v-btn>
      </v-date-picker>
    </v-menu>
  </v-col>
</template>

<script>
export default {
  props: {
    date: {
      type: String,
      required: true,
    },
  },
  data: () => ({
    selectDate: new Date().toISOString().substr(0, 10),
    menu: false,
  }),
  methods: {
    save() {
      this.$emit('update:date', this.selectDate)
      this.$refs.menu.save(this.selectDate)
    },
  },
}
</script>
