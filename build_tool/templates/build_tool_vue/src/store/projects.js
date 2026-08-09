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
        currentProject: null,

        count: 0,
        isLoading: false,
        next: null,
        previous: null,
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
        },

        processResponse(state, payload) {
            // handle success
            console.log(payload);

            state.projects = payload.results

            var next = null
            if(payload.next) {
                // next = new URLSearchParams(payload.next).get('page')

                const url = new URL(payload.next)
                next = url.searchParams.get("page")
            }
            var previous = null
            if(payload.previous) {
                // previous = new URLSearchParams(payload.previous).get('page') ?? 1

                const url = new URL(payload.previous)
                previous = url.searchParams.get("page") ?? 1
            }

            state.count = payload.count;
            state.next = next;
            state.previous = previous;
        },
        setCurrentProject(state, payload) {
            state.currentProject = payload;
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
                // .then(function (data) {
                //     // handle success
                //     console.log(data);

                //     commit('addProjects', {
                //         projects: data.results
                //     })
                // })
                .then(function (data) {
                    // handle success
                    // console.log(data);

                    commit('processResponse', data)
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
                    commit('setCurrentProject', data)
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
                    store.dispatch('showAlert', {title: 'Successfully created!', message: 'project', status: 'success'})
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
        updateProject ({ commit, state }, payload) {            
            // Make a request for a user with a given ID
            updateProject(payload.id, payload.data)
                .then(function (data) {
                    // handle success
                    console.log(data);
                    // commit('updateProject', data)
                    store.dispatch('getProject', {id: payload.id})
                    store.dispatch('showAlert', {title: 'Successfully updated!', message: 'project', status: 'success'})

                    // 
                    if (payload.data.action) {
                        commit('setBuildSession', data)
                        store.dispatch('fetchSteps', {project: payload.id});
                    }
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
        deleteProject ({ commit, state }, payload) {            
            // Make a request for a user with a given ID
            deleteProject(payload.id)
                .then(function (data) {
                    // handle success
                    console.log(data);
                    commit('removeProject', {id: payload.id})
                    store.dispatch('showAlert', {title: 'Successfully deleted!', message: 'project', status: 'success'})
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

export default projects;