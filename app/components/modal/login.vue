<template>
  <v-row justify="center">
    <v-dialog v-model="dialog" persistent max-width="600px">
      <v-card>
        <v-card-title>
          <span class="headline">Super Admin login</span>
        </v-card-title>
        <v-card-subtitle>
          You need to login as a super user to acsses the database.
        </v-card-subtitle>
        <v-card-text>
          <v-container class="my-3">
            <v-row>
              <v-col cols="12">
                <v-text-field
                  v-model.trim="username"
                  label="Your username"
                  type="text"
                ></v-text-field>
              </v-col>
              <v-col cols="12">
                <v-text-field
                  v-model.trim="password"
                  label="Your password"
                  type="password"
                />
              </v-col>
            </v-row>
          </v-container>
        </v-card-text>
        <UiMessage :alert="alert"></UiMessage>
        <v-card-actions>
          <v-spacer></v-spacer>
          <v-btn color="red darken-1" text @click="close"> Close </v-btn>
          <v-btn color="blue darken-1" text @click="login"> Login </v-btn>
        </v-card-actions>
      </v-card>
    </v-dialog>
  </v-row>
</template>

<script>
import Cookie from 'js-cookie'

export default {
  data: () => ({
    // dialog: true,
    username: '',
    password: '',
    alert: {
      type: '',
      hidden: true,
      message: '',
    },
  }),
  computed: {
    dialog() {
      return this.$store.getters['global/dialog']
    },
  },
  methods: {
    login() {
      fetch('http://127.0.0.1:8000/auth/', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify({
          username: this.username,
          password: this.password,
        }),
      })
        .then((resp) => resp.json())
        .then((res) => {
          const token = res.token
          // set jwt to the cookie
          Cookie.set('admin_token', token, { expires: 1 })
        })
        .then(() => {
          this.alert = {
            type: 'success',
            hidden: false,
            message: this.username + ' Logged in',
          }
          setTimeout(() => {
            this.close()
          }, 3000)
        })
        .catch((error) => {
          this.alert = {
            type: 'error',
            hidden: false,
            message: error,
          }
        })
    },
    close() {
      this.username = ''
      this.password = ''
      this.$store.commit('global/SET_DIALOG', false)
    },
  },
}
</script>
