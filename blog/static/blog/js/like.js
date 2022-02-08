csrftoken = getCookie('csrftoken');

function like(url) {
    const request = new Request(url, {
        method: 'POST',
        headers: { 'X-CSRFToken': csrftoken },
        mode: 'same-origin' // Do not send CSRF token to another domain.
    });

    fetch(request).then(function (response) {
        return response.json();
    }).then(function (data) {
        let containerLikes = document.querySelector(`#tweet_id_${url.split("/")[2]} .action.like`);
        let counterLikes = containerLikes.querySelector(".like-counter");
        let likeIcon = containerLikes.querySelector(".like-icon");

        if (counterLikes) {
            if (counterLikes.classList.contains("liked")) {
                counterLikes.classList.remove("liked");
                counterLikes.textContent = parseInt(counterLikes.textContent) - 1;

                if (counterLikes.textContent == '0')
                    containerLikes.removeChild(counterLikes);
            }
            else {
                counterLikes.classList.add("liked");
                counterLikes.textContent = parseInt(counterLikes.textContent) + 1;
            }
        }
        else {
            let counterLikes = document.createElement("span");
            counterLikes.classList.add("like-counter", "liked")
            counterLikes.textContent = '1';
            containerLikes.prepend(counterLikes);
        }

        if (likeIcon.getAttribute("fill") == "rgb(249, 24, 128)")
            likeIcon.setAttribute("fill", "currentColor");
        else
            likeIcon.setAttribute("fill", "rgb(249, 24, 128)");
    }).catch(function (reason) {
        console.log("Error");
    });
}
