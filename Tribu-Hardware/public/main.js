document.querySelector('.btn_js').addEventListener('click', () => {
    document.querySelector('.nav-menu').classList.toggle('show');
});
ScrollReveal().reveal('.presentacion');
ScrollReveal().reveal('.new_cards',{delay: 500});
ScrollReveal().reveal('.banner_card',{delay: 500});
ScrollReveal().reveal('.red_social',{delay: 500});
ScrollReveal().reveal('.derechos',{delay: 500});