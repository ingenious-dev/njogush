const institutions = {
    state: () => ({
        showAlert: false,
        title: '',
        message: '',
    }),
    mutations: {
        showAlert (state, payload) {
            state.showAlert = true;
            state.title = payload.title;
            state.message = payload.message;
        },
        closeAlert (state, payload) {
            state.showAlert = false;
        },
    },
    getters: {
        showAlert (state) {
            return state.showAlert
        },
        title (state) {
            return state.title
        },
        message (state) {
            return state.message
        },
    },
    actions: {
        showAlert ({ commit, state }, payload) {            
            commit('showAlert', payload)
        },
        closeAlert ({ commit, state }, payload) {            
            commit('closeAlert')
        },
    }
}

export default institutions;