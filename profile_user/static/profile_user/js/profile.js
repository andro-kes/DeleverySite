let avatars = document.querySelectorAll(".profile__avatar");
avatars.forEach(avatar => {
    avatar.style.backgroundImage = "url(" + avatar.dataset.imgurl + ")";
});

let orderImages = document.querySelectorAll(".order__image");

orderImages.forEach(i => {
    i.style.backgroundImage = "url(" + i.dataset.imgurl + ")";
});
    