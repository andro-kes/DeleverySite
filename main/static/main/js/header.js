let logoValue = "Kodopes",
    logoLen   = logoValue.length;

function animateLogo(a_p, s_c) {

    document.querySelector(".header__logo").innerHTML = (logoValue.slice(0, s_c)) + "|";

    if (s_c == logoLen) {
        document.querySelector(".header__logo").innerHTML = "Kodopes";
        clearInterval(a_p);
    }
    
}

let symbolCounter = 0;

window.onload = () => {

    setTimeout(() => {
        let animPlayback = setInterval(() => {
            symbolCounter += 1;
            animateLogo(animPlayback, symbolCounter);
        }, 80);
    }, 1000);
}