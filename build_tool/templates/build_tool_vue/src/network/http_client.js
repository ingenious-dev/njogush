import axios, {isCancel, AxiosError} from 'axios';
import { getCookie } from './get_cookie'

const headers = {
    // 'X-Custom-Header': 'foobar',
    "Content-Type": "application/json",
    "Accept": "application/json",
    // "Authorization": `Token ${import.meta.env.VITE_TOKEN != null ? import.meta.env.VITE_TOKEN : ''}`,
}

if(import.meta.env.VITE_TOKEN) {
    headers["Authorization"] = `Token ${import.meta.env.VITE_TOKEN}`
}

const csrftoken = getCookie('csrftoken');
if(csrftoken) {
    // + https://docs.djangoproject.com/en/5.0/howto/csrf/#setting-the-token-on-the-ajax-request
    headers["X-CSRFToken"] = csrftoken
}

const http_client = axios.create({
    // baseURL: 'https://some-domain.com/api/',
    // timeout: 30000,
    headers
});

export default http_client;