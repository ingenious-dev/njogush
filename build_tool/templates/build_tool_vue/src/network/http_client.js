import axios, {isCancel, AxiosError} from 'axios';

const headers = {
    // 'X-Custom-Header': 'foobar',
    "Content-Type": "application/json",
    "Accept": "application/json",
    "Authorization": `Token ${import.meta.env.VITE_TOKEN != null ? import.meta.env.VITE_TOKEN : ''}`,
}

// if(import.meta.env.VITE_TOKEN) {
//     headers["Authorization"] = import.meta.env.VITE_TOKEN
// }

const http_client = axios.create({
    // baseURL: 'https://some-domain.com/api/',
    // timeout: 30000,
    headers
});

export default http_client;