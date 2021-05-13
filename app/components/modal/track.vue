<template>
  <v-row justify="center">
    <v-dialog v-model="dialog" persistent max-width="600px">
      <template #activator="{ on, attrs }">
        <v-btn color="primary" dark v-bind="attrs" v-on="on">
          Track not found ?
        </v-btn>
      </template>
      <v-card>
        <v-card-title>
          <span class="headline">Add new track information</span>
        </v-card-title>
        <v-card-text>
          <v-container>
            <v-row>
              <v-col cols="12" class="mt-5">
                <v-text-field
                  v-model="name"
                  label="Track name*"
                  required
                ></v-text-field>
              </v-col>
            </v-row>
          </v-container>
          <small>*indicates required field</small>
        </v-card-text>
        <UiMessage :alert="alert"></UiMessage>
        <v-card-actions>
          <v-spacer></v-spacer>
          <v-btn color="blue darken-1" text @click="close"> Close </v-btn>
          <v-btn color="blue darken-1" text @click="check"> Save </v-btn>
        </v-card-actions>
      </v-card>
    </v-dialog>
  </v-row>
</template>

<script>
import { tracks } from '@/services/firebase'

export default {
  data: () => ({
    dialog: false,
    name: '',
    alert: {
      type: '',
      hidden: true,
      message: '',
    },
  }),
  methods: {
    create() {
      tracks
        .add({
          name: this.name,
        })
        .then(() => {
          this.alert = {
            type: 'success',
            hidden: false,
            message: 'Track name added',
          }
          setTimeout(() => {
            this.close()
          }, 5000)
        })
        .catch((error) => {
          this.alert = {
            type: 'error',
            hidden: false,
            message: error.message,
          }
        })
    },
    check() {
      if (this.name !== '') {
        this.create()
      } else {
        this.alert = {
          type: 'error',
          hidden: false,
          message: 'Name cannot be blank',
        }
      }
    },
    close() {
      this.name = ''
      this.dialog = false
    },
  },
}
</script>
