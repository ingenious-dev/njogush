import { axios_error_message } from '../network/axios_helper';
import http_client from '../network/http_client';
import { NJOGUSH_BASE_URL } from '../network/network_info';

// TODO https://stackoverflow.com/questions/11796093/is-there-a-way-to-provide-named-parameters-in-a-function-call-in-javascript
// Want to use async/await? Add the `async` keyword to your outer function/method.
async function fetchBuildSessions({project, limit, page}) {
    var query = project == null ? '' : `project=${project}`;
    query += limit == null ? '' : `&limit=${limit}`;
    query += page == null ? '' : `&page=${page}`;
    query = `?${query}`;

    try {
      const response = await http_client.get(`${NJOGUSH_BASE_URL}/api/build-sessions/${query}`);
      console.log(response);
      return response.data;
    } catch (error) {
      console.error(error);
      throw new Error(axios_error_message(error));
    }
  }
  
async function createBuildSession(data) {
    try {
        const response = await http_client.post(`${NJOGUSH_BASE_URL}/api/build-sessions/`, data);
        console.log(response);
        return response.data;
    } catch (error) {
        console.error(error);
        throw new Error(axios_error_message(error));
    }
}

async function getBuildSession(id) {
    try {
        const response = await http_client.get(`${NJOGUSH_BASE_URL}/api/build-sessions/${id}/`);
        console.log(response);
        return response.data;
    } catch (error) {
        console.error(error);
        throw new Error(axios_error_message(error));
    }
}

async function updateBuildSession(id, data) {
    try {
        const response = await http_client.patch(`${NJOGUSH_BASE_URL}/api/build-sessions/${id}/`, data);
        console.log(response);
        return response.data;
    } catch (error) {
        console.error(error);
        throw new Error(axios_error_message(error));
    }
}

async function deleteBuildSession(id) {
    try {
        const response = await http_client.delete(`${NJOGUSH_BASE_URL}/api/build-sessions/${id}/`);
        console.log(response);
        return response;
    } catch (error) {
        console.error(error);
        throw new Error(axios_error_message(error));
    }
}

export {
    fetchBuildSessions,
    createBuildSession,
    getBuildSession,
    updateBuildSession,
    deleteBuildSession,
};