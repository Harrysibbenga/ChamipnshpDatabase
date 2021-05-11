<template>
  <div>
    <v-container fluid>
      <h1 class="text-h5 pt-5 pb-16">Create calendar</h1>
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
                  <td>
                    <UiSelect
                      :label="'Track'"
                      :item.sync="item.track"
                    ></UiSelect>
                  </td>
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
      <v-row>
        <v-col>
          <v-btn @click.native="create">Create Calendar</v-btn>
        </v-col>
        <v-col>
          <UiMessage :alert="alert"></UiMessage>
        </v-col>
      </v-row>
    </v-container>
  </div>
</template>

<script>
import { calendars } from '@/services/firebase'

export default {
  props: {
    champ: {
      type: String,
      default: '',
    },
  },
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
    alert: {
      type: '',
      message: '',
      hidden: true,
    },
  }),
  methods: {
    add() {
      this.items.push({ track: '', rounds: '', date: '' })
    },
    remove(index) {
      this.items.splice(index, 1)
    },
    create() {
      calendars
        .add({
          year: this.year,
          tracks: this.items,
          champ: this.champ,
        })
        .then(() => {
          this.alert = {
            type: 'success',
            message: 'Calender timetable has been added',
            hidden: false,
          }
          setTimeout(() => {
            this.alert.hidden = true
          }, 5000)
        })
        .catch((error) => {
          this.alert = {
            type: 'error',
            message: error.message,
            hidden: false,
          }
          setTimeout(() => {
            this.alert.hidden = true
          }, 5000)
        })
    },
  },
}
</script>
