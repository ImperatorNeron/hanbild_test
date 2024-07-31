document.addEventListener("DOMContentLoaded", function () {
    document.getElementById("burger").addEventListener("click", function () {
        document.querySelector(".wrapper").classList.toggle("open")
    })
})

window.addEventListener('keydown', (e) => {
    if (e.key === "Escape") {
        document.querySelector(".wrapper").classList.remove("open")
    }
});

document.addEventListener('DOMContentLoaded', function () {
    var serviceLinks = document.querySelectorAll('.service-link');
    if (serviceLinks) {
        serviceLinks.forEach(function (link) {
            link.addEventListener('click', function () {
                document.querySelector(".wrapper").classList.remove("open")
                return
            });
        });
    }
});

document.getElementById("menu").addEventListener('click', event => {
    event._isClickWithInMenu = true;
});
document.getElementById("burger").addEventListener('click', event => {
    event._isClickWithInMenu = true;
});
document.body.addEventListener('click', event => {
    if (event._isClickWithInMenu) return;
    document.querySelector(".wrapper").classList.remove("open")
});

const filter_menu_btn = document.getElementById("filter-menu-btn")

if (filter_menu_btn) {
    filter_menu_btn.addEventListener('click', function () {
        document.querySelector(".wrapper").classList.remove("open-filter");
    });
}

window.addEventListener('keydown', (e) => {
    if (e.key === "Escape") {
        document.querySelector(".wrapper").classList.remove("open-filter")
    }
});

document.body.addEventListener('click', event => {
    if (event._isClickWithInMenu) return;
    document.querySelector(".wrapper").classList.remove("open-filter")
});

document.addEventListener("DOMContentLoaded", function () {
    const button_filter = document.getElementById("button-filter")
    if (button_filter) {
        document.getElementById("button-filter").addEventListener("click", function () {
            document.querySelector(".wrapper").classList.toggle("open-filter")
        })
    }
})

const filter_menu = document.getElementById("filter-menu")
const button_filter = document.getElementById("button-filter")

if (filter_menu) {
    filter_menu.addEventListener('click', event => {
        event._isClickWithInMenu = true;
    });
}

if (button_filter) {
    button_filter.addEventListener('click', event => {
        event._isClickWithInMenu = true;
    });
}

document.addEventListener("DOMContentLoaded", function () {
    var submenus = document.querySelectorAll('.burgermenu');
    submenus.forEach(function (submenu) {
        var id = submenu.id;
        var state = localStorage.getItem(id) || "closed";
        if (state === "open") {
            submenu.style.display = "flex";
        } else {
            submenu.style.display = "none";
        }
    });
});

// Function to handle accepting cookies by setting a cookie and hiding the cookie notice
function handleAcceptCookies() {
    var now = new Date();
    var expires = new Date(now.getTime() + 30 * 24 * 60 * 60 * 1000); // дата через 30 днів

    document.cookie = "allow-cookie-usage=true; path=/; expires=" + expires.toUTCString();
    document.querySelector(".cookies").style.display = "none";
    var button = document.querySelector('.additional-elements');
    button.style.bottom = '40px';
}

var acceptButton = document.getElementById("cookies-accept-button");
if (acceptButton) {
    acceptButton.addEventListener("click", handleAcceptCookies);
}

if (!document.querySelector(".cookies")) {
    var button = document.querySelector('.additional-elements');
    button.style.bottom = '40px';
}

// Function to set up language 
function setupLanguageSelection() {
    document.querySelectorAll('.language-link').forEach(function (link) {
        link.addEventListener('click', function (e) {
            e.preventDefault()
            var languageCode = this.getAttribute('data-lang-code')
            document.querySelector('#languageForm input[name="language"]').value = languageCode
            document.getElementById('languageForm').submit()
        })
    })
}

window.addEventListener('DOMContentLoaded', setupLanguageSelection);
document.getElementById('languageSelect').onchange = function () {
    document.getElementById('languageFormFooter').submit();
};

document.getElementById('languageSelectFooter').onchange = function () {
    document.getElementById('languageFormFooter2').submit();
};

// Function to start animation for pulsating element
function startAnimation() {
    var pulseButton = document.querySelector('.pulsating-element');
    pulseButton.style.animation = 'pulse linear 1s infinite';
    setTimeout(function () {
        pulseButton.style.animation = 'none';
        setTimeout(startAnimation, 3000);
    }, 1000);
}

startAnimation();

// Function to toggle submenu visibility and store state in local storage
function toggleSubmenu(id) {
    if (window.innerWidth <= 680){
        var submenu = document.getElementById(id);
        if (submenu.style.display === "none") {
            submenu.style.display = "flex";
            localStorage.setItem(id, "open");
        } else {
            submenu.style.display = "none";
            localStorage.setItem(id, "closed");
        }
    }
}

