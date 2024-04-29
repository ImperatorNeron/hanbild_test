// Initialize Swiper for image slider
new Swiper('.image-slider', {
    navigation: {
        nextEl: '.button-next',
        prevEl: '.button-prev'
    },
    spaceBetween: 5,
    loop: true,
    slidesPerView: 1,
    thumbs: {
        swiper: {
            el: '.image-mini-slider',
            slidesPerView: 3,
            spaceBetween: 5,
            breakpoints: {
                520: {
                    slidesPerView: 5
                },
            },
        }
    },
});

// Event listener for DOMContentLoaded event
document.addEventListener('DOMContentLoaded', function () {
    const images = document.querySelectorAll('.image-slider__image img');
    const overlay = document.createElement('div');
    overlay.classList.add('overlay');
    document.body.appendChild(overlay);

    // Adding click event listener to each image
    images.forEach(img => {
        img.addEventListener('click', function () {
            const enlargedImg = img.cloneNode(true);
            enlargedImg.classList.add('image-slider__image--expanded');
            overlay.appendChild(enlargedImg);
            overlay.style.display = 'block';

            const closeBtn = document.querySelector('.close-btn');
            closeBtn.style.display = 'block';

            closeBtn.addEventListener('click', function () {
                overlay.style.display = 'none';
                overlay.innerHTML = '';
                closeBtn.style.display = 'none';
            });
        });
    });

    // Adding click event listener to overlay to close it
    overlay.addEventListener('click', function () {
        overlay.style.display = 'none';
        overlay.innerHTML = '';
        document.querySelector('.close-btn').style.display = 'none';
    });
});