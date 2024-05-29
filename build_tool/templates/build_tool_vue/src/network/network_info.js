// const NJOGUSH_BASE_URL = `http://${getBaseUrl()}`;
const NJOGUSH_BASE_URL = `${window.location.protocol}//${getBaseUrl()}`;
const NJOGUSH_WEBSOCKET_URL = `${window.location.protocol.includes('https') ? 'wss' : 'ws'}://${getBaseUrl()}`;
const NJOGUSH_AUTHORITY = getBaseUrl();

function getBaseUrl() {
    return import.meta.env.VITE_BASE_URL ?? window.location.host
}

export {
    NJOGUSH_BASE_URL,
    NJOGUSH_WEBSOCKET_URL,
    NJOGUSH_AUTHORITY,
    getBaseUrl
}