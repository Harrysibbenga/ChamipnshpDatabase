<template>
  <v-container>
    <v-toolbar>
      <template #extension>
        <v-tabs v-model="tab" align-with-title>
          <v-tabs-slider color="primary"></v-tabs-slider>

          <v-tab v-for="item in items" :key="item">
            {{ item }}
          </v-tab>
        </v-tabs>
      </template>
    </v-toolbar>

    <v-tabs-items v-model="tab">
      <v-tab-item v-for="item in items" :key="item">
        <v-card v-if="item == 'Create Calendar'" flat>
          <v-card-text>
            <UploadCalendar :champ="champ" />
          </v-card-text>
        </v-card>
        <v-card v-else flat>
          <v-card-text>
            <UploadPdf />
          </v-card-text>
        </v-card>
      </v-tab-item>
    </v-tabs-items>
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
      tab: null,
      items: ['Create Calendar', 'Upload PDF'],
    }
  },
}
</script>
