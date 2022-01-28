let ancestors = document.querySelectorAll(".ancestor");
let children = document.querySelectorAll(".child");


if (ancestors && ancestors.length > 0) {
    for (let i = 0; i < ancestors.length; i++) {
        ancestors[i].querySelector("article").style.borderBottom = "0px";

        let conversationLine = document.createElement("div");
        let authorImgDiv = ancestors[i].querySelector(".post-author-image");
        const authorImg = ancestors[i].querySelector(".post-author-image img");
        const rect = authorImg.getBoundingClientRect();

        conversationLine.id = "conversation-line";
        conversationLine.style.height = ancestors[i].querySelector("article").offsetHeight - 53 + 'px';
        conversationLine.style.top = rect.y + 52 + 'px';
        authorImgDiv.append(conversationLine);
    }
}

if ((ancestors && ancestors.length > 0) || (children && children.length > 0)) {
    console.log(ancestors);
    console.log(children);
    document.querySelector(".post-tweet").style.paddingTop = "15px";
    let textAreaForm = document.getElementsByName("content")[0];
    textAreaForm.placeholder = "Tweet your reply";
    textAreaForm.style.marginBottom = "0px";

    let postOptions = document.querySelector(".post-options");
    postOptions.style.borderTop = "none";
    document.getElementById("postTweetBtn").innerText = "Reply";
}
