const NJOGUSH_BASE_URL = `http://${getBaseUrl()}`;
const NJOGUSH_WEBSOCKET_URL = `ws://${getBaseUrl()}`;
const NJOGUSH_AUTHORITY = getBaseUrl();

function getBaseUrl() {
    return import.meta.env.VITE_BASE_URL ?? window.location.host
}

export {
    NJOGUSH_BASE_URL,
    NJOGUSH_WEBSOCKET_URL,
    NJOGUSH_AUTHORITY,
}