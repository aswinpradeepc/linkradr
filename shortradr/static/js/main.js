document.addEventListener('DOMContentLoaded', () => {
    const hamburger = document.querySelector('.hamburger-menu');
    const mobileNavOverlay = document.querySelector('.mobile-nav-overlay');
    const closeNav = document.querySelector('.close-nav'); // Select close button
    const mobileNavLinks = document.querySelectorAll('.mobile-nav-link');

    if (hamburger && mobileNavOverlay && closeNav) {
        hamburger.addEventListener('click', () => {
            mobileNavOverlay.classList.toggle('active');
            hamburger.classList.toggle('active');
        });

        closeNav.addEventListener('click', () => {  // Handle close button click
            mobileNavOverlay.classList.remove('active');
            hamburger.classList.remove('active');
        });

        mobileNavLinks.forEach(link => {
            link.addEventListener('click', () => {
                mobileNavOverlay.classList.remove('active');
                hamburger.classList.remove('active');
            });
        });
    }
});
