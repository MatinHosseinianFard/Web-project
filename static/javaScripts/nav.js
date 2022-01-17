var html = document.documentElement;

var check = false;

var _check_the_category = true;

const moon = document.getElementsByClassName('moon');
const light_dark_div = document.getElementsByClassName('www');

var check_dark = "light";

if (localStorage.getItem('DarkOrLight') == null){
    localStorage.setItem('DarkOrLight', check_dark)
}
else if (localStorage.getItem('DarkOrLight') == 'dark'){
    check_dark = 'light'
    dark_light();
}

// window.addEventListener('scroll', scroll_down_to_show)

function scroll_down_to_show() {
    var y = window.scrollY;
    let height = document.getElementById('body-height').style.height;
    console.log(height)
    let elemet = document.getElementById('go-to-top');
    if (y >= 250){
        elemet.style.display = 'block';
        elemet.style.bottom = '20px'
    }
    else {
        elemet.style.display = 'none'
    }
}

function openNav() {
    document.getElementById("myNav").style.width = "50%";
}
  
function closeNav() {
    document.getElementById("myNav").style.width = "0%";
    setTimeout(proccess, 500)
    check = false;
}

function openCatNav(){

    document.getElementById("catNav").style.height = '290';
    //document.getElementById("catNav").style.animationName = 'animate'
    let choose_triangle = document.getElementById('first_tri');
    choose_triangle.innerHTML = ' &#9650;';
    html.addEventListener('click', _menu_closed_on_bodyClicked)
    
}

function closeCatNav(){
    if (_check_the_category){
        document.getElementById("catNav").style.height = '0';
        document.getElementById('first_tri').innerHTML = ' &#9660;';
    }
}

function _menu_closed_on_bodyClicked(event){
    const path = event.composedPath();

    if (path.some(elem => elem.id === "categoryLi"))
        return

    _check_the_category = true;
    closeCatNav();
    html.removeEventListener('click', _menu_closed_on_bodyClicked);
}

function clickOn_category(){

    if (_check_the_category){
        _check_the_category = false;
        openCatNav();
    }
    else {

        _check_the_category = true;
        closeCatNav();
    }
}

function category(){

    if (!check){
        var array = document.getElementsByClassName("se3");

        for (let i = 0; i < array.length; i++){
            array[i].style.display = "none";
        }

        var cat = document.getElementsByClassName("se_nested");

        for (let i = 0; i < cat.length; i++){
            cat[i].style.display = "block"
        }
        check = true;
        document.getElementById('mobile_tri').innerHTML = ' &#9650;';
    }
    else {
        proccess();
        check = false;
        document.getElementById('mobile_tri').innerHTML = ' &#9660;';
    }
}

function proccess(){
    var array = document.getElementsByClassName("se3");
    document.getElementById("mobile_tri").innerHTML = ' &#9660;';

    for (let i = 0; i < array.length; i++){
        array[i].style.display = "block";
    }

    var cat = document.getElementsByClassName("se_nested");

    for (let i = 0; i < cat.length; i++){
        cat[i].style.display = "none"
    }
}

function dark_light(){
    if (check_dark === "dark"){
        dark.media = 'none';
        light.media = '';
        check_dark = "light";
        localStorage.setItem('DarkOrLight', check_dark)


        for (let i = 0; i < moon.length; i++){
            moon[i].style.opacity = '0';
        }

        const delay = ms => new Promise(res => setTimeout(res, ms));
        const fading = async() => {
            await delay(300)
            for (let i = 0; i < moon.length; i++){
                moon[i].innerHTML = '&#9728;';
                moon[i].style.opacity = '1';
            }
        }
        fading();
        for (let i = 0; i < light_dark_div.length; i++){
            light_dark_div[i].style.left = '-31.5px';
        }
    }
    else {
        dark.media = ''
        light.media = 'none';
        check_dark = "dark";
        localStorage.setItem("DarkOrLight", check_dark)

        for (let i = 0; i < moon.length; i++){
            moon[i].style.opacity = '0';
        }

        const delay = ms => new Promise(res => setTimeout(res, ms));
        const fading = async() => {
            await delay(300)
            for (let i = 0; i < moon.length; i++){
                moon[i].innerHTML = '&#9789;';
                moon[i].style.opacity = '1';
            }
        }
        fading();
        for (let i = 0; i < light_dark_div.length; i++){
            light_dark_div[i].style.left = '2px';
        }
    }
}