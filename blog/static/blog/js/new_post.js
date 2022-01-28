const tx = document.getElementById("id_content");
const postImg = document.getElementById("id_media");
const tweetBtn = document.getElementById("postTweetBtn");
const spinner_media = document.getElementById("spinner_post_media");


if (tx) {
    tx.setAttribute("style", "height:" + (tx.scrollHeight) + "px;overflow-y:hidden;");
    tx.addEventListener("input", OnInput, false);
    tx.addEventListener("keyup", postHasContent, false);
}

if(postImg) {
    displayMedia(postImg);
}

function OnInput() {
    this.style.height = "auto";
    this.style.height = (this.scrollHeight) + "px";
}

function postHasContent() {
    if (tx.value === '' && postImg.value === '')
        tweetBtn.disabled = true;
    else
        tweetBtn.disabled = false;
}

function displayMedia(file) {
    const mediaContainer = document.getElementsByClassName("post-media-files")[0];
    const cancelImg = document.getElementById("cancelPostImg");

    file.addEventListener("change", function() {
        const img = this.files[0];

        if (img) {
            spinner_media.style.display = "block";
            mediaContainer.style.display = "flex";
            const readerImg = new FileReader();
            readerImg.addEventListener("load", function () {
                postHasContent();

                let prevImg = mediaContainer.getElementsByClassName("img-fluid")[0];
                if (prevImg)
                    mediaContainer.removeChild(prevImg);

                let uploadedImg = document.createElement('img');
                uploadedImg.classList.add("img-fluid");
                uploadedImg.src = this.result;
                mediaContainer.appendChild(uploadedImg);
                spinner_media.style.display = "none";

                cancelImg.addEventListener("click", function() {
                    prevImg = mediaContainer.getElementsByClassName("img-fluid")[0];
                    if (prevImg)
                        mediaContainer.removeChild(prevImg);

                    file.value = '';
                    mediaContainer.style.display = "none";
                    postHasContent();
                });
            });

            readerImg.readAsDataURL(img);
        }
    }, false);
}
