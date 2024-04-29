// Handle initial setup when the document is ready
$(document).ready(function () {
    // Selecting necessary elements
    var successMessage = $("#jq-notification");
    var goodsInCartCount = $("#cartCount");
    var cartCount = parseInt(goodsInCartCount.text() || 0);
    var is_uk_language = document.cookie.includes("django_language=uk")


    // Checking cart quantity initially
    check_carts_quantity();

    // Function to display a message on the screen
    function sendMessageToScreen(message) {
        successMessage.html(message);
        successMessage.fadeIn(400);
        setTimeout(function () {
            successMessage.fadeOut(400);
        }, 4000);
    }

    // Function to update HTML content
    function updateHTML(cart_items_html) {
        var cartItemsContainer = $("#cartContainer");
        cartItemsContainer.html(cart_items_html);
    }

    // Function to make AJAX POST request
    function ajaxPostRequest(url, data, success, error) {
        $.ajax({
            type: "POST",
            url: url,
            data: data,
            success: success,
            error: error,
        });
    }

    // Function to get cart item details
    function getCartItem(e, element) {
        e.preventDefault();
        var url = $(element).attr("href");
        var cartID = $(element).data("cart-id");
        var quantity_displayer = $(element).closest('.cart-item').find('.quantity_displayer');
        var currentValue = parseInt(quantity_displayer.text());
        return { cartID, quantity_displayer, currentValue, url }
    }

    // Function to validate form response
    function validateForm(response) {
        document.querySelectorAll(response.error_class).forEach(function (element) {
            element.textContent = "";
        });
        if (response.data.success == true) {
            $(response.form_id).trigger('reset');
            sendMessageToScreen(response.data.message);
            document.querySelectorAll(response.error_class).forEach(function (element) {
                element.style.display = "none";
            });
            return true
        }
        document.querySelectorAll(response.error_class).forEach(function (element) {
            element.style.display = "block";
        });
        // Setting error messages for specific fields
        $(response.number_or_email_error_field_id).text(response.data.form_errors.number_or_email);
        $(response.name_error_field_id).text(response.data.form_errors.name);
        return false
    }

    // Function to update cart quantity
    function updateCart(cartID, quantity, url) {
        data = {
            cart_id: cartID,
            quantity: quantity,
            csrfmiddlewaretoken: $("[name=csrfmiddlewaretoken]").val(),
        }

        function success(data) {
            goodsInCartCount.text(data.total_quantity);
            updateHTML(data.cart_items_html);
        }

        function error(data) {
            console.log("Помилка при зміні кількості товару");
        }

        ajaxPostRequest(url, data, success, error)
    }

    // Function to check cart quantity and display/hide accordingly
    function check_carts_quantity() {
        if (cartCount > 0) {
            goodsInCartCount.css("display", "flex");
        } else {
            goodsInCartCount.css("display", "none");
        }
    }

    // Event listener for adding an item to cart
    $(document).on("click", ".add-to-cart", function (e) {
        e.preventDefault();
        var url = $(this).attr("href");

        data = {
            product_id: $(this).data("product-id"),
            csrfmiddlewaretoken: $("[name=csrfmiddlewaretoken]").val(),
        }

        function success(data) {
            sendMessageToScreen(data.message)
            cartCount++;
            goodsInCartCount.text(cartCount);
            check_carts_quantity();
            updateHTML(data.cart_items_html);
        }

        function error(data) {
            console.log("Помилка при додавані товару в корзину");
        }

        ajaxPostRequest(url, data, success, error);
    });

    // Event listener for removing an item from cart
    $(document).on("click", ".remove-btn", function (e) {
        e.preventDefault();

        data = {
            cart_id: $(this).data("cart-id"),
            csrfmiddlewaretoken: $("[name=csrfmiddlewaretoken]").val(),
        }

        function success(data) {
            sendMessageToScreen(data.message);
            goodsInCartCount.text(data.total_quantity);
            cartCount = data.total_quantity;
            check_carts_quantity();
            if (cartCount == 0) {
                location.reload();
            }
            else {
                updateHTML(data.cart_items_html);
            }
        }

        function error(data) {
            console.log("Помилка при видалені товару з корзини");
        }

        ajaxPostRequest($(this).attr("href"), data, success, error);
    });

    // Event listener for decreasing quantity of cart item
    $(document).on("click", ".minus-btn", function (e) {
        item = getCartItem(e, this);
        if (item.currentValue > 1) {
            item.quantity_displayer.val(item.currentValue - 1);
            updateCart(item.cartID, item.currentValue - 1, item.url);
        }
    });

    // Event listener for increasing quantity of cart item
    $(document).on("click", ".plus-btn", function (e) {
        item = getCartItem(e, this);
        item.quantity_displayer.val(item.currentValue + 1);
        updateCart(item.cartID, item.currentValue + 1, item.url);
    });

    // Event listener for removing all items from cart
    $(document).on("click", ".remove-all-carts", function (e) {
        e.preventDefault();

        data = {
            csrfmiddlewaretoken: $("[name=csrfmiddlewaretoken]").val()
        }

        function success(data) {
            location.reload();
        }

        function error(data) {
            console.log("Помилка при видалені товару з корзини");
        }

        ajaxPostRequest($(this).data("url"), data, success, error);
    })

    // Event listener for submitting feedback form
    $('#contact-form').on('submit', function (e) {
        e.preventDefault();

        function success(data) {
            response = {
                data: data,
                form_id: '#contact-form',
                error_class: ".validation-error",
                number_or_email_error_field_id: "#user_number_or_email",
                name_error_field_id: "#user_name"
            }
            if (validateForm(response)) {
                document.querySelector('.popup-contact-form').classList.remove('active');
                document.querySelector('.additional-elements').style.display = ''
                document.body.style.overflow = '';
            }
            $('#loading-overlay').hide();
        }

        function error(data) {
            document.body.style.overflow = '';
            console.log("Помилка при надсилані повідомлення!");
            $('#loading-overlay').hide();
        }
        $('#loading-overlay').show();
        ajaxPostRequest(window.location.href, $(this).serialize(), success, error)
    });

    // Event listener for submitting page contact form
    $('#page-contact-form').on('submit', function (e) {
        e.preventDefault();

        function success(data) {
            response = {
                data: data,
                form_id: '#page-contact-form',
                error_class: ".page-validation-error",
                number_or_email_error_field_id: "#page_number_or_email",
                name_error_field_id: "#page_name"
            }
            validateForm(response);
            $('#loading-overlay').hide();
        }

        function error(data) {
            $('#loading-overlay').hide();
            console.log("Помилка при надсилані повідомлення!");
        }
        $('#loading-overlay').show();
        ajaxPostRequest(window.location.href, $(this).serialize(), success, error)
    });

    // Event listener for clicking confirm order button
    $("#id-confirm-order-button").on("click", function () {
        $("#id-order-form").submit();
    });

    // Event listener for submitting order form
    $("#id-order-form").on("submit", function (e) {
        e.preventDefault();

        function success(data) {
            if (data.success) {
                window.location.href = data.url
            } else {
                if (is_uk_language) {
                    sendMessageToScreen("Похибка у формі. Спробуйте ще раз.")
                } else {
                    sendMessageToScreen("Error in form. Try again.")
                }
                data.form_errors.forEach(element => {
                    $(element[0]).text(element[1]);
                });
                var inputs = document.querySelectorAll('.order-box .point input');
                document.querySelectorAll(".error-massage").forEach(function (element, index) {
                    if (element.textContent.trim().length > 0) {
                        element.style.display = "block";
                        inputs[index].classList.add("active-input")
                    } else {
                        element.style.display = "none";
                        inputs[index].classList.remove("active-input")
                    }
                });
            }
            $('#loading-overlay').hide();
        }

        function error(data) {
            console.log("Помилка при створенні замовлення!");
            $('#loading-overlay').hide();
        }
        $('#loading-overlay').show();
        ajaxPostRequest(window.location.href, $(this).serialize(), success, error)
    })
});