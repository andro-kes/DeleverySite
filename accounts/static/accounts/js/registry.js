let tabsBtn = document.querySelectorAll(".registry__switch .switch__btn");

const formsStatus = document.querySelectorAll('#status_form');
if (formsStatus.length){
    console.log(formsStatus)
    formsStatus[0].value = 'Покупатель';
    formsStatus[1].value = 'Компания';
}


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

checkboxes.forEach(checkbox => {
    // new
    const category = checkbox.dataset.category;
    const cityPk = checkbox.id;
    let checkboxInput;
    if(category==='address'){
        checkboxInput = document.querySelector(`#id_${category}_${cityPk-1}`);
    } else{
        checkboxInput = document.querySelector(`#id_list_${category}_${cityPk-1}`);
    }
    if(checkboxInput && checkboxInput.checked){
        checkbox.classList.toggle("_checked");
    }
    checkbox.addEventListener('click', f => {
        checkbox.classList.toggle("_checked");
        const category = checkbox.dataset.category;
        const cityPk = checkbox.id;
        if(category === 'warehouse'){
            const checkboxInput = document.querySelector(`#id_list_warehouse_${cityPk-1}`);
            if(checkboxInput.checked){
                checkboxInput.checked = false;
            } else{
                checkboxInput.checked = true;
            }
        } else if(category === 'pick_up_point'){
            const checkboxInput = document.querySelector(`#id_list_pick_up_point_${cityPk-1}`);
            if(checkboxInput.checked){
                checkboxInput.checked = false;
            } else{
                checkboxInput.checked = true;
            }
        } else if(category === 'address'){
            const checkboxInput = document.querySelector(`#id_address_${cityPk-1}`);
            const checkboxes_clear = document.querySelectorAll('input[type="checkbox"]');
            const div_clear = document.querySelectorAll('div[data-category="address"]');
            checkboxes_clear.forEach(checkbox => {
                checkbox.checked = false;
            });
            div_clear.forEach(div => {
                div.classList.remove('_checked');
            });
            checkbox.classList.toggle("_checked");
            if(checkboxInput.checked){
                checkboxInput.checked = false;
            } else{
                checkboxInput.checked = true;
            }
        }
    })
});




