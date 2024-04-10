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

let image_forms = document.querySelectorAll("input[type='file']");

image_forms.forEach(image_form => {
    image_form.onchange = function (evt) {
        let tgt = evt.target;
        let files = tgt.files;

        let image_image = document.querySelector("#" + image_form.dataset.imgid);
        console.log(image_image)
        // FileReader
        if (FileReader && files && files.length) {
            let fr = new FileReader();
            fr.onload = function () {
                image_image.dataset.imgurl = fr.result;
                image_image.style.zIndex = 200;
                image_image.style.opacity = 1;
                setAvatars();
            }
            fr.readAsDataURL(files[0]);
        }
    }
});
