let slideIndex = 1;
let currentImageIndex = 0;
const slides = document.getElementsByClassName("carousel-slide");
const images = document.querySelectorAll('.carousel-slide img');  // Get all the images in the carousel

// Show slides function
function showSlides(n) {
  if (n > slides.length) { slideIndex = 1; }
  if (n < 1) { slideIndex = slides.length; }
  for (let i = 0; i < slides.length; i++) {
    slides[i].style.display = "none";
  }
  slides[slideIndex - 1].style.display = "block";
}

// Function to handle the next/previous button clicks
function plusSlides(n) {
  showSlides(slideIndex += n);
}

// Function to open the image in view mode
function openImageView(index) {
  currentImageIndex = index;  // Set the index of the clicked image
  const viewer = document.getElementById('image-viewer');
  const viewerImg = document.getElementById('viewer-image');

  viewerImg.src = images[currentImageIndex].src;  // Set the src of the viewer image to the clicked image
  viewer.style.display = 'flex';  // Display the full-screen viewer
}

// Function to close the image viewer
function closeImageView() {
  const viewer = document.getElementById('image-viewer');
  viewer.style.display = 'none';
}

// Function to show the next image in view mode
function nextImageView() {
  currentImageIndex = (currentImageIndex + 1) % images.length;  // Loop to the first image
  document.getElementById('viewer-image').src = images[currentImageIndex].src;
}

// Function to show the previous image in view mode
function prevImageView() {
  currentImageIndex = (currentImageIndex - 1 + images.length) % images.length;  // Loop to the last image
  document.getElementById('viewer-image').src = images[currentImageIndex].src;
}

// Add event listener for keyboard navigation
document.addEventListener('keydown', function(event) {
  const viewer = document.getElementById('image-viewer');

  if (viewer.style.display === 'flex') {  // Only listen for keys if the viewer is open
    if (event.key === 'ArrowRight') {
      nextImageView();  // Show the next image
    } else if (event.key === 'ArrowLeft') {
      prevImageView();  // Show the previous image
    } else if (event.key === 'Escape') {
      closeImageView();  // Close the viewer when 'Escape' is pressed
    }
  } else {
    if (event.key === 'ArrowRight') {
      plusSlides(1);  // Navigate to the next slide
    } else if (event.key === 'ArrowLeft') {
      plusSlides(-1);  // Navigate to the previous slide
    }
  }
});

// Add click event listeners to open images in view mode
document.querySelectorAll('.carousel-slide').forEach((slide, index) => {
  slide.addEventListener('click', () => openImageView(index));
});

// Initially show the first slide
showSlides(slideIndex);
