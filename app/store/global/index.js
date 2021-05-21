export const state = () => ({
  dialog: false,
  token: null,
})

export const mutations = {
  SET_DIALOG: (state, dialog) => {
    state.dialog = dialog
  },
  SET_TOKEN: (state, token) => {
    state.token = token
  },
}

export const getters = {
  dialog: (state) => state.dialog,
  token: (state) => state.token,
}
