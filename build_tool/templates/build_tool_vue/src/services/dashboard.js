import { axios_error_message } from '../network/axios_helper';
import http_client from '../network/http_client';
import { NJOGUSH_BASE_URL } from '../network/network_info';

// TODO https://stackoverflow.com/questions/11796093/is-there-a-way-to-provide-named-parameters-in-a-function-call-in-javascript
// Want to use async/await? Add the `async` keyword to your outer function/method.
async function fetchDashboard() {
    try {
      const response = await http_client.get(`${NJOGUSH_BASE_URL}/api/dashboard/`);
      console.log(response);
      return response.data;
    } catch (error) {
      console.error(error);
      throw new Error(axios_error_message(error));
    }
  }
  

export {
    fetchDashboard,
};