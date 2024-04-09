// main.js

document.querySelectorAll('.add-to-cart-btn').forEach(function(btn) {
    btn.addEventListener('click', function(event) {
      event.preventDefault();
      var productId = this.getAttribute('id');
      var csrftoken = Cookies.get('csrftoken');
      $.ajax({
        url: '/add/',
        method: 'POST',
        data: {
          'product_id': productId,
          'csrfmiddlewaretoken': csrftoken
        },
        success: function(response) {
          console.log(response);
          // обновить интерфейс пользователя
        },
        error: function(xhr, textStatus, errorThrown) {
          console.log(xhr.responseText);
        }
      });
    });
  });
  