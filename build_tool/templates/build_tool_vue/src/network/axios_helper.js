
function axios_error_message(error) {
    var error_message = ''
    // TODO https://axios-http.com/docs/handling_errors
    if (error.response) {
        // The request was made and the server responded with a status code
        // that falls out of the range of 2xx
        console.log(error.response.data);
        console.log(error.response.status);
        console.log(error.response.headers);
        // return error.response.data.toString();

        try {
            for(let errorKey in error.response.data) {
                // + https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array/isArray
                if(Array.isArray(error.response.data[errorKey])) {
                    error.response.data[errorKey].forEach(element => {
                        error_message += element + ' '
                    });
                } else {
                    error_message += error.response.data[errorKey]
                }
            }
        } catch (error) {
            // Could not parse error. Probably a page error response rather than a JSON was sent
        }

    } else if (error.request) {
        // The request was made but no response was received
        // `error.request` is an instance of XMLHttpRequest in the browser and an instance of
        // http.ClientRequest in node.js
        console.log(error.request);
        return error.request.toString();
    } else {
        // Something happened in setting up the request that triggered an Error
        console.log('Error', error.message);
        return error.message.toString();
    }

    return error_message;
}

export {
    axios_error_message
}
