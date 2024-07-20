const searchBar = document.querySelector('.search-mobile-container');

const searchButton = document.querySelector('.search-button-mobile');

const closeSearch = document.querySelector('.close-search');

const navMenu = document.querySelector('.navlinks');

const menuButton = document.querySelector('.nav-menu');

const closeMenu = document.querySelector('.close-menu');


searchButton.addEventListener('click', function(){
    searchBar.style.display = 'flex';
})

closeSearch.addEventListener('click', function(){
    searchBar.style.display = 'none';
})

menuButton.addEventListener('click', function(){
    navMenu.style.display = 'block';
})

closeMenu.addEventListener('click', function(){
    navMenu.style.display = 'none';
})



const navbar = document.querySelector('.scroll-header');
const leftButton = document.querySelector('.left');
const rightButton = document.querySelector('.right');

const scrollStep = 100; 

function handleScrollRight() {
  navbar.scrollBy({
    left: scrollStep,
    behavior: 'smooth'
  });
  updateButtonVisibility();
}

function handleScrollLeft() {
  navbar.scrollBy({
    left: -scrollStep,
    behavior: 'smooth'
  });
  updateButtonVisibility();
}

function updateButtonVisibility() {
  leftButton.style.visibility = navbar.scrollLeft === 0 ? 'hidden' : 'visible';
  rightButton.style.visibility =
    navbar.scrollLeft + navbar.clientWidth >= navbar.scrollWidth ? 'hidden' : 'visible';
}

leftButton.addEventListener('click', handleScrollLeft);
rightButton.addEventListener('click', handleScrollRight);

navbar.addEventListener('scroll', updateButtonVisibility);

window.addEventListener('resize', () => {
  updateButtonVisibility();
});


const sidebar = document.querySelector('.sidebar');
const sidebarButton = document.querySelector('.sidebar-toggle-button');

sidebarButton.addEventListener('click', () => {
  sidebar.classList.toggle('show');
  navbar.classList.add('border');

  if (sidebar.classList.contains('show')) {
    sidebarButton.innerHTML = '&times;'; // Change to times symbol
  } else {
    sidebarButton.innerHTML = '&#8801;'; // Change back to menu symbol
  }
});