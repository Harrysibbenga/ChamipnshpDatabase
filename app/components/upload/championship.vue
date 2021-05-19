<template>
  <div>
    <h1 class="text-h5 py-5">Please select a Championship</h1>
    <UiCombobox
      :label="label"
      :item.sync="item"
      :items="items"
      :data="'championship'"
    ></UiCombobox>
  </div>
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
      label: 'Championships',
      default: '',
      championships: [],
    }
  },
  computed: {
    item: {
      get() {
        return this.default
      },
      set(newVal) {
        this.$emit('update:champ', newVal)
      },
    },
    items() {
      const items = []

      this.championships.forEach((champ) => {
        items.push(champ.name)
      })

      return items
    },
  },
  created() {
    fetch('http://127.0.0.1:8000/api/championships/', {
      method: 'GET',
      headers: {
        Authorization: 'Token 5d7b6dae64bce8b2a2d6ba1d5693eee4c2ed2140',
      },
    })
      .then((resp) => resp.json())
      .then((resp) => {
        this.championships = resp
        console.log(resp)
      })
      .catch((error) => console.log(error))
  },
}
</script>
