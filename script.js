document.addEventListener("DOMContentLoaded", function () {
     // Ajout d'une fonction pour déclencher l'animation de descente
     function animateAboutDave() {
        const aboutDave = document.getElementById("aboutDave");
        aboutDave.classList.add("slide-down-animation");
    }

    // Appelez la fonction pour déclencher l'animation après un certain délai (par exemple, 1000 millisecondes)
    setTimeout(animateAboutDave, 1000);
    const images = [
        "images/header_slide1.jpg",
        "images/header_slide2.jpg",
        "images/header_slide3.jpg",
    ];

    let loadedImages = 0;

    function preloadImages() {
        images.forEach((src) => {
            const img = new Image();
            img.onload = () => {
                loadedImages++;
                if (loadedImages === images.length) {
                    // Toutes les images sont chargées, retirez la classe preload-page
                    document.body.classList.remove("preload-page");

                    // Appel de la fonction pour changer les images après le preload
                    startImageChange();
                }
            };
            img.src = src;
        });
    }  

    // Appel de la fonction de préchargement des images
    preloadImages();

    // Déplacement du reste du code à l'extérieur de la fonction DOMContentLoaded
    const imgElement = document.querySelector(".overlay img");
    let currentIndex = 0;

    function startImageChange() {
        function changeImage() {
            if (currentIndex === 0) {
                // Slide 1: De la droite vers la gauche
                imgElement.style.transform = "translateX(100%)";

                setTimeout(() => {
                    imgElement.src = images[currentIndex];
                    imgElement.style.transform = "translateX(0)";
                    currentIndex = (currentIndex + 1) % images.length;
                }, 1000);
            } else if (currentIndex === 1) {
                // Slide 2: De la gauche vers la droite
                imgElement.style.transform = "translateX(-100%)";

                setTimeout(() => {
                    imgElement.src = images[currentIndex];
                    imgElement.style.transform = "translateX(0)";
                    currentIndex = (currentIndex + 1) % images.length;
                }, 1000);
            } else {
                // Slide 3: Du bas vers le haut
                imgElement.style.transform = "translateY(100%)";

                setTimeout(() => {
                    imgElement.src = images[currentIndex];
                    imgElement.style.transform = "translateY(0)";
                    currentIndex = (currentIndex + 1) % images.length;
                }, 1000);
            }

            imgElement.classList.add("scrollEffect");

            setTimeout(() => {
                imgElement.classList.remove("scrollEffect");
            }, 1000);
        }

        setInterval(changeImage, 10000); // Changement toutes les 10 secondes
    }

    //services 
    // Fonction pour appliquer l'effet de superposition sur l'image
    function applyCardZoomEffect() {
        const serviceCards = document.querySelectorAll(".card.mb-3");
      
        serviceCards.forEach((card) => {
          card.addEventListener("mouseenter", () => {
            console.log("Mouse enter");
            card.style.transition = "transform 0.3s";
            card.style.transform = "scale(1.1)"; // Zoom in
          });
      
          card.addEventListener("mouseleave", () => {
            console.log("Mouse leave");
            card.style.transition = "transform 0.3s";
            card.style.transform = "scale(1)"; // Zoom back to normal
          });
        });
      }
      
      // Appel de la fonction pour ajouter l'effet de zoom aux cartes de service
      applyCardZoomEffect();
      

    // Fonction pour détecter le défilement et ajouter des animations
    function handleScroll() {
        const elements = document.querySelectorAll(".scroll-animation");
        
        elements.forEach((element) => {
            const elementPosition = element.getBoundingClientRect().top;
            const windowHeight = window.innerHeight;

            if (elementPosition < windowHeight * 0.75) {
                // Ajoutez une classe pour déclencher l'animation lorsque l'élément est visible
                element.classList.add("animate");
            }
        });
    }

    // Écoutez l'événement de défilement
    window.addEventListener("scroll", handleScroll);

    // Appelez la fonction pour gérer l'animation lors du chargement initial
    handleScroll();
});
