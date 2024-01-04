import { axios_error_message } from './axios_helper';
import http_client from '../network/http_client';
import { NJOGUSH_BASE_URL } from '../network/network_info';

// TODO https://stackoverflow.com/questions/11796093/is-there-a-way-to-provide-named-parameters-in-a-function-call-in-javascript
// Want to use async/await? Add the `async` keyword to your outer function/method.
async function fetchProjects({name, limit, page}) {
    var query = name == null ? '' : `name=${name}`;
    query += limit == null ? '' : `&limit=${limit}`;
    query += page == null ? '' : `&page=${page}`;
    query = `?${query}`;

    try {
      const response = await http_client.get(`${NJOGUSH_BASE_URL}/api/projects/${query}`);
      console.log(response);
      return response.data;
    } catch (error) {
      console.error(error);
      throw new Error(axios_error_message(error));
    }
  }
  
async function createProject(data) {
    try {
        const response = await http_client.post(`${NJOGUSH_BASE_URL}/api/projects/`, data);
        console.log(response);
        return response.data;
    } catch (error) {
        console.error(error);
        throw new Error(axios_error_message(error));
    }
}

async function getProject(id) {
    try {
        const response = await http_client.get(`${NJOGUSH_BASE_URL}/api/projects/${id}/`);
        console.log(response);
        return response.data;
    } catch (error) {
        console.error(error);
        throw new Error(axios_error_message(error));
    }
}

async function updateProject(id, data) {
    try {
        const response = await http_client.patch(`${NJOGUSH_BASE_URL}/api/projects/${id}/`, data);
        console.log(response);
        return response.data;
    } catch (error) {
        console.error(error);
        throw new Error(axios_error_message(error));
    }
}

async function deleteProject(id) {
    try {
        const response = await http_client.delete(`${NJOGUSH_BASE_URL}/api/projects/${id}/`);
        console.log(response);
        return response;
    } catch (error) {
        console.error(error);
        throw new Error(axios_error_message(error));
    }
}

export {
    fetchProjects,
    createProject,
    getProject,
    updateProject,
    deleteProject,
};