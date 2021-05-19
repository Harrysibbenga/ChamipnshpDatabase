/* eslint-disable no-useless-catch */
import Cookie from 'js-cookie'
import { auth } from '@/services/firebase'

export const state = () => ({
  user: null,
  admin: false,
})

export const mutations = {
  SET_USER: (state, user) => {
    state.user = user
  },
  SET_ADMIN_USER: (state, admin) => {
    state.admin = admin
  },
}

export const getters = {
  user: (state) => state.user,
  admin: (state) => state.admin,
}

export const actions = {
  async login({ commit }, formdata) {
    try {
      // login user
      await auth.signInWithEmailAndPassword(formdata.email, formdata.password)

      // get jwt from firebase
      const token = await auth.currentUser.getIdToken()
      const { email, uid } = auth.currentUser

      // set jwt to the cookie
      Cookie.set('access_token', token, { expires: 5 })

      commit('SET_USER', { email, uid })
    } catch (error) {
      throw error.message
    }
  },
  // eslint-disable-next-line no-empty-pattern
  async restPass({}, email) {
    try {
      await auth.sendPasswordResetEmail(email)
    } catch (error) {
      throw error.message
    }
  },
}
