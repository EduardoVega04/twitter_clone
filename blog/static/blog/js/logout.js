let logoutDiv = document.querySelector('.logout');
let target = document.querySelector('.logout-popup');

logoutDiv.addEventListener("click", function (e) {
    e.stopPropagation();
    if (target.classList.contains('hidden-popup'))
        target.classList.remove('hidden-popup');
    else
        target.classList.add('hidden-popup');
});

document.body.addEventListener("click", function () {
    if (!target.classList.contains('hidden-popup'))
        target.classList.add('hidden-popup');
});

target.addEventListener("click", function (e) {
    e.stopPropagation();
});
