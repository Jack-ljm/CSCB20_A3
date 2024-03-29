const navSlide = () => {
    const burger = document.querySelector("nav div#burger");
    const nav = document.querySelector('nav');
    const navLinks = document.querySelectorAll('nav div.nav-link');
    const nameWrapper = document.querySelectorAll('nav div.name-wrapper');
    burger.addEventListener('click',() =>{
        nav.classList.toggle('nav-wrapper-active');
        navLinks.forEach((link, index) => {
            link.classList.toggle('nav-link-active');
        })
        nameWrapper.forEach((link, index) => {
            link.classList.toggle('name-wrapper-active');
        })
    });
}
navSlide();
