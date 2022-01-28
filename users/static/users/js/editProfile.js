const editProfileModal = document.getElementById('editProfileModal');
const profile_pic = document.getElementById("id_profile_pic");
const cover_pic = document.getElementById("id_cover_pic");


if (editProfileModal) {
    editProfileModal.addEventListener("hide.bs.modal", function (event) {
        let redirectURL = document.getElementsByClassName("btn-close")[0];
        window.location.href = redirectURL.href;
    });

    const myModal = new bootstrap.Modal(editProfileModal);
    myModal.show();
}

if (profile_pic) {
    showUploadedImage(profile_pic, "profile")
}

if (cover_pic) {
    showUploadedImage(cover_pic, "cover");
}

function toggleSpinner(pic, status) {
    const spinner = document.getElementById(`spinner_${pic}`);
    const addIcon = document.getElementById(`add_${pic}_label`);

    if (status === "show") {
        addIcon.style.display = "none";
        spinner.style.display = "block";
    }
    else {
        spinner.style.display = "none";
        addIcon.style.display = "flex";
    }
}

function showUploadedImage(fileInputElement, imgName) {
    let previewImg = document.querySelector(`.edit-${imgName}-photo`);

    fileInputElement.addEventListener("change", function() {
        toggleSpinner(imgName, "show");
        const img = this.files[0];

        if (img) {
            const readerImg = new FileReader();
            readerImg.addEventListener("load", function() {
                previewImg.setAttribute("src", this.result);
                toggleSpinner(imgName, "hide");
            });

            readerImg.readAsDataURL(img);
        }
    });
}
