import {
    fetchAssets,
    createAsset,
    getAsset,
    updateAsset,
    deleteAsset,
} from '../services/assets';

import store from '.';

const assets = {
    state: () => ({
        assets: []
    }),
    mutations: {
        addAssets(state, payload) {
            state.assets = payload.assets
        },
        prependAsset(state, payload) {
            state.assets.unshift(payload);
        },
        updateAsset(state, payload) {
            const array = state.assets; // [2, 5, 9]

            // console.log(array);

            // const index = array.indexOf(5);
            const index = array.findIndex((element) => element.id === payload.id);
            if(index > -1) {
                state.assets[index] = payload;
            } else {
                state.assets.push(payload);
            }
        },
        removeAsset(state, payload) {
            const array = state.assets; // [2, 5, 9]

            // console.log(array);

            // const index = array.indexOf(5);
            const index = array.findIndex((element) => element.id === payload.id);
            if (index > -1) { // only splice array when item is found
                array.splice(index, 1); // 2nd parameter means remove one item only
            }

            // array = [2, 9]
            // console.log(array);

            state.assets = array;
        }
    },
    getters: {
        assets (state) {
            return state.assets
        }
    },
    actions: {
        fetchAssets ({ commit, state }, payload) {            
            // Make a request for a user with a given ID
            fetchAssets(payload)
                .then(function (data) {
                    // handle success
                    console.log(data);

                    commit('addAssets', {
                        // assets: data.results
                        assets: data
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
        createAsset ({ commit, state }, payload) {   
            // https://masteringjs.io/tutorials/vue/file-upload
            const formData = new FormData();
            // https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Object/entries
            for (const [key, value] of Object.entries(payload)) {
                // console.log(`${key}: ${value}`);
                if(value == null) { continue; }
                formData.append(key, value);
            }
              
            // Make a request for a user with a given ID
            // createAsset(payload)
            createAsset(formData)
                .then(function (data) {
                    // handle success
                    console.log(data);
                    // commit('prependAsset', data)
                    store.dispatch('showAlert', {title: 'Successfully created!', message: 'asset'})
                    store.dispatch('fetchAssets', {})
                })
                .catch(function (error) {
                    // handle error
                    console.log(error);
                    store.dispatch('showAlert', {title: 'Error!', message: 'asset'})
                    throw error;
                })
                .finally(function () {
                    // always executed
                });
        },
        updateAsset ({ commit, state }, payload) {            
            // https://masteringjs.io/tutorials/vue/file-upload
            const formData = new FormData();
            // https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Object/entries
            for (const [key, value] of Object.entries(payload.data)) {
                // console.log(`${key}: ${value}`);
                if(value == null) { continue; }
                formData.append(key, value);
            }

            // Make a request for a user with a given ID
            // updateAsset(payload.id, payload.data)
            updateAsset(payload.id, formData)
                .then(function (data) {
                    // handle success
                    console.log(data);
                    commit('updateAsset', data)
                    store.dispatch('showAlert', {title: 'Successfully updated!', message: 'asset'})
                })
                .catch(function (error) {
                    // handle error
                    console.log(error);
                    store.dispatch('showAlert', {title: 'Error!', message: 'asset'})
                    throw error;
                })
                .finally(function () {
                    // always executed
                });
        },
        deleteAsset ({ commit, state }, payload) {            
            // Make a request for a user with a given ID
            deleteAsset(payload.id)
                .then(function (data) {
                    // handle success
                    console.log(data);
                    commit('removeAsset', {id: payload.id})
                    store.dispatch('showAlert', {title: 'Successfully deleted!', message: 'asset'})
                })
                .catch(function (error) {
                    // handle error
                    console.log(error);
                    store.dispatch('showAlert', {title: 'Error!', message: 'asset'})
                    throw error;
                })
                .finally(function () {
                    // always executed
                });
        }
    }
}

export default assets;