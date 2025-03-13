document.addEventListener('DOMContentLoaded', function() {
  /*************** HAMBURGER MENU CODE ******************/
  const menuButton = document.querySelector('.hamburger');
  const mobileMenu = document.querySelector('.main-nav');
  const closeBtn = document.querySelector('.close-btn');
  
  if (menuButton && mobileMenu && closeBtn) {
    // Toggle menu when hamburger is clicked
    menuButton.addEventListener('click', function(e) {
      e.stopPropagation();
      mobileMenu.classList.toggle('open');
    });
    
    // Close menu when the close button is clicked
    closeBtn.addEventListener('click', function() {
      mobileMenu.classList.remove('open');
    });
    
    // Close menu when clicking outside
    document.addEventListener('click', function(e) {
      if (!mobileMenu.contains(e.target) && !menuButton.contains(e.target)) {
        mobileMenu.classList.remove('open');
      }
    });
  }

  /*************** SLIDER CODE (for any slider-container) ******************/
  const sliderContainers = document.querySelectorAll('.slider-container');
  sliderContainers.forEach(container => {
    const slider = container.querySelector('.slider');
    const slides = container.querySelectorAll('.slide');
    const prevBtn = container.querySelector('.prev-arrow');
    const nextBtn = container.querySelector('.next-arrow');

    if (!slider || slides.length === 0) return; // Skip if structure is missing

    let currentIndex = 0;
    const totalSlides = slides.length;

    function updateSlidePosition() {
      slider.style.transform = `translateX(-${currentIndex * 100}%)`;
    }

    if (prevBtn) {
      prevBtn.addEventListener('click', () => {
        currentIndex = (currentIndex === 0) ? totalSlides - 1 : currentIndex - 1;
        updateSlidePosition();
      });
    }

    if (nextBtn) {
      nextBtn.addEventListener('click', () => {
        currentIndex = (currentIndex + 1) % totalSlides;
        updateSlidePosition();
      });
    }

    // Automatic sliding every 4 seconds
    setInterval(() => {
      currentIndex = (currentIndex + 1) % totalSlides;
      updateSlidePosition();
    }, 4000);
  });

  /*************** OPTIONAL: IntersectionObserver for Fade-In Effects ******************/
  const sections = document.querySelectorAll('.event-section');
  if (sections.length > 0) {
    const observer = new IntersectionObserver((entries) => {
      entries.forEach(entry => {
        if (entry.isIntersecting) {
          entry.target.classList.add('fade-in-up');
          observer.unobserve(entry.target);
        }
      });
    }, { threshold: 0.1 });
    sections.forEach(section => observer.observe(section));
  }
});
