export const state = () => ({
  dialog: false,
})

export const mutations = {
  SET_DIALOG: (state, dialog) => {
    state.dialog = dialog
  },
}

export const getters = {
  dialog: (state) => state.dialog,
}
