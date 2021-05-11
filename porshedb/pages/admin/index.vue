<template>
  <v-container>
    <v-row>
      <v-col cols="12">
        <UploadChampionship :champ.sync="champ"></UploadChampionship>
      </v-col>
      <v-col v-if="champ" cols="12">
        <UploadNav :champ="champ"></UploadNav>
      </v-col>
    </v-row>
  </v-container>
</template>

<script>
export default {
  data() {
    return {
      champ: '',
    }
  },
}
</script>
