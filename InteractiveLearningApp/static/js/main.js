// const navbar = document.querySelector('nav');
// const leftButton = document.querySelector('.left');
// const rightButton = document.querySelector('.right');

// const scrollStep = 100; 

// function handleScrollRight() {
//   navbar.scrollBy({
//     left: scrollStep,
//     behavior: 'smooth'
//   });
//   updateButtonVisibility();
// }

// function handleScrollLeft() {
//   navbar.scrollBy({
//     left: -scrollStep,
//     behavior: 'smooth'
//   });
//   updateButtonVisibility();
// }

// function updateButtonVisibility() {
//   leftButton.style.visibility = navbar.scrollLeft === 0 ? 'hidden' : 'visible';
//   rightButton.style.visibility =
//     navbar.scrollLeft + navbar.clientWidth >= navbar.scrollWidth ? 'hidden' : 'visible';
// }

// leftButton.addEventListener('click', handleScrollLeft);
// rightButton.addEventListener('click', handleScrollRight);

// navbar.addEventListener('scroll', updateButtonVisibility);

// window.addEventListener('resize', () => {
//   updateButtonVisibility();
// });



const navbar = document.querySelector('nav');
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
  leftButton.style.display = navbar.scrollLeft === 0 ? 'none' : 'block';
  rightButton.style.display =
    navbar.scrollLeft + navbar.clientWidth >= navbar.scrollWidth ? 'none' : 'block';
}

leftButton.addEventListener('click', handleScrollLeft);
rightButton.addEventListener('click', handleScrollRight);

navbar.addEventListener('scroll', updateButtonVisibility);

window.addEventListener('resize', () => {
  updateButtonVisibility();
});