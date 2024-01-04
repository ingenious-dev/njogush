const NJOGUSH_BASE_URL = `http://${getBaseUrl()}`;
const NJOGUSH_WEBSOCKET_URL = `ws://${getBaseUrl()}`;
const NJOGUSH_AUTHORITY = getBaseUrl();

function getBaseUrl() {
    return import.meta.env.VITE_BASE_URL ?? '127.0.0.1:6564'
}

export {
    NJOGUSH_BASE_URL,
    NJOGUSH_WEBSOCKET_URL,
    NJOGUSH_AUTHORITY,
}