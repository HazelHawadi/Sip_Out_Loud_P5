document.addEventListener("DOMContentLoaded", function () {
    let slider = document.querySelector(".hero-slider");

    if (slider) {
        let index = 0;
        let slides = slider.children.length;

        // Apply a smoother transition effect
        slider.style.transition = "transform 1.5s ease-in-out";

        function nextSlide() {
            index = (index + 1) % slides;
            slider.style.transform = `translateX(-${index * 100}%)`;
        }

        setInterval(nextSlide, 5000); // Slower transition (5 seconds)
    } else {
        console.error("Hero slider not found!");
    }
});
