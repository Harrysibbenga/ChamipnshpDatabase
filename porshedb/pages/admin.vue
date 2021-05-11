<template>
  <section id="admin">
    <v-container id="admin-nav">
      <v-toolbar flat>
        <v-toolbar-title>Admin panel</v-toolbar-title>
        <v-spacer></v-spacer>
        <nuxt-link to="/">
          <v-icon class="mr-1">mdi-home</v-icon>Home
        </nuxt-link>
        <a @click="logout()">
          <v-icon icon="ban" />
          Logout
        </a>
      </v-toolbar>

      <v-tabs center-active color="primary" class="mt-4">
        <v-tab :nuxt="true" to="/admin">Upload data</v-tab>
      </v-tabs>
    </v-container>

    <nuxt-child class="pt-3"></nuxt-child>
  </section>
</template>

<script>
export default {
  layout: 'admin',
}
</script>
