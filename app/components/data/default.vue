<template>
  <div>
    <UiCombobox
      :label="col"
      :item.sync="item"
      :items="items"
      :upload.sync="upload"
    ></UiCombobox>
    <UiMessage :alert="alert" />
  </div>
</template>

<script>
export default {
  props: {
    response: {
      type: String,
      default: '',
    },
    collection: {
      type: String,
      default: '',
    },
  },
  data() {
    return {
      default: '',
      data: [],
      alert: {
        type: 'info',
        message: '',
        hidden: true,
      },
    }
  },
  computed: {
    item: {
      get() {
        return this.default
      },
      set(newVal) {
        this.$emit('update:response', newVal)
      },
    },
    items() {
      const items = []

      this.data.forEach((item) => {
        items.push(item.name)
      })

      return items
    },
    col() {
      return this.collection.charAt(0).toUpperCase() + this.collection.slice(1)
    },
    token() {
      return this.$store.getters['global/token']
    },
    upload: {
      get() {
        const upload = {
          status: false,
          item: '',
        }
        return upload
      },
      set(newVal) {
        if (newVal.status === true) {
          this.add(newVal.item)
        }
      },
    },
  },
  created() {
    this.getData()
  },
  methods: {
    add(item) {
      fetch('http://127.0.0.1:8000/api/' + this.collection + '/', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
          Authorization: 'Token ' + this.token,
        },
        body: JSON.stringify({ name: item }),
      })
        .then(() => {
          this.getData()
        })
        .catch((error) => {
          this.alert = {
            type: 'error',
            message: error,
            hidden: false,
          }
        })
    },
    getData() {
      fetch('http://127.0.0.1:8000/api/' + this.collection + '/', {
        method: 'GET',
      })
        .then((resp) => resp.json())
        .then((res) => {
          this.data = res
        })
        .catch((error) => {
          this.alert = {
            type: 'error',
            message: error,
            hidden: false,
          }
        })
    },
  },
}
</script>
