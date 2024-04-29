// Selecting slider elements and other necessary DOM elements
let sliders = document.querySelectorAll(".my-slider");
let displayValOne = document.getElementById("range1");
let displayValTwo = document.getElementById("range2");
let minGap = 326000;
let sliderTrack = document.querySelector(".my-slider-track");
let sliderMaxValue = sliders[0].max;

// Event listeners for slider inputs
sliders[0].addEventListener("input", slideOne);
sliders[1].addEventListener("input", slideTwo);

// Event listener for input changes in displayValOne
displayValOne.addEventListener("input", function () {
    if (this.value == "") {
        sliders[0].value = 0;
    }
    else if (this.value > parseInt(sliders[1].value) - minGap) {
        sliders[0].value = parseInt(sliders[1].value) - minGap;
    } else {
        sliders[0].value = this.value;
    }
    fillColor();
});

// Event listener for input changes in displayValTwo
displayValTwo.addEventListener("input", function () {
    if (this.value == "") {
        sliders[1].value = 2000000;
    }
    else if (this.value < parseInt(sliders[0].value) + minGap) {
        sliders[1].value = parseInt(sliders[0].value) + minGap;
    } else {
        sliders[1].value = this.value;
    }
    fillColor();
});

// Function to handle input on first slider
function slideOne() {
    if (parseInt(sliders[1].value) - parseInt(sliders[0].value) <= minGap) {
        sliders[0].value = parseInt(sliders[1].value) - minGap;
    }
    displayValOne.value = sliders[0].value;
    fillColor();
}

// Function to handle input on second slider
function slideTwo() {
    if (parseInt(sliders[1].value) - parseInt(sliders[0].value) <= minGap) {
        sliders[1].value = parseInt(sliders[0].value) + minGap;
    }
    displayValTwo.value = sliders[1].value;
    fillColor();
}

// Function to set gradient background color of slider track based on slider values
function fillColor() {
    percent1 = (sliders[0].value / sliderMaxValue) * 100;
    percent2 = (sliders[1].value / sliderMaxValue) * 100;
    sliderTrack.style.background = `linear-gradient(to right, #dadae5 ${percent1}% , #f0500a ${percent1}% , #f0500a ${percent2}%, #dadae5 ${percent2}%)`;
}

fillColor();