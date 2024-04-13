let main = document.querySelector(".slider__main img");
let subs = document.querySelectorAll(".slider__sub img");

const priceInput = document.querySelector('#order_price');
priceInput.value = document.getElementById('result_price').innerHTML = document.getElementById('result_price').innerHTML
const deleveryInput = document.querySelector('#order_delevery');
deleveryInput.value = 'Econom';
const statusInput = document.querySelector('#order_status');
statusInput.value = 'Заказан'
const numberInput = document.querySelector('#order_number');
numberInput.value = document.querySelector('#number_id').textContent;

subs.forEach(sub => {
    sub.onclick = () => {
        subs.forEach(s => {
            s.classList.remove("_slider_current");
        });
        sub.classList.add("_slider_current");
        main.setAttribute("src", sub.getAttribute("src"));
    };
});
let deliveryOptions = document.querySelectorAll(".delivery__option");
deliveryOptions.forEach(opt => {
    opt.onclick = () => {
        document.querySelector(".delivery__option._picked").classList.remove("_picked");
        opt.classList.add("_picked");
        document.querySelector(".delivery input").value = opt.dataset.val;
        document.querySelector(".info__date b").innerHTML = opt.dataset.date;
        document.getElementById('result_price').innerHTML = opt.dataset.price;
        priceInput.value = opt.dataset.price;
        deleveryInput.value = opt.textContent;
    }    
});
