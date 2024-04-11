let main = document.querySelector(".slider__main img");
let subs = document.querySelectorAll(".slider__sub img");
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
    }    
});
