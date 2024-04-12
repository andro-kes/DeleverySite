let imageLoads = document.querySelectorAll(".images__image input");
imageLoads.forEach(il => {
    il.onchange = (evt) => {
        let tgt = evt.target;
        let files = tgt.files;
        let image_image = document.querySelector(`#` + il.dataset.imgid);
        // FileReader
        if (FileReader && files && files.length) {
            let fr = new FileReader();
            fr.onload = function () {
                image_image.src = fr.result;
                image_image.style.zIndex = 200;
                image_image.style.opacity = 1;
                il.value = "";
            }
            fr.readAsDataURL(files[0]);
        }
    }
});
let tagsList = [];
function addTag() {
    let tagsInput = document.querySelector("#tags_field").value.trim();
    if (tagsInput != "" && tagsList.indexOf(tagsInput.toLowerCase()) < 0 && tagsList.length < 5) {
        tagsList.push(tagsInput.toLowerCase());
        document.querySelector("#tags_field").value = '';
        showTags();
        document.querySelectorAll(".tag__delete").forEach(tag_del => {
            tag_del.onclick = () => {
                console.log("some")
                delTag(tagsList.indexOf(tag_del.dataset.tagval));
            };
        });
    }
}
function showTags() {
    let tagsListHTML = '';
    tagsList.forEach((currentTag) => {
        if (currentTag != "") {
            tagsListHTML += 
            `
            <div class="tags__tag">
                ${currentTag}
                <img class="tag__delete" data-tagval="${currentTag}" src="assets/images/ui/x.svg">
            </div>
            `;
        }
    });
    let tagsField = document.querySelector(".create__tags");
        tagsField.innerHTML = tagsListHTML +
        `
        <input type="text" value="${tagsList.join(" ")}">
        `;
}

function delTag(i) {
    console.log(i, tagsList);
    tagsList.splice(i, 1);
    showTags();
    
    document.querySelectorAll(".tag__delete").forEach(tag_del => {
        tag_del.onclick = () => {
            console.log("some")
            delTag(tagsList.indexOf(tag_del.dataset.tagval));
        };
    });
}

document.querySelector(".images__clean").onclick = () => {
    imageLoads = document.querySelectorAll(".images__image input");
    imageLoads.forEach(il => {
        il.value = "";
    });
    imagePics = document.querySelectorAll(".images__image img");
    imagePics.forEach(ipic => {
        ipic.setAttribute("src", ipic.dataset.default);
    })
};