document.addEventListener("DOMContentLoaded", function () {
    var submenus = document.querySelectorAll('.filtermenu');
    submenus.forEach(function (submenu) {
        var id = submenu.id;
        var state = localStorage.getItem(id);
        if (state === "open") {
            submenu.style.display = "flex";
        } else if (state === "closed") {
            submenu.style.display = "none";
        }
    });
});


// Function to handle scroll behavior and display scroll-to-top button
window.onscroll = function () { scrollFunction() };

function scrollFunction() {
    if (document.body.scrollTop > 20 || document.documentElement.scrollTop > 20) {
        document.getElementById("scrollToTopBtn").style.display = "block";
    } else {
        document.getElementById("scrollToTopBtn").style.display = "none";
    }
}

document.getElementById("scrollToTopBtn").onclick = function () {
    window.scrollTo({ top: 0, behavior: 'smooth' });
}

// Function to handle opening and closing pop-up contact form
const catalogMessageButtons = document.querySelectorAll('.catalog-message');
const openPopUp = document.querySelector('.pulsating-element');
const closePopUp = document.querySelector('.close-button');
const popUp = document.querySelector('.popup-contact-form');
const additionalElements = document.querySelector('.additional-elements');
const scroll_body = document.getElementById("scroll-body")

function handlePopUpFormClick(event) {
    event.preventDefault();
    document.body.setAttribute('scroll', 'no');
    document.body.style.overflow = 'hidden';
    popUp.classList.add('active');
    additionalElements.style.display = 'none';
}

catalogMessageButtons.forEach(button => {
    button.addEventListener('click', handlePopUpFormClick);
});

openPopUp.addEventListener('click', handlePopUpFormClick);

closePopUp.addEventListener('click', () => {
    popUp.classList.remove('active');
    document.body.removeAttribute('scroll');
    document.body.style.overflow = '';
    additionalElements.style.display = '';
})

// Function to toggle submit button based on agreement checkbox state
function setupSubmitButton(agreementCheckboxId, submitButtonClass, submitButtonWrapperClass) {
    var agreementCheckbox = document.getElementById(agreementCheckboxId);
    var submitButton = document.querySelector(submitButtonClass);
    var submitButtonWrapper = document.querySelector(submitButtonWrapperClass);

    function toggleSubmitButton() {
        if (agreementCheckbox.checked) {
            changeStyle(false, "#f0500a", "black");
        } else {
            changeStyle(true, "#fc9a79", "#666666");
        }
    }

    function changeStyle(is_active, bg_color, color) {
        submitButton.disabled = is_active;
        submitButtonWrapper.style.backgroundColor = bg_color;
        submitButtonWrapper.style.color = color;
    }

    if (agreementCheckbox) agreementCheckbox.addEventListener('change', toggleSubmitButton);
}

document.addEventListener('DOMContentLoaded', function () {
    setupSubmitButton('feedback-agreement', '.feedback-submit-button', '.feedback-submit-button-wrapper');
    setupSubmitButton('contact-agreement', '.contact-submit-button', '.contact-submit-button-wrapper');
});

// Update URL with goods quantity parameter on input change
var goodsQuantityInput = document.getElementById("id_goods_quantity");

if (goodsQuantityInput) {
    goodsQuantityInput.addEventListener("change", function () {
        var url = new URL(window.location.href);
        url.searchParams.set('quantity', this.value);
        window.location.href = url;
    });
}

// Toggle visibility of vacancy details and associated resume
var vacancies = document.querySelectorAll(".vacancy-block")
var resumes = document.querySelectorAll(".vacancy-resume")
var arrows = document.querySelectorAll(".click-arrow")

if (vacancies) {
    vacancies.forEach((vacancy, index) => {
        vacancy.addEventListener('click', (e) => {
            if (vacancy.classList.contains("vacancy-block-selected")) {
                resumes[index].style.display = "none";
                vacancy.classList.remove('vacancy-block-selected');
                vacancy.classList.add('vacancy-block');
                arrows[index].style.transform = 'rotate(0deg)';
            } else {
                resumes[index].style.display = "flex";
                vacancy.classList.remove('vacancy-block');
                vacancy.classList.add('vacancy-block-selected');
                arrows[index].style.transform = 'rotate(180deg)';
            }
        });
    });
}

// Function to reload the page if it's being loaded from the cache
(function () {
    window.onpageshow = function (event) {
        if (event.persisted) {
            window.location.reload();
        }
    };
})();