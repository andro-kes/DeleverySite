function setAvatars() {
    let avatars = document.querySelectorAll(".profile__avatar");
    avatars.forEach(avatar => {
        avatar.style.backgroundImage = "url(" + avatar.dataset.imgurl + ")";
    });

    let orderImages = document.querySelectorAll(".order__image");
    orderImages.forEach(i => {
        i.style.backgroundImage = "url(" + i.dataset.imgurl + ")";
    });
}
setAvatars();

const statusValue = document.getElementById('value_status').textContent;
if(statusValue === 'Покупатель'){
    document.getElementById('client').classList.add('_active');
} else{
    document.getElementById('company').classList.add('_active');
}