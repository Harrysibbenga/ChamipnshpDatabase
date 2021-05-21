<template>
  <v-container fluid>
    <h1 class="text-h5 pt-5 pb-16">PDF uploads for the {{ champ }}</h1>
    <v-row>
      <v-col>
        <DataYear :year.sync="year" />
      </v-col>
      <v-col>
        <DataSession :session.sync="session" />
      </v-col>
    </v-row>
    <v-row>
      <v-col>
        <DataTrack :track.sync="track" />
      </v-col>
      <v-col>
        <v-text-field v-model="round" label="Round number" type="number">
        </v-text-field>
      </v-col>
    </v-row>
    <v-row>
      <v-col>
        <DataWeather :weather.sync="weather" />
      </v-col>
      <v-col>
        <DataRoad :road.sync="road" />
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
      <UiMessage :alert="alert" />
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
      road: '',
      alert: {
        type: 'info',
        message: '',
        hidden: true,
      },
    }
  },
  computed: {
    token() {
      return this.$store.getters['global/token']
    },
  },
  methods: {
    upload() {
      const formData = new FormData()
      formData.append('file', this.file)
      formData.append('year', this.year)
      formData.append('champ', this.champ)
      formData.append('track', this.track)
      formData.append('session', this.session)
      formData.append('round_number', this.round)
      formData.append('road', this.road)
      formData.append('weather', this.weather)
      formData.append('date', this.date)
      formData.append('time', this.time)

      fetch('http://127.0.0.1:8000/api/upload/file/', {
        method: 'POST',
        headers: {
          Authorization: 'Token ' + this.token,
        },
        body: formData,
      })
        .then((resp) => resp.json())
        .then((res) => {
          this.alert = {
            type: 'success',
            message: res.message,
            hidden: false,
          }
        })
        .catch((error) => {
          this.alert = {
            type: 'error',
            message: error.message,
            hidden: false,
          }
        })
    },
    checkNull(list) {
      let empty = false
      for (let i = 0; i < list.length - 1; i++) {
        if (list[i] === null || list[i] === '') {
          this.alert = {
            type: 'error',
            message:
              'Missing variables please make sure all the information is filled',
            hidden: false,
          }
          empty = true
          break
        }
      }
      if (!empty) {
        this.upload()
      }
    },
    check() {
      if (!this.token) {
        // Prompt to login
        this.$store.commit('global/SET_DIALOG', true)
      } else {
        const items = [
          this.weather,
          this.track,
          this.time,
          this.round,
          this.date,
          this.file,
          this.road,
          this.session,
          this.champ,
        ]
        this.checkNull(items)
      }
    },
  },
}
</script>
