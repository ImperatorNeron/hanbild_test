// Function to check if SVG animation elements are in viewport
function checkSVGAnimation() {
    var svgContainer = document.querySelector('.road-svg');
    var svgElement = document.getElementById('svg1');
    var an_stroke = document.getElementById('an_stroke');
    var svgElement2 = document.getElementById('svg2');
    var an_stroke2 = document.getElementById('an_stroke2');

    if (isElementInViewportPlus(svgElement, 10)) {
        an_stroke.beginElement();
        an_stroke2.beginElement();
        svgContainer.style.opacity = '1';
        window.removeEventListener('scroll', checkSVGAnimation);
    }
}

// Function to check if an element is in viewport with a specified offset
function isElementInViewportPlus(el, offset) {
    var rect = el.getBoundingClientRect();
    var windowHeight = window.innerHeight || document.documentElement.clientHeight;
    return (
        rect.top - offset <= windowHeight &&
        rect.bottom >= 0
    );
}

window.addEventListener('scroll', checkSVGAnimation);

// Function to handle visibility of elements with 'point' class
function handleVisibility() {
    var points = document.querySelectorAll('.point');
    points.forEach(function (point) {
        if (isElementInViewportPlus(point, -75)) {
            point.classList.add('active');
        }
    });
}
window.addEventListener('scroll', handleVisibility);
window.addEventListener('load', handleVisibility);


const isIOS = /iPad|iPhone|iPod/.test(navigator.userAgent);

if (isIOS) {
    new Swiper('.reviews-swiper-container', {
        slidesPerView: 1,
        centeredSlides: true,
        spaceBetween: 100,

        slidesPerGroup: 1,
        loop: true,
        loopFillGroupWithBlank: false,

        pagination: {
            el: '.swiper-pagination',
            clickable: true,
        },
        navigation: {
            nextEl: '.button-next',
            prevEl: '.button-prev',
        },

        autoplay: {
            delay: 7000
        },
    });
} else {
    new Swiper('.reviews-swiper-container', {
        slidesPerView: 1,
        centeredSlides: true,
        spaceBetween: 100,

        slidesPerGroup: 1,
        loop: true,
        loopFillGroupWithBlank: false,

        pagination: {
            el: '.swiper-pagination',
            clickable: true,
        },
        navigation: {
            nextEl: '.button-next',
            prevEl: '.button-prev',
        },

        breakpoints: {
            720: {
                slidesPerView: 1,
                spaceBetween: 1000
            },
            972: {
                slidesPerView: 3,
                spaceBetween: 0

            },
        },
        autoplay: {
            delay: 7000
        },
    });
}
