let radioBtns = document.querySelectorAll(".status__btn");

radioBtns.forEach(radio => {
    radio.onclick = () => {
        let radioGroup = radio.dataset.group;
        document.querySelectorAll(`.status__btn[data-group='${radioGroup}']`).forEach(r => {
            r.classList.remove("_active");
        });
        radio.classList.add("_active");
    };
});

window.onload = () => {
    const orders_list = document.querySelectorAll('.orders__list');
    orders_list.forEach(order => {
        const formStatus = order.querySelector('#id_status'),
        formNumber = order.querySelector('#id_number'),
        orderStatus = order.querySelector('#order_status'),
        orderNumber = order.querySelector('#order_number');

        formNumber.value = orderNumber.textContent;
        formStatus.value = orderStatus.textContent;

        const statusValue = orderStatus.textContent.trim(); // Получаем значение статуса из элемента orderStatus

        const radioButtons = order.querySelectorAll('input[type="radio"][name="1"]');

        // Перебираем радиокнопки и устанавливаем нужную в состояние `checked`
        radioButtons.forEach((radioButton) => {
            const associatedLabel = radioButton.previousElementSibling;
            if (associatedLabel.textContent.trim() === statusValue) {
                radioButton.checked = true;
                associatedLabel.classList.add("_active");
            };
            radioButton.onclick = () => {
                let radioGroup = radioButton.dataset.group;
                order.querySelectorAll(`.status__btn[data-group='${radioGroup}']`).forEach(r => {
                    r.classList.remove("_active");
                });
                radioButton.classList.add("_active");
                formStatus.value = associatedLabel.textContent;
            };
        });
    });
}




