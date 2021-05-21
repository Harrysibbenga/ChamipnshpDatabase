<template>
  <section id="login">
    <v-container class="pt-5">
      <div class="mb-5">
        <NuxtLink to="/" class="d-flex align-items-center mb-2">
          <v-icon class="mr-1" color="secondary"> mdi-home </v-icon>
          <span class="secondary--text">Home</span>
        </NuxtLink>
        <hr class="white" />
      </div>

      <form v-if="!showForgotPassword" @submit.prevent>
        <h3 class="text-center secondary--text my-4">Sign in</h3>
        <v-text-field
          v-model.trim="formdata.email"
          label="Your email"
          type="email"
        ></v-text-field>
        <v-text-field
          v-model.trim="formdata.password"
          label="Your password"
          type="password"
        />
        <div class="text-center py-5">
          <v-btn color="secondary primary--text" @click="login">Login</v-btn>
          <v-btn color="pl-4" @click="togglePasswordReset"
            >Forgot Password</v-btn
          >
        </div>
      </form>

      <form v-if="showForgotPassword" @submit.prevent>
        <div v-if="!passwordResetSuccess">
          <h3 class="text-center secondary--text my-4">Reset Password</h3>
          <h4 class="text-center white--text">
            An email will be sent for you to reset your password
          </h4>

          <v-text-field
            v-model.trim="passwordForm.email"
            label="Your email"
            type="email"
          >
          </v-text-field>

          <div class="text-center py-5">
            <v-btn color="secondary primary--text" @click="resetPassword"
              >Submit</v-btn
            >
            <v-btn class="pl-4" @click="toggleForm">Back to Log In</v-btn>
          </div>
        </div>
        <div v-else>
          <div class="text-center">
            <h3 class="text-center secondary--text my-4">Email sent</h3>
            <v-btn class="py-5" @click="toggleForm">Back to Log In</v-btn>
          </div>
        </div>
      </form>

      <transition name="fade">
        <div
          v-if="isError"
          :class="`error`"
          class="pl-5 mt-2 white--text text-center"
        >
          <p>{{ msg }}</p>
        </div>
      </transition>
    </v-container>
  </section>
</template>

<script>
import { required, email, minLength } from 'vuelidate/lib/validators'

export default {
  data() {
    return {
      formdata: {
        email: 'harry@torquetogether.com',
        password: 'testing123',
      },
      hovered: false,
      passwordForm: {
        email: '',
      },
      showLoginForm: true,
      showForgotPassword: false,
      passwordResetSuccess: false,
      msg: '',
      isError: false,
    }
  },
  validations: {
    formdata: {
      email: {
        required,
        email,
      },
      password: {
        required,
        minLength: minLength(6),
      },
    },
  },
  methods: {
    toggleForm() {
      this.errorMsg = ''
      this.showLoginForm = !this.showLoginForm
      if (this.showForgotPassword) {
        this.showForgotPassword = false
        this.passwordResetSuccess = false
      }
    },
    togglePasswordReset() {
      if (this.showForgotPassword) {
        this.showLoginForm = true
        this.showForgotPassword = false
        this.passwordResetSuccess = false
      } else {
        this.showLoginForm = false
        this.showForgotPassword = true
      }
    },
    login() {
      this.$store
        .dispatch('users/login', this.formdata)
        .then(() => {
          this.$router.push('/admin')
          this.formdata = {
            email: '',
            password: '',
          }
        })
        .catch((error) => {
          this.isError = true
          this.msg = error

          setTimeout(() => {
            this.isError = false
          }, 5000)
        })
    },
    resetPassword() {
      this.performingRequest = true
      this.$store
        .dispatch('users/restPass', this.passwordForm.email)
        .then(() => {
          this.performingRequest = false
          this.passwordResetSuccess = true
          this.passwordForm.email = ''
        })
        .catch((error) => {
          this.isError = true
          this.msg = error

          setTimeout(() => {
            this.isError = false
          }, 5000)
        })
    },
  },
}
</script>
