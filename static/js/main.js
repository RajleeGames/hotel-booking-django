// Wait until the DOM is fully loaded
document.addEventListener('DOMContentLoaded', function() {
    // Get the mobile menu button and the menu itself
    const menuButton = document.querySelector('.menu-toggle');
    const mobileMenu = document.querySelector('.mobile-menu');

    // Check if the button and menu exist
    if (menuButton && mobileMenu) {
        // Add event listener to toggle the menu
        menuButton.addEventListener('click', function() {
            mobileMenu.classList.toggle('hidden'); // Toggles the 'hidden' class on the menu
        });
    }
});
