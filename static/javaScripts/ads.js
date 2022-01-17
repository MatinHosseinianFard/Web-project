var adsIndex = 0;
ads_showSlides();

function ads_showSlides() {
  var i;
//   remember to change(add) for loops if ads slideshows have different number of pictures
  const slides = document.getElementsByClassName("adsSlides");
  const slides2 = document.getElementsByClassName('adsSlides2');

  for (i = 0; i < slides.length; i++) {
    slides[i].style.display = "none";
    if (slides2.length > 0 && i < 2)
      slides2[i].style.display = 'none';
  }
  adsIndex++;
  if (adsIndex > slides.length) {
      adsIndex = 1
  }    
  slides[adsIndex-1].style.display = "block";
  if (slides2.length > 0)
    slides2[adsIndex - 1].style.display = 'block';
  setTimeout(ads_showSlides, 10000); // Change image every 2 seconds
}