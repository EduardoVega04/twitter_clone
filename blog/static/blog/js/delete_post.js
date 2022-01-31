csrftoken = getCookie('csrftoken');

function delete_post(url) {
    const request = new Request(url, {
        method: 'POST',
        headers: { 'X-CSRFToken': csrftoken },
        mode: 'same-origin' // Do not send CSRF token to another domain.
    });

    fetch(request).then(function(response) {
        return response.json();
    }).then(function(data) {
        let target_post = data.deleted;
        document.getElementById(`tweet_id_${target_post}`).remove();
    }).catch(function(reason) {
        console.log("Error");
    });
}

