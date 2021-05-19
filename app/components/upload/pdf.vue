<template>
  <v-container fluid>
    <h1 class="text-h5 pt-5 pb-16">PDF uploads for the {{ champ }}</h1>
    <v-row>
      <v-col>
        <UiSelect :label="'Year'" :items="years" :item.sync="year" />
      </v-col>
      <v-col>
        <UiSelect :label="'Session'" :items="sessions" :item.sync="session" />
      </v-col>
    </v-row>
    <v-row>
      <v-col>
        <UiSelect :label="'Track'" :items="tracks" :item.sync="track" />
      </v-col>
      <v-col>
        <v-text-field v-model="round" label="Round number" type="number">
        </v-text-field>
      </v-col>
    </v-row>
    <v-row>
      <v-col>
        <UiSelect
          :label="'Weather'"
          :items="weatherTypes"
          :item.sync="weather"
        />
      </v-col>
    </v-row>
    <v-row>
      <v-col>
        <h3 class="text-h5 pb-10">Date</h3>
        <v-date-picker v-model="date"></v-date-picker>
      </v-col>
      <v-col>
        <h3 class="text-h5 pb-10">Time</h3>
        <v-time-picker v-model="time" format="ampm" landscape></v-time-picker>
      </v-col>
    </v-row>
    <v-row class="my-10">
      <v-col>
        <v-file-input
          v-model="file"
          label="PDF file input"
          accept="application/pdf"
          chips
          show-size
        ></v-file-input>
      </v-col>
      <v-col cols="12">
        <v-btn @click.native="check">Upload to database</v-btn>
      </v-col>
    </v-row>
  </v-container>
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
      year: '',
      session: '',
      weather: '',
      track: '',
      time: '',
      round: '',
      date: '',
      file: '',
    }
  },
  methods: {
    upload() {},
    check() {},
  },
}
</script>
