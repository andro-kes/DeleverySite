let tabsBtn = document.querySelectorAll(".registry__switch .switch__btn");

tabsBtn.forEach(i => {
    i.onclick = () => {
        document.querySelector(".registry__tab.tab_active").classList.remove("tab_active");
        let tabClass = i.dataset.tab;
        document.querySelector(".registry__tab." + tabClass).classList.add("tab_active");

        document.querySelector(".registry__switch .switch__btn._active").classList.remove("_active");
        i.classList.add("_active");
    };
});

let checkboxes = document.querySelectorAll(".checkbox__button");

checkboxes.forEach(i => {
    i.onclick = () => {
        i.classList.toggle("_checked");
    };
});




