csrftoken = getCookie('csrftoken');

function pin_unpin_post(url) {
    document.querySelector(`#tweet_id_${url.split("/")[2]} .dropdown-menu`).style.display = "none";
    const request = new Request(url, {
        method: 'POST',
        headers: { 'X-CSRFToken': csrftoken },
        mode: 'same-origin' // Do not send CSRF token to another domain.
    });
    
    fetch(request).then(function (response) {
        return response.json();
    }).then(function (data) {
        window.location.reload();
    }).catch(function (reason) {
        console.log("Error");
    });
}
