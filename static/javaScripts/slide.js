
var timeOut;
var slideIndex = 0;
var check1 = true, fadeOut = null;
var className = "mySlides"
clearTimeout(timeOut)
showSlides();
var dotsSize = 16;

const dark = document.getElementById('dark');
const light = document.getElementById('light');

// Next/previous controls
function plusSlides(n) {
  if (n == -2){
    check1 = false;
  }
  if (n == -2 && slideIndex == 1)
    n = 1;
  slideIndex += n
  clearTimeout(timeOut)
  showSlides();
}

// Thumbnail image controls
function currentSlide(n) {
  slideIndex = n - 1
  clearTimeout(timeOut)
  showSlides();
}

function showSlides() {
   
  var n = slideIndex;
  var i;
  var slides = document.getElementsByClassName("mySlides");
  var dots = document.getElementsByClassName("dot");

  if (n > slides.length) {
    slideIndex = 1
  }
  if (n < 1) {
    slideIndex = slides.length
  }

  for (i = 0; i < slides.length; i++) {
    if (fadeOut != null){
      if (slides[i].id != fadeOut.toString()){
        slides[i].style.display = "none";
        slides[i].style.opacity = "0";
      }
    }
    else {
       slides[i].style.display = "none";
       slides[i].style.opacity = '0'
    }
  }

  for (let i = 0; i < slideIndex; i++){
    dots[i].style.width = 15 - slideIndex + i + 'px';
    dots[i].style.height = 15 - slideIndex + i + 'px';
  }

  slideIndex++;
  if (slideIndex > slides.length){
    slideIndex = 1;
  }

  for (i = 0; i < dots.length; i++) {
      dots[i].className = dots[i].className.replace(" active", "");
  }

  if (fadeOut != null)
    document.getElementById((fadeOut).toString()).style.opacity = '0';
    
    slides[slideIndex-1].style.display = 'block'

    const delay = ms => new Promise(res => setTimeout(res, ms));
    const delay_to_fade_in = async() => {
        await delay(900)
        
        slides[slideIndex-1].style.opacity = "1";
    }
    delay_to_fade_in();

  
  dots[slideIndex-1].className += " active";
  dots[slideIndex - 1].style.width = '16px';
  dots[slideIndex - 1].style.height = '16px';
  for (let i = slideIndex; i < dots.length; i++){
    dots[i].style.width = 14 - i + slideIndex + 'px';
    dots[i].style.height = 14 - i + slideIndex + 'px';
  }
  fadeOut = slideIndex;
  timeOut = setTimeout(showSlides, 5000)
}

