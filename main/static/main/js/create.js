let status_create = document.getElementById('id_status');
status_create.value = 'Выставлен';

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
        if(document.getElementById('id_category').value){
            document.getElementById('id_category').value += ' ' + document.querySelector("#tags_field").value
        } else{
            document.getElementById('id_category').value += document.querySelector("#tags_field").value
        }

        document.querySelector("#tags_field").value = '';
        showTags();
        document.querySelectorAll(".tag__delete").forEach(tag_del => {
            tag_del.addEventListener('click', f = () => {
                let indexInTagsList = tagsList.indexOf(tag_del.dataset.tagval);
                delTag(indexInTagsList);
                let categoryValue = document.getElementById('id_category').value;
                let arr = categoryValue.split(" ");
                let indexInArr = arr.indexOf(tag_del.dataset.tagval);
                arr.splice(indexInArr, 1);
                document.getElementById('id_category').value = arr.join(" ");
            });
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
                <img class="tag__delete" data-tagval="${currentTag}" src="/static/accounts/img/ui/x.svg">
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
    tagsList.splice(i, 1);
    showTags();
    
    document.querySelectorAll(".tag__delete").forEach(tag_del => {
        tag_del.onclick = () => {
            delTag(tagsList.indexOf(tag_del.dataset.tagval));
        };
    });
}

