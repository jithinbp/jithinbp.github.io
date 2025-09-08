document.addEventListener("DOMContentLoaded", function() {
  const sidebar = document.getElementById("_sidebar");
  let lastScrollY = window.scrollY;

  // Function to check if the device is a mobile/tablet
  function isMobileOrTablet() {
    return window.matchMedia("(max-width: 1024px)").matches;
  }

  // Handle the scroll event
  window.addEventListener("scroll", function() {
    // Only apply the logic on mobile and tablet devices
    if (isMobileOrTablet()) {
      const currentScrollY = window.scrollY;

      // Check for a downward scroll
      if (currentScrollY > lastScrollY && currentScrollY > 50) {
        // Find the _drawer element, which controls the sidebar's state
        const drawer = document.getElementById("_drawer");
        if (drawer) {
          drawer.close();
        }
      }

      lastScrollY = currentScrollY;
    }
  });

  // Optional: Add a simple swipe down to close
  let touchstartY = 0;
  
  document.addEventListener("touchstart", (e) => {
    touchstartY = e.touches[0].clientY;
  });

  document.addEventListener("touchend", (e) => {
    const touchendY = e.changedTouches[0].clientY;
    if (touchstartY < touchendY - 20 && isMobileOrTablet()) {
      // Swipe down gesture
      const drawer = document.getElementById("_drawer");
      if (drawer) {
        drawer.close();
      }
    }
  });
});