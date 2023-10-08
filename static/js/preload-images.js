console.log('hello')
var images = [
    "../static/img/580b585b2edbce24c47b270f.png",
    "../static/img/mercury (1).png",
    "../static/img/venus.png"
];

// Preload the images
images.forEach(function (imgSrc) {
    var img = new Image();
    img.src = imgSrc;
});

// Function to scroll to a specific section
function scrollToSection(sectionId) {
    var section = document.getElementById(sectionId);
    console.log(section)
    if (section) {
        section.scrollIntoView({
            behavior: 'smooth',
            block: 'start'
        });
    }
}

// Add click functionality to the images
document.addEventListener("DOMContentLoaded", function () {
    var imageElements = document.querySelectorAll(".planet-image");

    imageElements.forEach(function (imageElement, index) {
        imageElement.addEventListener("click", function () {
            // Scroll to the corresponding section when the image is clicked
            scrollToSection("section" + index); // Assumes your sections have IDs like "section0", "section1", etc.
        });
    });
});
