import {
    fetchProjects,
    createProject,
    getProject,
    updateProject,
    deleteProject,
} from '../services/projects';

import store from '.';

const projects = {
    state: () => ({
        projects: [],
        build_sessions: {},
    }),
    mutations: {
        addProjects(state, payload) {
            state.projects = payload.projects
        },
        prependProject(state, payload) {
            state.projects.unshift(payload);
        },
        updateProject(state, payload) {
            const array = state.projects; // [2, 5, 9]

            // console.log(array);

            // const index = array.indexOf(5);
            const index = array.findIndex((element) => element.id === payload.id);
            if(index > -1) {
                state.projects[index] = payload;
            } else {
                state.projects.push(payload);
            }
            
        },
        removeProject(state, payload) {
            const array = state.projects; // [2, 5, 9]

            // console.log(array);

            // const index = array.indexOf(5);
            const index = array.findIndex((element) => element.id === payload.id);
            if (index > -1) { // only splice array when item is found
                array.splice(index, 1); // 2nd parameter means remove one item only
            }

            // array = [2, 9]
            // console.log(array);

            state.projects = array;
        },
        setBuildSession(state, payload) {
            state.build_sessions[payload.project] = payload;
        }

    },
    getters: {
        projects (state) {
            return state.projects
        }
    },
    actions: {
        fetchProjects ({ commit, state }, payload) {            
            // Make a request for a user with a given ID
            fetchProjects(payload)
                .then(function (data) {
                    // handle success
                    console.log(data);

                    commit('addProjects', {
                        // projects: data.results
                        projects: data
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
        getProject ({ commit, state }, payload) {            
            // Make a request for a user with a given ID
            getProject(payload.id)
                .then(function (data) {
                    // handle success
                    console.log(data);

                    commit('updateProject', data)
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
        createProject ({ commit, state }, payload) {            
            // Make a request for a user with a given ID
            createProject(payload)
                .then(function (data) {
                    // handle success
                    console.log(data);
                    commit('prependProject', data)
                    store.dispatch('showAlert', {title: 'Successfully created!', message: 'project'})
                })
                .catch(function (error) {
                    // handle error
                    console.log(error);
                    store.dispatch('showAlert', {title: 'Error!', message: 'project'})
                    throw error;
                })
                .finally(function () {
                    // always executed
                });
        },
        updateProject ({ commit, state }, payload) {            
            // Make a request for a user with a given ID
            updateProject(payload.id, payload.data)
                .then(function (data) {
                    // handle success
                    console.log(data);
                    // commit('updateProject', data)
                    store.dispatch('getProject', {id: payload.id})
                    store.dispatch('showAlert', {title: 'Successfully updated!', message: 'project'})

                    // 
                    if (payload.data.action) {
                        commit('setBuildSession', data)
                        store.dispatch('fetchSteps', {project: payload.id});
                    }
                })
                .catch(function (error) {
                    // handle error
                    console.log(error);
                    store.dispatch('showAlert', {title: 'Error!', message: 'project'})
                    throw error;
                })
                .finally(function () {
                    // always executed
                });
        },
        deleteProject ({ commit, state }, payload) {            
            // Make a request for a user with a given ID
            deleteProject(payload.id)
                .then(function (data) {
                    // handle success
                    console.log(data);
                    commit('removeProject', {id: payload.id})
                    store.dispatch('showAlert', {title: 'Successfully deleted!', message: 'project'})
                })
                .catch(function (error) {
                    // handle error
                    console.log(error);
                    store.dispatch('showAlert', {title: 'Error!', message: 'project'})
                    throw error;
                })
                .finally(function () {
                    // always executed
                });
        }
    }
}

export default projects;