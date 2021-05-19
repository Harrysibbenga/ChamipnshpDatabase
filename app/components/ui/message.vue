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
        type: 'info',
        hidden: true,
        messege: '',
      }),
    },
  },
  watch: {
    alert(val) {
      if (val.hidden === false) {
        setTimeout(() => {
          // eslint-disable-next-line vue/no-mutating-props
          this.alert.hidden = true
        }, 5000)
      }
    },
  },
}
</script>
