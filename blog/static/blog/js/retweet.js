csrftoken = getCookie('csrftoken');

function retweet(url) {
    const request = new Request(url, {
        method: 'POST',
        headers: { 'X-CSRFToken': csrftoken },
        mode: 'same-origin' // Do not send CSRF token to another domain.
    });

    fetch(request).then(function (response) {
        return response.json();
    }).then(function (data) {
        let containerRetweets = document.querySelector(`#tweet_id_${url.split("/")[2]} .action.retweet`);
        let counterRetweets = containerRetweets.querySelector(".retweet-counter");
        let retweetIcon = containerRetweets.querySelector(".retweet-icon");

        if (counterRetweets) {
            if (counterRetweets.classList.contains("retweeted")) {
                counterRetweets.classList.remove("retweeted");
                counterRetweets.textContent = parseInt(counterRetweets.textContent) - 1;

                if (counterRetweets.textContent == '0')
                    containerRetweets.removeChild(counterRetweets);
            }
            else {
                counterRetweets.classList.add("retweeted");
                counterRetweets.textContent = parseInt(counterRetweets.textContent) + 1;
            }
        }
        else {
            let counterRetweets = document.createElement("span");
            counterRetweets.classList.add("retweet-counter", "retweeted")
            counterRetweets.textContent = '1';
            containerRetweets.prepend(counterRetweets);
        }

        if (retweetIcon.getAttribute("fill") == "rgb(0, 186, 124)")
            retweetIcon.setAttribute("fill", "currentColor");
        else 
            retweetIcon.setAttribute("fill", "rgb(0, 186, 124)");

    }).catch(function (reason) {
        console.log(reason);
    });
}
