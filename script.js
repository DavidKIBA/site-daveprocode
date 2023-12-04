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
});



//services 
// Fonction pour appliquer l'effet de superposition sur l'image
function applyImageOverlay() {
    const images = document.querySelectorAll(".imgservice");

    images.forEach((img) => {
        img.addEventListener("mouseenter", () => {
            img.style.transition = "transform 0.3s, filter 0.3s";
            img.style.transform = "scale(0.9)"; // Rétrécit l'image
            img.style.filter = "blur(5px)";
        });

        img.addEventListener("mouseleave", () => {
            img.style.transition = "transform 0.3s, filter 0.3s";
            img.style.transform = "scale(1)";
            img.style.filter = "blur(0)";
        });
    });
}

// option voir plus //

<script>
    // Ajoutez ce script pour activer l'effet "Voir plus"
    $(document).ready(function () {
        $(".toggle-text").click(function () {
            var $this = $(this);
            var $text = $this.parent().next().find(".truncated-text");

            $text.toggleClass("expanded");

            if ($text.hasClass("expanded")) {
                $text.text("Création de stratégies de contenu personnalisées, du marketing engageant aux campagnes sur les réseaux sociaux, pour renforcer la notoriété de votre marque.");
                $this.text("Voir moins");
            } else {
                $text.text("Création de stratégies de contenu personnalisées, du marketing engageant aux campagnes sur les réseaux sociaux, pour renforcer la notoriété de votre marque.");
                $this.text("Voir plus");
            }
        });
    });
</script>

// Appel de la fonction d'effet de superposition
applyImageOverlay();

  