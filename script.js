//Acceille
document.addEventListener("DOMContentLoaded", function () {
    const images = [
        "images/header_slide1.jpg",
        "images/header_slide2.jpg",
        "images/header_slide3.jpg",
    ];

    const imgElement = document.querySelector(".overlay img");
    let currentIndex = 0;

    function changeImage() {
        imgElement.style.transition = "transform 0.5s"; // Transition plus rapide

        if (currentIndex < images.length - 1) {
            currentIndex++;
        } else {
            currentIndex = 0;
        }

        imgElement.style.transform = "translateX(-100%)";

        setTimeout(() => {
            imgElement.src = images[currentIndex];
            imgElement.style.transform = "translateX(0)";
        }, 500); // Délai plus court entre les transitions

        imgElement.classList.add("scrollEffect");

        setTimeout(() => {
            imgElement.classList.remove("scrollEffect");
        }, 500); // Délai plus court entre les transitions
    }

    setInterval(changeImage, 10000); // Changement toutes les 10 secondes
});




//services 
// Fonction pour appliquer l'effet de superposition sur l'image
function applyImageOverlay() {
    const images = document.querySelectorAll(".imgservice");

    images.forEach((img) => {
        img.addEventListener("mouseenter", () => {
            img.style.transition = "transform 0.3s, filter 0.3s";
            img.style.transform = "scale(1.1)";
            img.style.filter = "brightness(80%)"; // Réduit la luminosité pour mettre en évidence l'image
            img.style.zIndex = "1"; // Place l'image au-dessus des autres
        });

        img.addEventListener("mouseleave", () => {
            img.style.transition = "transform 0.3s, filter 0.3s";
            img.style.transform = "scale(1)";
            img.style.filter = "brightness(100%)"; // Rétablit la luminosité à la normale
            img.style.zIndex = "0"; // Rétablit la position Z à la normale
        });
    });
}

// Appel de la fonction d'effet de superposition
applyImageOverlay();




  