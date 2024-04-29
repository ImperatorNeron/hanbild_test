// Selecting slider elements and other necessary DOM elements
let sliders1 = document.querySelectorAll(".my-slider1");
let displayValOne1 = document.getElementById("range11");
let displayValTwo1 = document.getElementById("range21");
let minGap1 = 326000;
let sliderTrack1 = document.querySelector(".my-slider-track1");
let sliderMaxValue1 = sliders1[0].max;

// Event listeners for slider inputs
sliders1[0].addEventListener("input", slideOne1);
sliders1[1].addEventListener("input", slideTwo1);

// Event listener for input changes in displayValOne1
displayValOne1.addEventListener("input", function () {
    if (this.value == "") {
        sliders1[0].value = 0;
    }
    else if (this.value > parseInt(sliders1[1].value) - minGap1) {
        sliders1[0].value = parseInt(sliders1[1].value) - minGap1;
    } else {
        sliders1[0].value = this.value;
    }
    fillColor1();
});

// Event listener for input changes in displayValTwo1
displayValTwo1.addEventListener("input", function () {
    if (this.value == "") {
        sliders1[1].value = 2000000;
    }
    else if (this.value < parseInt(sliders1[0].value) + minGap1) {
        sliders1[1].value = parseInt(sliders1[0].value) + minGap1;
    } else {
        sliders1[1].value = this.value;
    }
    fillColor1();
});

// Function to handle input on first slider
function slideOne1() {
    if (parseInt(sliders1[1].value) - parseInt(sliders1[0].value) <= minGap1) {
        sliders1[0].value = parseInt(sliders1[1].value) - minGap1;
    }
    displayValOne1.value = sliders1[0].value;
    fillColor1();
}

// Function to handle input on second slider
function slideTwo1() {
    if (parseInt(sliders1[1].value) - parseInt(sliders1[0].value) <= minGap1) {
        sliders1[1].value = parseInt(sliders1[0].value) + minGap1;
    }
    displayValTwo1.value = sliders1[1].value;
    fillColor1();
}

// Function to set gradient background color of slider track based on slider values
function fillColor1() {
    percent1 = (sliders1[0].value / sliderMaxValue1) * 100;
    percent2 = (sliders1[1].value / sliderMaxValue1) * 100;
    sliderTrack1.style.background = `linear-gradient(to right, #dadae5 ${percent1}% , #f0500a ${percent1}% , #f0500a ${percent2}%, #dadae5 ${percent2}%)`;
}

fillColor1();