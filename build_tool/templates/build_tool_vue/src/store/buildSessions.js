import {
    fetchBuildSessions,
    createBuildSession,
    getBuildSession,
    updateBuildSession,
    deleteBuildSession,
} from '../services/buildSessions';

import store from '.';

const buildSessions = {
    state: () => ({
        buildSessions: []
    }),
    mutations: {
        addBuildSessions(state, payload) {
            state.buildSessions = payload.buildSessions
        },
        prependBuildSession(state, payload) {
            state.buildSessions.unshift(payload);
        },
        updateBuildSession(state, payload) {
            const array = state.buildSessions; // [2, 5, 9]

            // console.log(array);

            // const index = array.indexOf(5);
            const index = array.findIndex((element) => element.id === payload.id);
            if(index > -1) {
                state.buildSessions[index] = payload;
            } else {
                state.buildSessions.push(payload);
            }
        },
        removeBuildSession(state, payload) {
            const array = state.buildSessions; // [2, 5, 9]

            // console.log(array);

            // const index = array.indexOf(5);
            const index = array.findIndex((element) => element.id === payload.id);
            if (index > -1) { // only splice array when item is found
                array.splice(index, 1); // 2nd parameter means remove one item only
            }

            // array = [2, 9]
            // console.log(array);

            state.buildSessions = array;
        }
    },
    getters: {
        buildSessions (state) {
            return state.buildSessions
        }
    },
    actions: {
        fetchBuildSessions ({ commit, state }, payload) {            
            // Make a request for a user with a given ID
            fetchBuildSessions(payload)
                .then(function (data) {
                    // handle success
                    console.log(data);

                    commit('addBuildSessions', {
                        buildSessions: data.results
                    })
                })
                .catch(function (error) {
                    // handle error
                    console.log(error);
                    throw error;
                })
                .finally(function () {
                    // always executed
                });
        },
        getBuildSession ({ commit, state }, payload) {            
            // Make a request for a user with a given ID
            getBuildSession(payload.id)
                .then(function (data) {
                    // handle success
                    console.log(data);

                    commit('updateBuildSession', data)
                })
                .catch(function (error) {
                    // handle error
                    console.log(error);
                    throw error;
                })
                .finally(function () {
                    // always executed
                });
        },
        createBuildSession ({ commit, state }, payload) {   
            // https://masteringjs.io/tutorials/vue/file-upload
            const formData = new FormData();
            // https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Object/entries
            for (const [key, value] of Object.entries(payload)) {
                // console.log(`${key}: ${value}`);
                formData.append(key, value);
            }
              
            // Make a request for a user with a given ID
            // createBuildSession(payload)
            createBuildSession(formData)
                .then(function (data) {
                    // handle success
                    console.log(data);
                    // commit('prependBuildSession', data)
                    store.dispatch('showAlert', {title: 'Successfully created!', message: 'step', status: 'success'})
                    store.dispatch('fetchBuildSessions', {project: payload.project})
                })
                .catch(function (error) {
                    // handle error
                    console.log(error);
                    store.dispatch('showAlert', {title: 'Error!', message: error.message, status: 'error'})
                    throw error;
                })
                .finally(function () {
                    // always executed
                });
        },
        updateBuildSession ({ commit, state }, payload) {            
            // https://masteringjs.io/tutorials/vue/file-upload
            const formData = new FormData();
            // https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Object/entries
            for (const [key, value] of Object.entries(payload.data)) {
                // console.log(`${key}: ${value}`);
                if(!value) { continue; }
                formData.append(key, value);
            }

            // Make a request for a user with a given ID
            // updateBuildSession(payload.id, payload.data)
            updateBuildSession(payload.id, formData)
                .then(function (data) {
                    // handle success
                    console.log(data);
                    commit('updateBuildSession', data)
                    store.dispatch('showAlert', {title: 'Successfully updated!', message: 'step', status: 'success'})
                })
                .catch(function (error) {
                    // handle error
                    console.log(error);
                    store.dispatch('showAlert', {title: 'Error!', message: error.message, status: 'success', status: 'error'})
                    throw error;
                })
                .finally(function () {
                    // always executed
                });
        },
        deleteBuildSession ({ commit, state }, payload) {            
            // Make a request for a user with a given ID
            deleteBuildSession(payload.id)
                .then(function (data) {
                    // handle success
                    console.log(data);
                    commit('removeBuildSession', {id: payload.id})
                    store.dispatch('showAlert', {title: 'Successfully deleted!', message: 'step', status: 'success'})
                })
                .catch(function (error) {
                    // handle error
                    console.log(error);
                    store.dispatch('showAlert', {title: 'Error!', message: error.message, status: 'error'})
                    throw error;
                })
                .finally(function () {
                    // always executed
                });
        }
    }
}

export default buildSessions;