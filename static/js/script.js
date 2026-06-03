const card=document.getElementById("card");

card.addEventListener("click",()=>{
    card.innerHTML = `
    <h1 class="text-lg mt-4">Best of Luck! </h1>`;
});

const menuBtn = document.getElementById("menu-btn");
const mobileMenu = document.getElementById("mobile-menu");

menuBtn.addEventListener(("click"),()=>{

    mobileMenu.classList.toggle("hidden");
})


