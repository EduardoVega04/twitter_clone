csrftoken = getCookie('csrftoken');

function pin_unpin_post(url) {
    const request = new Request(url, {
        method: 'POST',
        headers: { 'X-CSRFToken': csrftoken },
        mode: 'same-origin' // Do not send CSRF token to another domain.
    });
    
    fetch(request).then(function (response) {
        return response.json();
    }).then(function (data) {
        console.log(data.result);
    }).catch(function (reason) {
        console.log("Error");
    });
}
