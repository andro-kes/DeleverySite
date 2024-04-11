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