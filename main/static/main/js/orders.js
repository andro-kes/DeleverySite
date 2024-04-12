let radioBtns = document.querySelectorAll(".status__btn");
radioBtns.forEach(radio => {
    radio.onclick = () => {
        let radioGroup = radio.dataset.group;
        document.querySelectorAll(`.status__btn[data-group='${radioGroup}']`).forEach(r => {
            r.classList.remove("_active");
        });
        radio.classList.add("_active");
    }
});
console.log(document.querySelector(".header").pageY)