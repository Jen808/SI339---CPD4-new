document.addEventListener("DOMContentLoaded", () => {
   const toggleMenu = document.getElementById("toggle-menu");
   const navbar = document.getElementById("navbar");

   toggleMenu.addEventListener("click", () => {
      navbar.classList.toggle("active");
      toggleMenu.classList.toggle("active");
   });

   const images = document.querySelectorAll("img[src*='../images/profiles/']");

   images.forEach((img) => {
      img.onerror = () => {
         img.src = '../images/profiles/default_image.png';
      };
   });
});