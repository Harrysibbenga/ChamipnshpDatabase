<template>
  <div>
    <v-alert :type="alert.type" :class="{ hidden: alert.hidden }">
      {{ alert.message }}
    </v-alert>
  </div>
</template>

<script>
export default {
  props: {
    alert: {
      type: Object,
      default: () => ({
        type: '',
        hidden: true,
        messege: '',
      }),
    },
  },
}
</script>
