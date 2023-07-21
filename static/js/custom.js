/* Carousel */
 window.addEventListener('resize', function() {
  resizeImages();
});

function resizeImages() {
  var carouselInner = document.querySelector('.carousel-inner');
  var images = carouselInner.getElementsByTagName('img');

  for (var i = 0; i < images.length; i++) {
    var image = images[i];
    image.style.height = carouselInner.offsetHeight + 'px';
  }
}

resizeImages(); // Chamada inicial para redimensionar as imagens