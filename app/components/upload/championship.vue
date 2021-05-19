<template>
  <div>
    <h1 class="text-h5 py-5">Please select a Championship</h1>
    <UiCombobox
      :label="label"
      :item.sync="item"
      :items="items"
      :upload.sync="upload"
    ></UiCombobox>
    <UiMessage :alert="alert" />
  </div>
</template>

<script>
import Cookies from 'js-cookie'
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
      alert: {
        type: 'info',
        message: '',
        hidden: true,
      },
      token: '',
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
          console.log(newVal.item)
        }
      },
    },
  },
  created() {
    this.getChamps()
    this.token = Cookies.get('admin_token')
  },
  methods: {
    add(item) {
      fetch('http://127.0.0.1:8000/api/championships/', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
          Authorization: 'Token ' + this.token,
        },
        body: JSON.stringify({ name: item }),
      })
        .then(() => {
          this.getChamps()
        })
        .catch((error) => {
          this.alert = {
            type: 'error',
            message: error,
            hidden: false,
          }
        })
    },
    getChamps() {
      fetch('http://127.0.0.1:8000/api/championships/', {
        method: 'GET',
      })
        .then((resp) => resp.json())
        .then((resp) => {
          this.championships = resp
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
