const institutions = {
    state: () => ({
        showAlert: false,
        title: '',
        message: '',
        status: '',
    }),
    mutations: {
        showAlert (state, payload) {
            state.showAlert = true;
            state.title = payload.title;
            state.message = payload.message;
            state.status = payload.status;
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
        status (state) {
            return state.status
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