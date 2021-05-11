<template>
  <div>
    <v-container>
      <h1 class="text-h2 pt-5 pb-16">Create calendar</h1>
      <v-row class="text-center">
        <v-col cols="6" class="pb-5">
          <v-text-field
            v-model.trim="year"
            label="Year"
            :rules="yearRules"
            hide-details="auto"
          ></v-text-field>
        </v-col>
        <v-col class="my-auto"
          ><v-btn color="primary">Track not found ?</v-btn></v-col
        >
      </v-row>
    </v-container>
    <v-row class="pt-5">
      <v-col cols="12">
        <v-simple-table fixed-header height="600px">
          <template #default>
            <thead>
              <tr>
                <th class="text-left">Track</th>
                <th class="text-left">Rounds</th>
                <th class="text-left">Date</th>
                <th class="text-left">Actions</th>
              </tr>
            </thead>
            <tbody>
              <tr v-for="(item, index) in items" :key="index">
                <td><UiSelect :track.sync="item.track"></UiSelect></td>
                <td>
                  <v-text-field
                    v-model.trim="item.rounds"
                    label="e.g 1,2,3"
                    :rules="roundRules"
                  ></v-text-field>
                </td>
                <td><UiDpmenu :date.sync="item.date"></UiDpmenu></td>
                <td>
                  <v-btn fab small @click.native="add">
                    <v-icon color="green"> mdi-plus </v-icon>
                  </v-btn>
                  <v-btn
                    fab
                    small
                    :class="{ hidden: index == 0 }"
                    @click.native="remove(index)"
                  >
                    <v-icon color="red"> mdi-minus </v-icon>
                  </v-btn>
                </td>
              </tr>
            </tbody>
          </template>
        </v-simple-table>
      </v-col>
    </v-row>
  </div>
</template>

<script>
export default {
  data: () => ({
    yearRules: [
      (value) => !!value || 'Required.',
      (value) =>
        (value && Number.isInteger(parseInt(value))) || 'Must be a number',
      (value) => (value || '').length <= 4 || 'Max 4 characters',
    ],
    roundRules: [
      (value) => !!value || 'Required.',
      (value) =>
        (value && Number.isInteger(parseInt(value))) || 'Must be numbers',
      (value) => (value || '').length <= 6 || 'Max 6 characters',
    ],
    year: '',
    items: [
      {
        track: '',
        rounds: '',
        date: '',
      },
    ],
  }),
  methods: {
    add() {
      this.items.push({ track: '', rounds: '', date: '' })
    },
    remove(index) {
      this.items.splice(index, 1)
    },
    create() {
      
    }
  },
}
</script>

<style>
.hidden {
  visibility: hidden;
}
</style>
