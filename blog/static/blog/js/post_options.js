function getCookie(name) {
    let cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        const cookies = document.cookie.split(';');
        for (let i = 0; i < cookies.length; i++) {
            const cookie = cookies[i].trim();
            // Does this cookie string begin with the name we want?
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}

const csrftoken = getCookie('csrftoken');


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


function pin_post(user_id, post_id) {

}
