import {
    fetchSteps,
    createStep,
    getStep,
    updateStep,
    deleteStep,
} from '../services/steps';

import store from '.';

const steps = {
    state: () => ({
        steps: []
    }),
    mutations: {
        addSteps(state, payload) {
            state.steps = payload.steps
        },
        prependStep(state, payload) {
            state.steps.unshift(payload);
        },
        updateStep(state, payload) {
            const array = state.steps; // [2, 5, 9]

            // console.log(array);

            // const index = array.indexOf(5);
            const index = array.findIndex((element) => element.id === payload.id);
            if(index > -1) {
                state.steps[index] = payload;
            } else {
                state.steps.push(payload);
            }
        },
        removeStep(state, payload) {
            const array = state.steps; // [2, 5, 9]

            // console.log(array);

            // const index = array.indexOf(5);
            const index = array.findIndex((element) => element.id === payload.id);
            if (index > -1) { // only splice array when item is found
                array.splice(index, 1); // 2nd parameter means remove one item only
            }

            // array = [2, 9]
            // console.log(array);

            state.steps = array;
        }
    },
    getters: {
        steps (state) {
            return state.steps
        }
    },
    actions: {
        fetchSteps ({ commit, state }, payload) {            
            // Make a request for a user with a given ID
            fetchSteps(payload)
                .then(function (data) {
                    // handle success
                    console.log(data);

                    commit('addSteps', {
                        // steps: data.results
                        steps: data
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
        createStep ({ commit, state }, payload) {   
            // https://masteringjs.io/tutorials/vue/file-upload
            const formData = new FormData();
            // https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Object/entries
            for (const [key, value] of Object.entries(payload)) {
                // console.log(`${key}: ${value}`);
                if(value == null) { continue; }
                formData.append(key, value);
            }
              
            // Make a request for a user with a given ID
            // createStep(payload)
            createStep(formData)
                .then(function (data) {
                    // handle success
                    console.log(data);
                    // commit('prependStep', data)
                    store.dispatch('showAlert', {title: 'Successfully created!', message: 'step'})
                    store.dispatch('fetchSteps', {})
                })
                .catch(function (error) {
                    // handle error
                    console.log(error);
                    store.dispatch('showAlert', {title: 'Error!', message: 'step'})
                    throw error;
                })
                .finally(function () {
                    // always executed
                });
        },
        updateStep ({ commit, state }, payload) {            
            // https://masteringjs.io/tutorials/vue/file-upload
            const formData = new FormData();
            // https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Object/entries
            for (const [key, value] of Object.entries(payload.data)) {
                // console.log(`${key}: ${value}`);
                if(value == null) { continue; }
                formData.append(key, value);
            }

            // Make a request for a user with a given ID
            // updateStep(payload.id, payload.data)
            updateStep(payload.id, formData)
                .then(function (data) {
                    // handle success
                    console.log(data);
                    commit('updateStep', data)
                    store.dispatch('showAlert', {title: 'Successfully updated!', message: 'step'})
                })
                .catch(function (error) {
                    // handle error
                    console.log(error);
                    store.dispatch('showAlert', {title: 'Error!', message: 'step'})
                    throw error;
                })
                .finally(function () {
                    // always executed
                });
        },
        deleteStep ({ commit, state }, payload) {            
            // Make a request for a user with a given ID
            deleteStep(payload.id)
                .then(function (data) {
                    // handle success
                    console.log(data);
                    commit('removeStep', {id: payload.id})
                    store.dispatch('showAlert', {title: 'Successfully deleted!', message: 'step'})
                })
                .catch(function (error) {
                    // handle error
                    console.log(error);
                    store.dispatch('showAlert', {title: 'Error!', message: 'step'})
                    throw error;
                })
                .finally(function () {
                    // always executed
                });
        }
    }
}

export default steps;